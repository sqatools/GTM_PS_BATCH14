# Automation Test Plan for Automation Practice Page

## Website Under Test
- URL: https://sqatools.in/automation-practice-page/
- Purpose: Validate core UI interactions on the automation practice page using the existing Selenium-based pytest framework.

## 1. Framework Code Structure Analysis

The current automation framework in this workspace is organized as follows:

- Base layer
  - [base/selenium_base.py](../base/selenium_base.py) : Contains reusable Selenium actions such as finding elements, clicking, typing, dropdown selection, file upload, and screenshots.

- Page object layer
  - [page_objects/practice_page/practice_page.py](../page_objects/practice_page/practice_page.py) : Encapsulates page-specific methods like launching the URL, entering user details, selecting radio buttons, checkboxes, dropdown values, and uploading a file.
  - [page_objects/practice_page/practice_page_locators.py](../page_objects/practice_page/practice_page_locators.py) : Stores element locators for the practice page.
  - [page_objects/practice_page/practice_page_data.py](../page_objects/practice_page/practice_page_data.py) : Stores test data such as URL, username, password, address, and selected values.

- Test layer
  - [tests/practice_test/test_practice_page.py](../tests/practice_test/test_practice_page.py) : Contains the main UI test case for entering form details and verifying selections.
  - [tests/conftest.py](../tests/conftest.py) : Provides the browser fixture and sets up the WebDriver.

- Supporting folders
  - logs/ : Stores screenshots and logs generated during test execution.

## 2. Test Strategy

### Scope
This plan focuses on positive test scenarios for the main UI elements on the practice page.

### Tools and Approach
- Python
- pytest
- Selenium WebDriver
- Page Object Model (POM)

### Test Data
- Username: John
- Password: admin@1234
- Address: Mumbai, Bandra
- Gender: Male
- Country: India
- Checkbox: Java

## 3. Positive Test Cases (5 Phases)

### Phase 1: Page Load and Basic Validation

#### TC-01: Open the page successfully
- Objective: Verify the automation practice page loads correctly.
- Steps:
  1. Launch the browser.
  2. Navigate to https://sqatools.in/automation-practice-page/.
  3. Wait for the page to load.
  4. Verify the page title contains "Automation Practice Page".
  5. Verify the main heading is visible.
- Expected Result:
  - The page opens successfully.
  - The title and heading are displayed correctly.

#### TC-02: Verify core input fields are visible
- Objective: Confirm the form fields are present and ready for input.
- Steps:
  1. Open the page.
  2. Verify the username field is visible.
  3. Verify the password field is visible.
  4. Verify the address field is visible.
- Expected Result:
  - All three input fields are displayed and enabled.

#### TC-03: Verify navigation links are present
- Objective: Confirm key page links are available.
- Steps:
  1. Open the page.
  2. Verify the "Dummy Page" link is visible.
  3. Verify the "Login Page" link is visible.
- Expected Result:
  - Both navigation links appear on the page.

### Phase 2: Form Entry and Selection

#### TC-04: Enter valid user details
- Objective: Validate that user information can be entered into the text fields.
- Steps:
  1. Open the page.
  2. Enter "John" in the username field.
  3. Enter "admin@1234" in the password field.
  4. Enter "Mumbai, Bandra" in the address field.
  5. Verify the entered values match the typed values.
- Expected Result:
  - All values are entered successfully and stored correctly in the fields.

#### TC-05: Select a radio button
- Objective: Verify the male radio button can be selected successfully.
- Steps:
  1. Open the page.
  2. Click the "Male" radio button.
  3. Verify it becomes selected.
- Expected Result:
  - The male radio button is selected.

#### TC-06: Select a checkbox
- Objective: Verify a checkbox can be selected successfully.
- Steps:
  1. Open the page.
  2. Click the "Java" checkbox.
  3. Verify it becomes selected.
- Expected Result:
  - The Java checkbox is selected.

#### TC-07: Select a value from the dropdown
- Objective: Verify a country can be chosen from the dropdown list.
- Steps:
  1. Open the page.
  2. Click the country dropdown.
  3. Select "India".
  4. Verify "India" is displayed as the selected value.
- Expected Result:
  - India is selected from the dropdown.

### Phase 3: Buttons and Alerts

