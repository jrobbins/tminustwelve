# TMinusTwelve Minimal Viable Product Requirements

This file specifies the functional requirements needed for an initial demo of this application.

## Feature: Application header

Every UI page will include a header with the following information:

- The left-justify product name spelled out as text and linked to the Launch list page.
- A right-justified area that contains one of two things:
    - When the user is signed out: a button allowing the user to sign in.
    - When the user is signed in: A menu labeled with the user's email address that opens to show an option to sign out.

## Feature: Left-hand navigation

Every UI page will include a navigation menu on the left-hand side that lists the following options:

- New launch: Navigates to the Launch creation page.
- All launches: Navigates to the Launch list page.

## Feature: Saving indicator

The submit button indicates that a submission is in progress:

- When the user presses the submit button, it immediately becomes disabled and its label changes to "Submitting…".
- After the submission has completed, the button can change back to normal, but the user typically will not see that because the UI will navigate to the next page.
