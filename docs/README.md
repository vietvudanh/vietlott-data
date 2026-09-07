# GitHub Pages Setup Instructions

This repository includes a GitHub Pages site with a modern design inspired by Meta's Astryx design system that displays lottery data statistics.

## Keeping Data Up to Date

The data statistics displayed on the GitHub Pages site are automatically synchronized with the data in the `data/` folder using the `render_docs.py` script:

```bash
python src/render_docs.py
# or using the CLI command:
vietlott-render-docs
```

This script should be run after updating the data to ensure the GitHub Pages site displays current information.

## Enabling GitHub Pages

To enable GitHub Pages for this repository, follow these steps:

1. Go to your repository on GitHub
2. Click on **Settings** (top menu)
3. Click on **Pages** (left sidebar)
4. Under **Source**, select:
   - Source: **GitHub Actions**
5. Save the settings

## How It Works

- The workflow `.github/workflows/deploy-pages.yml` builds and deploys the static documentation site
- It runs on a daily schedule and can be triggered via workflow dispatch
- Site content is located in the `docs/` directory
- Published URL: `https://vietvudanh.github.io/vietlott-data/`

## Manual Deployment

You can also manually trigger the deployment:

1. Go to **Actions** tab in your repository
2. Select **Deploy GitHub Pages** workflow
3. Click **Run workflow**

## Design

The site features a modern design system inspired by **Astryx** (Meta Design System):
- Clean typography using Figtree and JetBrains Mono
- Light & dark mode with smooth theme transitions
- Glassmorphic sticky top navigation with language switcher
- Interactive component cards with live status indicators and categorical color tokens
- Refined tables and macOS-styled terminal code blocks
- Fully responsive layout without any npm dependencies

## Updating Content

To update the page content:
1. Edit `docs/index.html` for content changes
2. Edit `docs/styles.css` for styling changes
3. Commit and push to `main` branch
4. The workflow will automatically redeploy
