# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]

### Added

- Shields-style badge templates (`shields-badge.svg` two-color and `flat-badge.svg` single-color) matching the classic shields.io design.
- Shape selector (pill / rounded / square), outline toggle, and outline color parameters.
- Expression engine now supports strings, comparisons (`==`, `!=`, `<`, `>`, ...), logical operators, ternaries, `max`/`min`/`len` functions, and local-variable definition blocks `{{# x = ...; y = ... }}`.
- "Copy Markdown" now copies an inline data-URI badge instead of raw SVG.

### Fixed

- `classic-badge.svg` no longer emits invalid CSS/SVG (removed broken `0.8 * {width}` expressions).
- `social_badge.svg` text is now centered for any size.

### Removed

- Empty `archives.zip` placeholder file.
- Legacy Python/Flask `.gitignore` rules that no longer apply to the static site.

## [v0.1.0] - 2026-08-14

### Added

- Initial static GitHub Pages app with banner, badge, and social badge SVG templates.