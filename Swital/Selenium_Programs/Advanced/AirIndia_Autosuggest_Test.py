"""Simple positive test: enter From/To on airindia.com and select autosuggestions.

This script is intentionally tolerant of varying DOM structures: it tries
multiple locator strategies for the From/To inputs and for suggestion lists.

Usage: run with the project's virtualenv where ChromeDriver is available.
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def find_input(driver, label_text: str):
    """Try several XPath strategies to find an input for a given label."""
    text = label_text.lower()
    xpaths = [
        f"//input[contains(translate(@placeholder,'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'), '{text}')]",
        f"//input[contains(translate(@aria-label,'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'), '{text}')]",
        f"//label[contains(translate(.,'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'), '{text}')]/following::input[1]",
    ]
    for xp in xpaths:
        elems = driver.find_elements(By.XPATH, xp)
        if elems:
            for e in elems:
                try:
                    if e.is_displayed() and e.is_enabled():
                        return e
                except Exception:
                    continue
    # fallback: look for combobox or text inputs and choose by heuristic
    comboboxes = driver.find_elements(By.XPATH, "//*[@role='combobox']")
    if comboboxes:
        for cb in comboboxes:
            # try to find an input inside the combobox
            try:
                child_inputs = cb.find_elements(By.XPATH, ".//input")
                for ci in child_inputs:
                    if ci.is_displayed() and ci.is_enabled():
                        return ci
            except Exception:
                continue

    text_inputs = driver.find_elements(By.XPATH, "//input[@type='text' or @type='search' or not(@type)]")
    if text_inputs:
        # prefer first for 'from', second for 'to' when available
        candidates = text_inputs
        if 'from' in text and len(candidates) >= 1:
            cand = candidates[0]
            if cand.is_displayed() and cand.is_enabled():
                return cand
        if 'to' in text and len(candidates) >= 2:
            cand = candidates[1]
            if cand.is_displayed() and cand.is_enabled():
                return cand
        for cand in candidates:
            if cand.is_displayed() and cand.is_enabled():
                return cand

    raise RuntimeError(f"Could not locate input for '{label_text}'")


def select_suggestion(driver, input_elem, query: str, timeout: int = 10) -> bool:
    """Wait for suggestion elements to appear and click the one that contains `query`.

    Returns True if an item was clicked, False otherwise.
    """
    wait = WebDriverWait(driver, timeout)
    # Combined XPath for common suggestion containers
    suggestions_xp = (
        "//ul[contains(@class,'suggest') or contains(@class,'ui-autocomplete')]/li | "
        "//div[contains(@class,'suggest') or contains(@id,'suggest')]/div | "
        "//div[contains(@class,'autocomplete')]/div | //li"
    )

    wait.until(lambda d: len(d.find_elements(By.XPATH, suggestions_xp)) > 0)
    items = driver.find_elements(By.XPATH, suggestions_xp)
    q = query.lower()

    # matching strategies to try in order
    strategies = [
        lambda t: q == t,                 # exact match
        lambda t: t.startswith(q),        # starts with
        lambda t: q in t,                 # contains
        lambda t: any(tok.startswith(q) for tok in t.split()),
    ]

    for strat in strategies:
        for item in items:
            text = (item.text or "").strip().lower()
            if not text:
                continue
            if strat(text):
                try:
                    item.click()
                except ElementClickInterceptedException:
                    try:
                        driver.execute_script("arguments[0].scrollIntoView({block:'center'});", item)
                        driver.execute_script("arguments[0].click();", item)
                    except Exception:
                        continue

                # verify the input's value updated to include the query (some sites update a hidden input)
                try:
                    WebDriverWait(driver, timeout).until(
                        lambda d: (input_elem.get_attribute('value') or '').strip() != '' and q in (input_elem.get_attribute('value') or '').lower()
                    )
                    return True
                except Exception:
                    # not matched, try next candidate
                    continue

    # final fallback: try clicking each suggestion until input updates
    for item in items:
        try:
            item.click()
        except ElementClickInterceptedException:
            try:
                driver.execute_script("arguments[0].scrollIntoView({block:'center'});", item)
                driver.execute_script("arguments[0].click();", item)
            except Exception:
                continue
        try:
            WebDriverWait(driver, timeout).until(
                lambda d: (input_elem.get_attribute('value') or '').strip() != '' and q in (input_elem.get_attribute('value') or '').lower()
            )
            return True
        except Exception:
            continue

    return False


def main():
    driver = webdriver.Chrome()
    try:
        driver.maximize_window()
        driver.get("https://www.airindia.in/")

        # try to dismiss cookie/privacy overlays that block interactions
        try:
            # common OneTrust accept button
            btn = driver.find_element(By.ID, "onetrust-accept-btn-handler")
            if btn.is_displayed():
                btn.click()
        except Exception:
            # fallback: remove known overlay elements via JS
            driver.execute_script("""
                document.querySelectorAll('[class*="onetrust"], [id*="onetrust"], .ot-sdk-container, .onetrust-pc-dark-filter').forEach(e=>e.remove());
            """)

        wait = WebDriverWait(driver, 15)

        # Positive scenario: From 'Delhi' -> To 'Mumbai'
        from_input = find_input(driver, "From")
        from_input.clear()
        from_input.send_keys("Delhi")
        assert select_suggestion(driver, "Delhi"), "Failed to select From suggestion"

        # small pause to allow the UI to stabilise
        time.sleep(1)

        to_input = find_input(driver, "To")
        to_input.clear()
        to_input.send_keys("Mumbai")
        assert select_suggestion(driver, "Mumbai"), "Failed to select To suggestion"

        # if we reach here the basic positive flow succeeded
        print("PASS: selected From and To suggestions")
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
