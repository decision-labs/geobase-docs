![Geobase Docs](public/geobase-logo.svg)

<p align="center">
  <a href="https://vercel.com/sabmans-projects/geobase-docs" target="_blank">
    <img alt="Vercel Status" src="https://therealsujitk-vercel-badge.vercel.app/?app=geobase-docs" />
  </a>
</p>

# Geobase Docs

Docs are hosted at: https://docs.geobase.app

## Community

- Discord: [geobase.app/discord](https://geobase.app/discord)
- YouTube: [@geobaseapp](https://www.youtube.com/@geobaseapp)
- X: [@geobaseapp](https://x.com/geobaseapp)
- Bluesky: [@geobaseapp](https://bsky.app/geobaseapp)

## Local Development

1. Install deps: `pnpm i`
2. Start dev server: `pnpm dev` (visit http://localhost:3000)

## Production

- Build: `pnpm build`
- Start: `pnpm start`

## Prerequisites

- Node.js 18.18+ or 20+
- pnpm 8+
- Recommended: enable Corepack to manage pnpm versions

```bash
corepack enable
```

## Project structure

- `pages/`: MDX docs content (e.g., `pages/guides/...`). Sidebar order and labels are controlled via `_meta.js` files inside subfolders.
- `components/`: Reusable MDX/React components (e.g., `youtube-embed.tsx`, `geobase-logo.tsx`).
- `public/`: Static assets served from the site root.
- `theme.config.tsx`: Site-wide configuration (title, logo, repo links, colors, footer, copy-code button).
- `next.config.mjs`: Nextra setup for the docs theme.

## Adding or editing docs

1. Create a `.mdx` file under `pages/...`.
2. Update the nearest `pages/**/_meta.js` to include the new page in the sidebar.
3. Place images in `public/` or alongside the MDX in an `images/` folder; reference relatively.
4. Prefer absolute internal links (e.g., `/guides/...`) for stable routing.
5. You can import and use components from `components/` in MDX.

## Scripts

- `pnpm dev`: Start Next.js in dev mode at http://localhost:3000
- `pnpm build`: Build the production bundle
- `pnpm start`: Start the production server

## Deployment

- Deployed on Vercel. Pushes to `main` trigger production deploys. Pull requests get preview URLs.
- No environment variables are required for local dev or deploy.

## Contributing

- Issues and PRs are welcome in this repository.
- Suggested checklist for new/updated pages:
  - Content compiles locally (`pnpm dev`) with no console errors
  - Sidebar entry added/updated in the relevant `_meta.js`
  - Internal links are absolute; images render correctly
  - Reuse shared components from `components/` where helpful

## Troubleshooting

- Version mismatches: ensure Node and pnpm meet the prerequisites; consider `nvm use` if you maintain an `.nvmrc`.
- Stale build artifacts: delete `.next/` and restart the dev server.
- MDX import errors: check import paths and ensure components exist in `components/`.
