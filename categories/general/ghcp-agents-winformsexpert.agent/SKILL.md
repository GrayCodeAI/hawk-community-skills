---
name: ghcp-agents-winformsexpert.agent
description: Support development of .NET (OOP) WinForms Designer compatible Apps.
license: MIT
tags:
- general
---

## WinForms Design Principles

### Core Rules

**Scaling and DPI:**
- Use adequate margins/padding; prefer TableLayoutPanel (TLP)/FlowLayoutPanel (FLP) over absolute positioning of controls.
- The layout cell-sizing approach priority for TLPs is:
  * Rows: AutoSize > Percent > Absolute
  * Columns: AutoSize > Percent > Absolute

- For newly added Forms/UserControls: Assume 96 DPI/100% for `AutoScaleMode` and scaling
- For existing Forms: Leave AutoScaleMode setting as-is, but take scaling for coordinate-related properties into account

- Be DarkMode-aware in .NET 9+ - Query current DarkMode status: `Application.IsDarkModeEnabled`
  * Note: In DarkMode, only the `SystemColors` values change automatically to the complementary color palette.

- Thus, owner-draw controls, custom content painting, and DataGridView theming/coloring need customizing with absolute color values.

### Layout Strategy

**Divide and conquer:**
- Use multiple or nested TLPs for logical sections - don't cram everything into one mega-grid.
- Main form uses either SplitContainer or an "outer" TLP with % or AutoSize-rows/cols for major sections.
- Each UI-section gets its own nested TLP or - in complex scenarios - a UserControl, which has been set up to handle the area details.

**Keep it simple:**
- Individual TLPs should be 2-4 columns max
- Use GroupBoxes with nested TLPs to ensure clear visual grouping.
- RadioButtons cluster rule: single-column, auto-size-cells TLP inside AutoGrow/AutoSize GroupBox.
- Large content area scrolling: Use nested panel controls with `AutoScroll`-enabled scrollable views.

**Sizing rules: TLP cell fundamentals**
- Columns:
  * AutoSize for caption columns with `Anchor = Left | Right`.
  * Percent for content columns, percentage distribution by good reasoning, `Anchor = Top | Bottom | Left | Right`. 
    Never dock cells, always anchor!
  * Avoid _Absolute_ column sizing mode, unless for unavoidable fixed-size content (icons, buttons).
- Rows:
  * AutoSize for rows with "single-line" character (typical entry fields, captions, checkboxes).
  * Percent for multi-line TextBoxes, rendering areas AND filling distance filler for remaining space to e.g., a bottom button row (OK|Cancel).
  * Avoid _Absolute_ row sizing mode even more.

- Margins matter: Set `Margin` on controls (min. default 3px). 
- Note: `Padding` does not have an effect in TLP cells.

### Common Layout Patterns

#### Single-line TextBox (2-column TLP)
**Most common data entry pattern:**
- Label column: AutoSize width
- TextBox column: 100% Percent width
- Label: `Anchor = Left | Right` (vertically centers with TextBox)
- TextBox: `Dock = Fill`, set `Margin` (e.g., 3px all sides)

#### Multi-line TextBox or Larger Custom Content - Option A (2-column TLP)
- Label in same row, `Anchor = Top | Left`
- TextBox: `Dock = Fill`, set `Margin`
- Row height: AutoSize or Percent to size the cell (cell sizes the TextBox)

#### Multi-line TextBox or Larger Custom Content - Option B (1-column TLP, separate rows)
- Label in dedicated row above TextBox
- Label: `Dock = Fill` or `Anchor = Left`
- TextBox in next row: `Dock = Fill`, set `Margin`
- TextBox row: AutoSize or Percent to size the cell

**Critical:** For multi-line TextBox, the TLP cell defines the size, not the TextBox's content.

### Container Sizing (CRITICAL - Prevents Clipping)

**For GroupBox/Panel inside TLP cells:**
- MUST set `AutoSize = true` and `AutoSizeMode = GrowOnly`
- Should `Dock = Fill` in their cell
- Parent TLP row should be AutoSize
- Content inside GroupBox/Panel should use nested TLP or FlowLayoutPanel

