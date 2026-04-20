## Purpose

This repository is a minimal reproduction for a NiceGUI CSS parsing issue related to `@keyframes`.
It is intended to show that a component containing `@keyframes` can break the generated `<style>` output and prevent styles in following components from being applied.

## Reproduced Version

- NiceGUI `3.10.0`

## Reproduction Notes

Important: restart NiceGUI before opening each page.

Once a component is imported, its `<style>` remains in the running NiceGUI process.
Because of that, opening multiple pages in the same session can hide or contaminate the reproduction result.

## Pages

- `/ok`
  - No issue.
  - `PlainStyleComponent` is rendered normally, and its style is applied.

- `/issue_keyframe_css`
  - Reproduces the bug.
  - When a component containing `@keyframes` is imported, the generated CSS becomes malformed due to a brace mismatch.
  - As a result, the style of the following `PlainStyleComponent` is not applied.

- `/issue_keyframe_css_import_order_matters`
  - Shows that import order affects the generated CSS output.
  - Changing the import order changes where the `@keyframes` block appears in the final `<style>`.
  - This can make the breakage less obvious, even though the generated CSS is still malformed.
