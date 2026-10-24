---

version: "alpha" name: "TMinusTwelve" description: "Simplified design system for TMinusTwelve."

colors: primary: "\#366597" primary-center: "\#4580c0" primary-medium: "\#85b4df" primary-light: "\#bdd6ed" accent-blue: "\#5588ff" surface: "\#ffffff" surface-subtle: "\#eeeeee" on-surface: "\#222222" on-surface-secondary: "\#444444" on-primary: "\#ffffff" gray-1: "\#e6e6e6" gray-2: "\#a9a9a9" gray-3: "\#797979" gray-4: "\#515151" border: "\#dddddd" border-input: "\#d4d4d4" error: "\#ff0000" error-surface: "\#ffedf5"

typography: h1: fontFamily: "system-ui, sans-serif" fontSize: "30px" fontWeight: 300 h2: fontFamily: "system-ui, sans-serif" fontSize: "25px" fontWeight: 300 h3: fontFamily: "system-ui, sans-serif" fontSize: "20px" fontWeight: 300 body: fontFamily: "system-ui, sans-serif" fontSize: "14px" fontWeight: 400 lineHeight: "1.4" button: fontFamily: "system-ui, sans-serif" fontSize: "10pt" fontWeight: 700 code: fontFamily: "monospace" fontSize: "14px" fontWeight: 400

rounded: default: "3px" sm: "4px" md: "8px" pill: "12px"

spacing: xs: "4px" sm: "8px" md: "16px" xl: "80px"

components: card: backgroundColor: "{colors.surface}" textColor: "{colors.on-surface}" borderColor: "{colors.border}" rounded: "{rounded.default}" padding: "{spacing.md}" button-primary: backgroundColor: "{colors.primary}" textColor: "{colors.on-primary}" rounded: "{rounded.sm}" padding: "4px 16px" typography: "{typography.button}" button-disabled: backgroundColor: "{colors.gray-4}" textColor: "{colors.on-primary}" rounded: "{rounded.sm}" padding: "4px 16px" input: backgroundColor: "{colors.surface}" textColor: "{colors.on-surface}" borderColor: "{colors.border-input}" rounded: "{rounded.sm}" padding: "7px" input-invalid: backgroundColor: "{colors.error-surface}" textColor: "{colors.on-surface}" borderColor: "{colors.error}" rounded: "{rounded.sm}" padding: "7px"

---

&nbsp;

## Overview

TMinusTwelve (`TMinusTwelve.com`) uses a clean, utility-first interface designed for reading and managing high-density project metadata, launch stages, and review discussions.&nbsp;

## Colors

The color palette centers on blues paired with high-contrast neutral grays on white cards:

- **Brand Blues**: `--tm12-color-dark` (`#366597`) is the primary brand accent used for icons, theme metadata, and primary emphasis, supported by `--tm12-color-center` ( `#4580c0`), `--tm12-color-medium` (`#85b4df`), and `--tm12-color-light` (`#bdd6ed`).  
- **Surfaces & Text**: Cards and form panels sit on `--card-background` (`#ffffff`) with subtle secondary regions in `--light-grey` (`#eeeeee`). Primary text uses `--default-fon t-color` (`#222222`) and secondary/navigation text uses `--nav-link-color` (`#444444`).  
- **Neutral Scale**: Four stepped grays (`--gray-1: #e6e6e6` through `--gray-4: #515151`) handle dividers, disabled button backgrounds, and interactive hover borders.  
- **Validation & Status**: Form errors use `--error-border-color` (`#ff0000`) and `--invalid-color` (`rgba(255, 0, 0, 0.75)`) over a soft pink invalid input fill (`#ffedf5`).

## Typography

- **Font Stack**: Inherits the system sans-serif stack (`14px system-ui, sans-serif`) for body and form controls (`--form-element-font`), with `monospace` for `<code>` blocks.  
- **Headings**: All headings (`h1`–`h4`) use a light weight (`font-weight: 300`) to keep dense dashboards visually calm:  
  - `h1`: `30px` (`24px` at `<= 700px`)  
  - `h2`: `25px` (`20px` at `<= 700px`)  
  - `h3`: `20px` (`15px` at `<= 700px`)  