**Why:** Fixed-height containers clip content even when parent row is AutoSize. The container reports its fixed size, breaking the sizing chain.

### Modal Dialog Button Placement

**Pattern A - Bottom-right buttons (standard for OK/Cancel):**
- Place buttons in FlowLayoutPanel: `FlowDirection = RightToLeft`
- Keep additional Percentage Filler-Row between buttons and content.
- FLP goes in bottom row of main TLP
- Visual order of buttons: [OK] (left) [Cancel] (right)

**Pattern B - Top-right stacked buttons (wizards/browsers):**
- Place buttons in FlowLayoutPanel: `FlowDirection = TopDown`
- FLP in dedicated rightmost column of main TLP
- Column: AutoSize
- FLP: `Anchor = Top | Right`
- Order: [OK] above [Cancel]

**When to use:**
- Pattern A: Data entry dialogs, settings, confirmations
- Pattern B: Multi-step wizards, navigation-heavy dialogs

### Complex Layouts

- For complex layouts, consider creating dedicated UserControls for logical sections.
- Then: Nest those UserControls in (outer) TLPs of Form/UserControl, and use DataContext for data passing.
- One UserControl per TabPage keeps Designer code manageable for tabbed interfaces.

### Modal Dialogs

| Aspect | Rule |
|--------|------|
| Dialog buttons | Order -> Primary (OK): `AcceptButton`, `DialogResult = OK` / Secondary (Cancel): `CancelButton`, `DialogResult = Cancel` |
| Close strategy | `DialogResult` gets applied by DialogResult implicitly, no need for additional code |
| Validation | Perform on _Form_, not on Field scope. Never block focus-change with `CancelEventArgs.Cancel = true` |

Use `DataContext` property (.NET 8+) of Form to pass and return modal data objects.

### Layout Recipes

| Form Type | Structure |
|-----------|-----------|
| MainForm | MenuStrip, optional ToolStrip, content area, StatusStrip |
| Simple Entry Form | Data entry fields on largely left side, just a buttons column on right. Set meaningful Form `MinimumSize` for modals |
| Tabs | Only for distinct tasks. Keep minimal count, short tab labels |

### Accessibility

- CRITICAL: Set `AccessibleName` and `AccessibleDescription` on actionable controls
- Maintain logical control tab order via `TabIndex` (A11Y follows control addition order)
- Verify keyboard-only navigation, unambiguous mnemonics, and screen reader compatibility

### TreeView and ListView

| Control | Rules |
|---------|-------|
| TreeView | Must have visible, default-expanded root node |
| ListView | Prefer over DataGridView for small lists with fewer columns |
| Content setup | Generate in code, NOT in designer code-behind |
| ListView columns | Set to `-1` (size to longest content) or `-2` (size to header name) after populating |
| SplitContainer | Use for resizable panes with TreeView/ListView |

### DataGridView

- Prefer derived class with double buffering enabled
- Configure colors when in DarkMode!
- Large data: page/virtualize (`VirtualMode = True` with `CellValueNeeded`)

### Resources and Localization

- String literal constants for UI display NEED to be in resource files.
- When laying out Forms/UserControls, take into account that localized captions might have different string lengths. 
- Instead of using icon libraries, try rendering icons from the font "Segoe UI Symbol". 
- If an image is needed, write a helper class that renders symbols from the font in the desired size.

## Critical Reminders

| # | Rule |
|---|------|
| 1 | `InitializeComponent` code serves as serialization format - more like XML, not C# |
| 2 | Two contexts, two rule sets - designer code-behind vs regular code |
| 3 | Validate form/control names before generating code |
| 4 | Stick to coding style rules for `InitializeComponent` |
| 5 | Designer files never use NRT annotations |
| 6 | Modern C# features for regular code ONLY |
| 7 | Data binding: Treat ViewModels as DataSources, remember `Command` and `CommandParameter` properties |
