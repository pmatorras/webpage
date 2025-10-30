# Personal Website

A simple, fast personal website built with HTML/CSS and hosted on GitHub Pages, used to showcase projects, interactive dashboards, and contact information.

[**Live site**](htpps://pablo.matorras.com): <htpps://pablo.matorras.com>

## Highlights
- Clean, responsive static pages with no backend dependencies.
- Embedded interactive dashboards via iframe (e.g., [MacroEconomics](https://github.com/pmatorras/MacroEconomics) Dash app).
- Links to data-science and ML projects, CV, and contact.

## Project structure
- `index.html`: homepage with profile and links.
- `assets/css/`: styles and static assets.
- `publications.html`: List the relevant publications
- `talks.html`: List the talks given at conferences
- `macroeconomics.html`: Display  the [MacroEconomics](https://github.com/pmatorras/MacroEconomics) dashboard.
- `financial-ml.html`: Describe the [financial-ml](https://github.com/pmatorras/financial-ml) repository.

## Local development
No build step required. Just open `index.html` in a browser or serve with a simple HTTP server.

## Deployment (GitHub Pages)
- Create your repository.
- Push changes to the default branch and enable Pages in Settings → Pages, serving from the repository root or `/docs`. 
- If using a custom domain, configure DNS (A/ALIAS or CNAME) and add a `CNAME` file in the repo.

## Embedding a live dashboard
- Add an iframe pointing to the hosted app
