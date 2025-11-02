# GitHub Pages Setup Instructions

This repository includes a GitHub Pages site with neobrutalism design that displays lottery data statistics.

## Enabling GitHub Pages

To enable GitHub Pages for this repository, follow these steps:

1. Go to your repository on GitHub
2. Click on **Settings** (top menu)
3. Click on **Pages** (left sidebar)
4. Under **Source**, select:
   - Source: **GitHub Actions**
5. Save the settings

## How It Works

- The workflow file `.github/workflows/deploy-pages.yml` automatically builds and deploys the site
- The workflow triggers on every push to the `main` branch
- The site content is in the `docs/` directory
- The page will be available at: `https://vietvudanh.github.io/vietlott-data/`

## Manual Deployment

You can also manually trigger the deployment:

1. Go to **Actions** tab in your repository
2. Select **Deploy GitHub Pages** workflow
3. Click **Run workflow**

## Design

The site features a **neobrutalism design** with:
- Bold black borders
- Vibrant colors (yellow, red, blue, green, purple, orange)
- Drop shadows for depth
- Responsive layout
- Clean, brutalist aesthetics

## Updating Content

To update the page content:
1. Edit `docs/index.html` for content changes
2. Edit `docs/styles.css` for styling changes
3. Commit and push to `main` branch
4. The workflow will automatically redeploy
