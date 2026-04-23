# CurvySnake

A smooth, curve-based Snake game built with Pygame. Control a snake that moves in continuous curves rather than on a grid.

## Website (Download Page)

This repo includes a simple **static HTML + CSS** website (no React/Node required).

- Website entrypoint: `index.html`
- Styles: `styles.css`
- Download link points to the GitHub file page.

## Requirements

- Python 3.x
- pygame

## Installation

```bash
pip install pygame
```

## How to Run

```bash
python "Group8 cse423 sping 2023 project.py"
```

## Run the website locally

Open `index.html` in a browser.

## Deploy to Vercel

1. Push this repo to GitHub.
2. In Vercel, click **New Project** and import the repo.
3. Keep **Root Directory** as the repo root.

Vercel will deploy the static site automatically.

## Gameplay

1. **Select Difficulty**: Choose 1 (Easy), 2 (Medium), or 3 (Hard) at startup
2. **Controls**:
   - `LEFT Arrow`: Rotate snake counterclockwise
   - `RIGHT Arrow`: Rotate snake clockwise
   - `SPACE`: Slow down
   - `UP Arrow`: Speed up
3. **Objective**: Collect targets to grow and increase your score
4. **Game Over**: Hitting the border ends the game

## Features

- Three difficulty levels with varying speeds and sizes
- Smooth curve-based movement
- Dynamic target spawning
- Score tracking
- Visual laser pointer showing direction