#### TC-08: Click a normal button
- Objective: Verify a standard button can be clicked without errors.
- Steps:
  1. Open the page.
  2. Click the "Normal Button".
- Expected Result:
  - The button responds to the click without any error.

#### TC-09: Accept a simple alert
- Objective: Validate that the simple alert can be handled successfully.
- Steps:
  1. Open the page.
  2. Click the "Simple Alert" button.
  3. Accept the alert.
- Expected Result:
  - The alert is displayed and accepted successfully.

#### TC-10: Accept a confirmation alert
- Objective: Validate that the confirmation alert can be handled successfully.
- Steps:
  1. Open the page.
  2. Click the "Confirm Alert" button.
  3. Click "OK" on the alert.
- Expected Result:
  - The confirmation alert is displayed and accepted successfully.

#### TC-11: Enter text in a prompt alert
- Objective: Verify prompt alert handling with valid input.
- Steps:
  1. Open the page.
  2. Click the "Prompt Alert" button.
  3. Enter a sample text such as "Automation".
  4. Accept the prompt.
- Expected Result:
  - The prompt accepts the entered value and closes correctly.

### Phase 4: File Upload, Links, Date, and Table Validation

#### TC-12: Upload a valid file
- Objective: Verify that a file can be attached through the file input.
- Steps:
  1. Open the page.
  2. Create or choose a small text file for upload.
  3. Click the "Choose File" button.
  4. Select the file.
- Expected Result:
  - The file is selected and attached successfully.

#### TC-13: Enter date and time values
- Objective: Validate that date and time fields accept input correctly.
- Steps:
  1. Open the page.
  2. Locate the date field.
  3. Enter a valid date.
  4. Enter a valid time value.
- Expected Result:
  - The date and time are entered without errors.

#### TC-14: Verify links navigate correctly
- Objective: Confirm the page links open the expected destinations.
- Steps:
  1. Open the page.
  2. Click the "Open Google" link.
  3. Verify the new tab or window opens.
  4. Return to the page.
  5. Click the "Go to Bottom" link.
  6. Verify the page scrolls to the bottom section.
- Expected Result:
  - Both links behave as expected and navigate correctly.

#### TC-15: Validate the web table content
- Objective: Confirm the table displays the expected records.
- Steps:
  1. Open the page.
  2. Locate the web table.
  3. Verify the headers are present: ID, Name, Role.
  4. Verify the expected rows are visible.
- Expected Result:
  - The table content matches the expected values.

### Phase 5: Advanced UI Interactions

#### TC-16: Perform drag and drop
- Objective: Verify the drag-and-drop interaction works correctly.
- Steps:
  1. Open the page.
  2. Drag the "Drag Me" element.
  3. Drop it onto the "Drop Here" area.
- Expected Result:
  - The element is successfully dropped into the target area.

#### TC-17: Perform keyboard actions
- Objective: Validate keyboard interaction on the page.
- Steps:
  1. Open the page.
  2. Click the keyboard input field.
  3. Press a few keys.
  4. Verify the typed characters appear.
- Expected Result:
  - Keyboard input is accepted successfully.

#### TC-18: Interact with nested shadow DOM elements
- Objective: Verify shadow DOM elements can be accessed and interacted with.
- Steps:
  1. Open the page.
  2. Locate the shadow DOM section.
  3. Enter text into the nested shadow input.
  4. Click the shadow button.
- Expected Result:
  - The nested shadow DOM elements are accessible and interactable.

#### TC-19: Submit a comment form with valid data
- Objective: Validate the comment form accepts valid input.
- Steps:
  1. Open the page.
  2. Enter a comment in the comment field.
  3. Enter a name in the name field.
  4. Enter a valid email address.
  5. Enter a website value.
  6. Click the "Post Comment" button.
- Expected Result:
  - The form accepts the data and no validation error is displayed.

## 4. Recommended Test Execution Order
1. Phase 1: Basic page validation
2. Phase 2: Form data entry and selections
3. Phase 3: Alerts and button actions
4. Phase 4: File upload, links, table, and input fields
5. Phase 5: Advanced UI interactions

## 5. Notes
- The current framework already supports the core Selenium actions needed for these tests.
- Additional locators may be required for some advanced sections like alerts, drag-and-drop, and shadow DOM.
- Screenshots and logs are automatically captured in the logs folder during execution.