- **Readable Copy**: `.description` blocks and sidebar navigation links use `line-height: 1.4`.

## Layout

Spacing and containment tokens follow an `8px` base grid:

- **Content Width**: Primary views and `#subheader` are constrained to `--max-content-width` (`860px`). Form containers (`.stage_form`, `.flat_form`, `#metadata`) expand up to  `67em` (`1em` internal padding), with the primary field column taking `60%` (`max-width: 35em`).  
- **Spacing Scale**:  
  - `--content-padding-quarter` (`4px`): Tight gaps in `<details>` and `.roadmap-sidebar nav`.  
  - `--content-padding-half` (`8px`): Compact vertical cell padding, icon spacing, and accordion margins.  
  - `--content-padding` (`16px`): Default padding and margin across cards, tables, and sections (`--content-padding-negative: -16px` for edge-bleed).  
- **Flex Utilities**: Use `.hbox` (row) and `.vbox` (column) with `.spacer` (`flex-grow: 1`), or `.layout` with `.wrap`, `.center`, `.center-center`, and `.vertical`.  
- **Responsive Breakpoint**: At `max-width: 700px`, headings scale down and non-essential `#subheader` controls collapse.

## Elevation & Depth

TMinusTwelve favors flat, bordered surfaces with subtle elevation:

- **Cards & Form Panels**: Elevate from the page canvas using a `1px` border (`--card-border: 1px solid #ddd`) and a soft directional drop shadow (`--card-box-shadow: rgba(0, 0,  0, 0.067) 1px 1px 4px`).  
- **Toolbars & Bars**: Use `--bar-shadow-color` (`rgba(0, 0, 0, 0.065)`) and `--bar-border-color` (`#d4d4d4`).  
- **Focus & Popups**: Focused `.datalist-input-wrapper` elements in `forms-css.js` display a `0 0 0 3px #0ea5e966` focus ring; roadmap `.popup-content` overlays use a `2px solid  #888` border.

## Shapes

Corner radii are intentionally subtle to preserve a crisp, tabular layout:

- **Cards & Milestones**: Use `--default-border-radius` (`3px`).  
- **Buttons, Tables, Inputs & Accordions**: Use `4px` (`--border-radius`, `--button-border-radius`, `--accordion-border-radius`, and `.datalist-input`).  
- **Popups & Badges**: Roadmap popups and `.experiment` tags use `8px` radius, while `.usage-tag` badges in `forms-css.js` use `12px` pill corners.

## Components

- **Buttons**: `4px 16px` padding, `10pt` font size, `white-space: nowrap`, and `--gray-4` (`#515151`) border on hover. `.primary` buttons and `input[type="sub mit"]` use bold white text on primary fill (`--gray-4` when `:disabled`); `.button.secondary` uses an outlined border with `--content-padding` margin.  
- **Data Tables**: `100%` width with `--default-border`, `4px` corner radius, and `--content-padding-half` (`8px`) by `--content-padding` (`16 px`) cell padding.  
- **Forms & Fields**: `form-field` renders as a `table-row-group`. Text inputs and textareas use `7px` padding and `1px solid var(--bar-border-color)`  (`#d4d4d4`).&nbsp;  
- **Accordions & Dialogs**: `sl-details::part(header)` uses `20px` light font (`font-weight: 300`), `4px 8px` padding, and `--accordion-background`. `sl-skelet on` uses `--color: #eee` and `--sheen-color: #ccc`.

## Do's and Don'ts

- **Do** use a shared CSS file for all theme details.  Individual templates or components may use CSS only for layout, padding, and visual details that must be unique to that template or component.  
- **Do** use the `--content-padding*` scale (`4px`, `8px`, `16px`) and `--max-content-width` (`860px`) for layout consistency.  
- **Do** use `var(--card-background)`, `var(--card-border)`, and `var(--card-box-shadow)` for surface containers.  
- **Don't** use legacy Sass syntax (such as `$tm12-color-dark` or `$invalid-color` found in older rules of `forms-css.js`); always use standard CSS `var(--...)` custom properties.  
- **Don't** introduce new hardcoded gray hex values when `--light-grey` (`#eee`), `--bar-border-color` (`#d4d4d4`), or `--gray-4` (`#515151`) fit the semantic role.

