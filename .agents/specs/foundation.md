# TMinusTwelve Foundational Requirements

This file specifies the most essential functional requirements for this application.

## Feature: Anonymous access

The application is available to users who visit the site without signing in.  

- HTTPS requests without authentication cookies shall be treated as coming from anonymous users.
- Anonymous users shall never be offered any UI elements that allow them to update any data in the application's database.  
- Anonymous users shall never be shown application data that is marked as confidential or private.

## Feature: Launch objects are the central business object type

The application centers around Launch objects and treats most related objects as secondary.  

- Signed-in users shall be able to create a `Launch`.
- Any user shall be able to view the Launch list page.
- Launch list page shall appear on the site home page.
- `Stage` and `Gate` and `Vote` objects are only shown on the detail page for a given `Launch`.

## Feature: Form structure

Any form that asks the user to enter field values should be organized as a table with room for field-level help.  

- Any data entry form shall be presented as a table with one row per form field.
- The first column of the form shall present the field name.
- The second column of the form field shall offer an appropriate editing widget.
- The third field shall present field-level on-line help to explain the purpose of that field and its validation requirements in human-understandable terms.
- Below the bottom of the form there shall be a button to submit changes.

## Feature: Field display lists

Any page or part of a page that displays a list of field values shall use an HTML description list with `<dl>`, `<dt>`, and `<dd>` elements.

- The name of the field shall be displayed in the `<dt>` element.
- The value of the field shall be appropriately formatted inside the `<dd>` element.
- If the field has no value, the string "No information provided yet" shall be shown in italics.
- If the field holds a URL, it shall be rendered as a clickable link that opens a new tab.
- If the field holds a multi-line text value, it shall be rendered using `white-space: pre-wrap`.


## Feature: Launch objects creation page

A signed-in user may use a Launch creation form to create a `Launch` object.  

- Signed-in users shall be able to view and use this page.
- The launch creation page shall consist of a single form that requests only required fields of the `Launch` object that are not computed by the system.
- Submitting this form creates a `Launch` object.
- After the `Launch` is created, the UI navigates to the Launch detail page for that `Launch`.

## Feature: Launch list page

Any user may view a list of `Launch` objects that have been created.  

- All users shall be able to view this page.
- The main content of the page is a table that lists `Launch` objects, one per row.
- The main content of each row shall be the name of a single `Launch` that is linked to the Launch detail page for that `Launch`.

## Feature: Launch detail page

Any user may view a list of fields on a single `Launch` object.  

- All users shall be able to view this page.
- The URL of this page specifies the ID of one `Launch` object.
- The main content of the page is a field list for the fields of the specified `Launch` object.
