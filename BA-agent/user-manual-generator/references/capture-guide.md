# UI Capture Guide

Capture enough evidence for a user to recognize the screen and complete real tasks.

## Desktop And Web

Use Playwright when the app can run in a browser or Electron automation is available.

Recommended viewport:

- Desktop/web: `1440x900`.
- Narrow web checks: `390x844` when the manual includes responsive behavior.

Capture these states when present:

- Main list/dashboard.
- Search and advanced filters.
- Create/edit/detail forms.
- Long dialogs at top and after scrolling.
- Confirmation dialogs.
- Row action menus.
- Empty, loading, validation, and error states.
- Approval/rejection flows.
- Role-specific views.

Close overlays with Escape or a visible cancel/close action before changing pages.

Use stable names:

```text
static/img/screenshots/<module>/<module>-01-overview.png
static/img/screenshots/<module>/<module>-02-filter.png
static/img/screenshots/<module>/<module>-03-create-form.png
static/img/screenshots/<module>/<module>-04-create-form-scroll.png
static/img/screenshots/<module>/<module>-05-actions.png
```

## Mobile

If the source is a PDF or screenshot bundle, extract images at high resolution and crop only empty margins. Keep role prefixes when role-specific:

```text
emp-checkin-01-home.png
mgr-approval-01-list.png
admin-user-01-form.png
```

Do not crop away device UI if it helps the user identify context.

## Exploration Notes

While exploring, keep a small evidence log:

```markdown
| Module | Path | Screenshot | Verified actions | Roles checked | Open questions |
| --- | --- | --- | --- | --- | --- |
```

This log prevents the final manual from quietly mixing verified facts with guesses.
