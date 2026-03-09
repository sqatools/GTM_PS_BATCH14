# Dummy Booking Website Automation Test Plan

**Website:** https://sqatools.in/dummy-booking-website/

The plan is divided into **5 phases**. Each phase contains positive test cases with detailed steps.

---

## Phase 1 – Navigation & Page Load

1. **TC1 – Open website and verify title**
   - Step 1: Launch browser (Chrome headless via test framework).
   - Step 2: Navigate to the URL.
   - Step 3: Wait for page to load.
   - Step 4: Assert the page title contains "Dummy Booking" or expected text.

2. **TC2 – Verify essential elements are present**
   - Step 1: After navigation, locate key form fields (e.g., first name, last name, email).
   - Step 2: Assert each element is displayed and enabled.

---

## Phase 2 – Personal Details Entry

1. **TC3 – Enter valid first and last name**
   - Step 1: Locate first name field and input a valid string.
   - Step 2: Locate last name field and input a valid string.
   - Step 3: Verify the values are entered correctly.

2. **TC4 – Enter contact information**
   - Step 1: Input a well‑formed email address.
   - Step 2: Input a valid phone number.
   - Step 3: Ensure both fields accept the data.

---

## Phase 3 – Booking Details

1. **TC5 – Select booking dates**
   - Step 1: Click the check‑in date picker and choose a valid date.
   - Step 2: Click the check‑out date picker and choose a later valid date.
   - Step 3: Confirm the dates are displayed correctly.

2. **TC6 – Choose room type & quantity**
   - Step 1: Locate room‑type dropdown and select an option.
   - Step 2: Change number of guests to a valid integer.
   - Step 3: Verify selections persisted.

---

## Phase 4 – Additional Options & Submission

1. **TC7 – Fill optional fields (e.g., special requests)**
   - Step 1: Enter text in any comment or request box.
   - Step 2: Attach a file if upload is supported.
   - Step 3: Verify the file name appears.

2. **TC8 – Submit booking form**
   - Step 1: Click the "Submit" or "Book" button.
   - Step 2: Wait for response/redirect.
   - Step 3: Ensure no error messages are shown.

---

## Phase 5 – Confirmation & Post‑Submission

1. **TC9 – Verify confirmation message/page**
   - Step 1: After submission, verify the user is redirected to a confirmation page or message appears.
   - Step 2: Assert presence of booking reference number or success text.

2. **TC10 – Return to home and re‑open form**
   - Step 1: Click "Back to home" or manually navigate to the URL.
   - Step 2: Confirm the form loads empty and is ready for new input.

---

> All test cases assume the application is in a clean state and network connectivity is available. Data used for positive tests should be valid and consistent with application requirements.