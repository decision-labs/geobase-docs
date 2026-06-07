# geobase-docs Conventions

This file defines conventions for how we structure and name docs pages in `apps/geobase-docs`.

## Navigation tabs and entry pages

1. Use the tab keys defined in `content/_meta.js` (and any nested `content/<section>/_meta.js`) as the source of truth for naming.
2. For a tab/section that has an entry ("index") page, name the MDX after the tab key (not `index.mdx`).
   - Example: if the tab key is `ai`, the entry page should be `content/ai/ai.mdx` (and not `content/ai/index.mdx`).
3. Avoid creating new `index.mdx` files under `content/**`. If you must rename an existing one, keep the tab key the same and update links as needed.

## File locations

1. Keep route-level structure aligned with the folder structure under `content/`.
2. If a page belongs under a tab/section, place it in the corresponding `content/<section>/...` directory.

## Meta configuration

1. Update `content/_meta.js` when you add/remove or rename top-level navigation tabs.
2. For nested sections, prefer `content/<section>/_meta.js` over trying to encode navigation structure inside a single page file.

