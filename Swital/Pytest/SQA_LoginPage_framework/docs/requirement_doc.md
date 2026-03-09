1️⃣ Requirement Document (SRS) – Login Functionality
Project Name

Login Module Testing

Application URL

https://practice.expandtesting.com/login

Module

User Authentication – Login

Objective

Allow registered users to securely log in to the system using valid credentials.

Actors

Registered User

Functional Requirements
FR1 – Login Page Access

User should be able to open the login page via URL.

FR2 – Username Input

User must enter username in the username field.

FR3 – Password Input

User must enter password in the password field.

FR4 – Login Button

User clicks Login button to submit credentials.

FR5 – Successful Login

If credentials are correct:

User is redirected to Secure Area page

Success message displayed:

"You logged into a secure area!"

Logout button visible.

FR6 – Invalid Username

If username is incorrect:

Error message shown

Invalid username.
FR7 – Invalid Password

If password is incorrect:

Error message shown

Invalid password.
FR8 – Session Handling

After login:

Session should remain active until logout.

Non-Functional Requirements
Security

Password should be masked.

Performance

Login response time < 3 seconds.

Usability

Clear error messages.

Compatibility

Application should work on:

Chrome

Firefox

Edge

Test Data

Valid Credentials:

Username: practice
Password: SuperSecretPassword!

Invalid Credentials:

Username: wrongUser
Password: WrongPassword