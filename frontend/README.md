# Just Eat Takeaway - Coding Assignment
## Restaurant Discovery Application

A modern, responsive, and modular React application for discovering restaurants, built as part of the JET candidate assessment.

---

## 🚀 Key Features

- **Dynamic Data Fetching**: Retrieves real restaurant data from a Python FastAPI backend.
- **Editorial Design**: A premium, branded UI using the JET #FF8000 color palette.
- **Responsive Layout**: Side-by-side restaurant details and MiniMaps that adapt to mobile, tablet, and desktop.
- **Industrial Architecture**: A highly modular codebase following the "Service-Hook-Component" pattern.
- **UX Excellence**: Includes professional loading states and graceful error handling.

## 🏗️ Technical Architecture

This project has been restructured for maximum modularity:

- **`/src/api`**: Pure network service layer.
- **`/src/hooks`**: Encapsulated state and data fetching logic.
- **`/src/components`**: Atomic UI components separated by responsibility.
- **`/src/assets`**: Centralized brand assets.

## 🛠️ Setup & Running

1. **Backend**: Ensure the FastAPI server is running at `http://localhost:8000`.
2. **Frontend**:
   ```bash
   npm install
   npm run dev
   ```
3. **View**: Open `http://localhost:5173` in your browser.

---

*Built with React, Vite, and Tailwind CSS v4.*
