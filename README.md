# CurvySnake

A smooth, curve-based Snake game built with Pygame. Control a snake that moves in continuous curves rather than on a grid.

## Website (Download Page)

This repo includes a simple MERN-style site:

- **React (Vite)** frontend in `client/`
- **Node/Express** API in `api/` (optional Mongo logging via `MONGODB_URI`)
- The download button pulls the `.py` file directly from GitHub (raw URL)

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

Frontend:

```bash
cd client
npm install
npm run dev
```

API (optional, for `/api/download` + `/api/health`):

```bash
cd api
npm install
npm run dev
```

Then open `http://localhost:5173`.

## Deploy to Vercel

1. Push this repo to GitHub.
2. In Vercel, click **New Project** and import the repo.
3. Keep **Root Directory** as the repo root (this is required for `vercel.json` to wire both frontend + API).
4. (Optional) Add an environment variable:
   - `MONGODB_URI` = your MongoDB connection string (enables download logging)

Vercel will build the React app and deploy the API automatically.

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