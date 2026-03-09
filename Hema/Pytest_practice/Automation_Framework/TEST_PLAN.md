# Test Plan for Dummy Booking Website

**Website URL:** https://sqatools.in/dummy-booking-website/

This test plan covers positive or happy‑path scenarios organized into five phases. Each test case includes step-by-step actions and expected results.

---

## Phase 1 – Navigation & Page Load

### TC‑1.1: Open homepage and verify title
1. Launch a browser and navigate to the URL.
2. Wait for page to load completely.
3. Verify that the browser title/customer greeting appears (e.g. "Dummy Booking Website").

### TC‑1.2: Check presence of core form elements
1. On the loaded page, confirm that the ticket options (radio buttons) are visible.
2. Verify that the personal information fields (first name, last name, address, email) are present.
3. Ensure date picker, gender radios, journey type radios and city fields are available.

---

## Phase 2 – Ticket Selection

### TC‑2.1: Select each available ticket option
1. For each radio button value (visa, return ticket, hotel booking, hotel+flight, cab), click the option.
2. Confirm only the chosen radio is selected and the others are not.
3. (Optional) Validate that the associated price label is correct.

### TC‑2.2: Ensure default ticket selection
1. Reload the page.
2. Verify no ticket option is pre‑selected or that the expected default is set.

---

## Phase 3 – Personal Information Entry

### TC‑3.1: Enter valid personal details
1. Select a ticket type to make the rest of form active.
2. Type a valid first name in the first name field.
3. Type a valid last name in the last name field.
4. Enter a legitimate address in the address field.
5. Input a properly formatted email address.
6. Verify each entry appears correctly and accepts input.

### TC‑3.2: Use date picker for birthday
1. Click the date field and choose a valid date.
2. Confirm the date appears in the field in the expected format.

### TC‑3.3: Choose gender
1. Click the “Male” radio button and verify selection.
2. Click the “Female” radio button and verify selection swaps correctly.

---

## Phase 4 – Travel Details & Preferences

### TC‑4.1: Select journey type
1. Click the “One Way” radio option and confirm.
2. Click the “Round Trip” option and verify it becomes selected.

### TC‑4.2: Populate location fields
1. Enter a valid "from" city.
2. Enter a valid "destination" city.
3. Provide a prefecture/state and postcode if present.
4. Confirm all text fields accept input and display the text.

---

## Phase 5 – Submission & Confirmation

### TC‑5.1: Submit completed form
1. After filling all required fields, click the Submit/Book button.
2. Wait for any success message or navigation to confirmation page.
3. Verify that a confirmation message (e.g. "Booking successful") or summary is displayed.

### TC‑5.2: Verify no errors on submission
1. Submit the form with all valid inputs.
2. Confirm no validation error messages appear.
3. Ensure the browser does not navigate to an error page.

---

*End of test plan*
