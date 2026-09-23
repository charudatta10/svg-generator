## How to add new SVG to the collection

### How it works ?

Templates live in `docs/templates/` as `.svg` files. The static app in `docs/index.html` fetches each template and fills in placeholders — plain `{text1}` / `{text2}` / `{width}` / `{height}` tokens via string replacement, or `{{ ... }}` expressions via a small in-browser evaluator. Everything renders locally; no server required.

### Placeholders

- **Plain tokens** — `{text1}`, `{text2}`, `{width}`, `{height}` are replaced with the raw field values (XML-escaped).
- **`{{ ... }}` expressions** — a safe mini-language run entirely in the browser. It supports:

  - arithmetic: `+ - * / ( )`, unary `+ / -`
  - strings: `'single'` or `"double"` quoted
  - comparisons: `== != < <= > >=` (yield `1`/`0`)
  - logic: `&& || !`
  - ternary: `cond ? a : b`
  - functions: `max(...)`, `min(...)`, `len(...)`
  - local variables: `{{# lw = max(len(left_text) * 8 + 20, 24); rw = ... }}` runs assignments and emits nothing, so later `{{lw}}` can reuse the value.

  Field values are XML-escaped automatically, so user text can never break out into markup.

### Field types

`FIELD_DEFS` supports `text`, `number`, `color`, `select` (with `options`), and `checkbox` inputs.

### Steps to follow :

1. Add your template as `docs/templates/your-name.svg`, using `{text1}`, `{text2}`, `{width}`, `{height}` (or `{{ ... }}` expressions) for dynamic values.
2. Register it in the `TEMPLATES` map at the top of `docs/index.html` — give it a label, the list of fields it needs, and default values.
3. If your template uses new parameter names, add matching field definitions to `FIELD_DEFS` in `docs/index.html`.
4. Done — it appears in the template dropdown on the static page.