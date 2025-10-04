
### Suggested README.md

# Personal Website

A simple, fast personal website built with HTML/CSS and hosted on GitHub Pages, used to showcase projects, interactive dashboards, and contact information.

## Live site
- <htpp://pablo.matorras.com>

## Highlights
- Clean, responsive static pages with no backend dependencies.
- Embedded interactive dashboards via iframe (e.g., [MacroEconomics](https://github.com/pmatorras/MacroEconomics) Dash app).
- Links to data-science and ML projects, CV, and contact.

## Project structure
- `index.html`: homepage with profile and links.
- `assets/` or `css/`: styles and static assets.
- `publications.html`: List the relevant publications
- `publications.html`: List the talks given at conferences
- `macroeconomics.html`: Display  the [MacroEconomics](https://github.com/pmatorras/MacroEconomics) dashboard.

## Local development
No build step required—open `index.html` in a browser or serve with a simple HTTP server.

## Deployment (GitHub Pages)
- Push changes to the default branch and enable Pages in Settings → Pages, serving from the repository root or `/docs`. 
- If using a custom domain, configure DNS (A/ALIAS or CNAME) and add a `CNAME` file in the repo.

## Embedding a live dashboard
Add an iframe pointing to the hosted app: