# 🍽️ Return First 10 Restaurants - JET Complete at Home Coding Assignment

A professional, enterprise-grade full-stack application for discovering top-rated restaurants. Built with a focus on modularity, data resilience, and automated testing.

## 🚀 Quick Start: How to Run

### 1. Backend (FastAPI)
The backend manages data fetching, transformation, and caching.

1.  **Navigate to the backend folder**:
    ```bash
    cd backend
    ```
2.  **Create and activate a virtual environment**:
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```
3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
4.  **Run the server**:
    ```bash
    uvicorn main:JET_app --reload
    ```
    *The API will be available at `http://127.0.0.1:8000/`*

### 2. Frontend (React + Vite)
The frontend provides a premium, responsive UI with interactive maps and error handling.

1.  **Navigate to the frontend folder**:
    ```bash
    cd frontend
    ```
2.  **Install dependencies**:
    ```bash
    npm install
    ```
3.  **Run the development server**:
    ```bash
    npm run dev
    ```
    *The UI will be available at `http://localhost:5173/`*

---

## 🧪 Running Tests

### Backend Tests (Pytest)
Includes unit tests for transformers, service mocks, and API endpoints.
```bash
cd backend
.\venv\Scripts\python -m pytest tests/
```

### Frontend Tests (Vitest)
Includes component resilience tests and UI verification.
```bash
cd frontend
npm run test        # Terminal mode
npm run test:ui     # Interactive Dashboard mode
```

---

## 🧠 Key Assumptions & Decisions

1.  **Data Transformation Layer**: The raw Just Eat API provides overlapping data in fields like `cuisines` and `ethnicity`. I implemented a **Custom Transformer** that aggregates these into a high-quality "Specialties" list to ensure the user sees the most relevant information.
2.  **Map Integration**: Since no Google Maps API key was provided, I utilized the **Google Maps Embed API** in "Search/Embed" mode. This allows for persistent, visual location markers for every restaurant without requiring a paid billing key.
3.  **Resilience (Network & Data)**: I assumed that the external API might occasionally be slow or provide corrupted data. I implemented:
    - **In-Memory Caching**: To prevent redundant network calls.
    - **Fallback UI**: If a single restaurant's data is corrupted, only that specific card shows an error state, while the rest of the list remains functional.
4.  **Casing Sensitivity**: To handle Windows/Unix discrepancies, a `jsconfig.json` was added to force consistent path casing (`ARDA` vs `ArDA`), ensuring the Vitest runner remains stable.

---

## 🛠️ Data Coverage (Assignment Requirements)

I have ensured that all four mandatory data points are explicitly and clearly displayed:
1.  **Name**: Prominent title on every card.
2.  **Cuisines**: Grouped and styles with branded tags.
3.  **Rating**: Displayed as a clear numerical value (e.g., `4.5 / 5`).
4.  **Address**: Displayed with geographic icons for quick scannability.

---

## ✨ Future Improvements

If I had more time, I would implement the following:
-   **Dynamic Postcode Search**: Real-time input field to fetch restaurants for any UK postcode.
-   **Persistent Caching**: Replace the in-memory cache with **Redis** for production-level scalability.
-   **Enhanced Sorting**: Add filters for "Price Range," "Delivery Time," and "Distance from Postcode."
-   **E2E Testing**: Add **Playwright** tests to simulate a full user journey from landing page to map interaction.

---
*Created by Arda Guney - JET Coding Assignment*
