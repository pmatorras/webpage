# Personal Website

A simple, fast personal website built with HTML/CSS and hosted on GitHub Pages, used to showcase projects, interactive dashboards, and contact information.

[**Live site**](https://pablo.matorras.com/): <https://pablo.matorras.com/>

## Highlights
- Clean, responsive static pages with no backend dependencies.
- Embedded interactive dashboards via iframe (e.g., [MacroEconomics](https://github.com/pmatorras/MacroEconomics) Dash app).
- Portfolio of Data Science, NLP, and Financial Engineering projects.
- Academic profile (publications & talks).

## Project structure

### Core
- `index.html`: Homepage with bio, skills matrix, and featured projects.
- `assets/`: Styles (`css/`) and images (`img/`, including optimized WebP assets).

### Projects (`/projects/`)
- `financial-sentiment.html`: Multi-task LLM architecture details & benchmarks.
- `financial-ml.html`: Equity selection system methodology & results.
- `footai.html`: Football match prediction system.
- `macroeconomics.html`: Interactive Dash visualization wrapper.

### Research (`/research/`)
- `publications.html`: List of relevant physics & ML publications.
- `talks.html`: Conference presentations and talks.

## Local development
No build step required. Just open `index.html` in a browser or serve with a simple HTTP server.

## Deployment (GitHub Pages)
- Create your repository.
- Push changes to the default branch and enable Pages in Settings → Pages, serving from the repository root or `/docs`. 
- If using a custom domain, configure DNS (A/ALIAS or CNAME) and add a `CNAME` file in the repo.

## Technical Implementation
- **Dashboards:** Hosted externally (Render/Heroku) and embedded via responsive iframes.
- **Performance:** Assets optimized (WebP) to maintain high Lighthouse scores despite heavy iframes.

