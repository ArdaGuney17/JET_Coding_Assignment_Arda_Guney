# 🍽️ Return First 10 Restaurants - JET Complete at Home Coding Assignment

My solution to the JET Complete at Home Coding Assignment. Returns the first 10 restaurants for a given postcode with their requested data: name, cuisines, rating, and address.

---

## 🚀 Quick Start: How to Run

### 0. Clone and Navigate
First, prepare a folder on your local machine and clone the repository:

1. **Create a folder for the project**:
   ```bash
   # Example for Desktop
   cd Desktop
   mkdir JET_Project
   cd JET_Project
   ```
2. **Clone the Repository to the folder you created**:
   ```bash
    git clone https://github.com/ArdaGuney17/JET_Coding_Assignment_Arda_Guney.git
    ```

3. **Go to the project folder**:
   ```bash
   cd JET_Coding_Assignment_Arda_Guney
   ```

### 1. Backend (FastAPI)
Lets start by setting up the backend:

1.  **Navigate to the backend folder when u are still in the project folder**:
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
**Important:** Keep the backend terminal running. Open a **new, second terminal** window for these steps.

1.  **Navigate to your clone location**:
    First, `cd` into the same folder where you originally ran the `git clone` command (e.g., Desktop, Downloads, etc.).
    
2.  **Enter the project and frontend folders**:
    ```bash
    cd JET_Coding_Assignment_Arda_Guney/frontend
    ```
3.  **Install dependencies**:
    ```bash
    npm install
    ```
4.  **Run the development server**:
    ```bash
    npm run dev
    ```
    *The UI will be available at `http://localhost:5173/`*

---

## 🧪 Quality Assurance & Testing Strategy

A rigorous testing strategy is implemented across both the backend and frontend to ensure data integrity, component resilience, and API reliability. This demonstrates my strong focus on delivering production-ready, high-quality software and verifying all business logic through unit tests.

### Backend Tests (Pytest)
The backend test suite heavily focuses on unit testing the core business and transformation logic.
- **Transformer Tests**: Ensures raw API data is strictly validated and accurately converted into the Pydantic models. Unit tests heavily cover edge cases, missing fields, and taxonomy normalization without relying on live API data.
- **Service Mocks**: Simulates various network responses (e.g., successful API calls, HTTP errors) to verify the orchestrator's resilience and caching mechanisms.
- **API Endpoints**: Validates the REST schema, proper error propagation, and correct HTTP status codes.

```bash
cd backend                                # first go to the backend folder if you are not already there
.\venv\Scripts\python -m pytest tests/    # run the tests
```

### Frontend Tests (Vitest)
The frontend implements component-level unit testing to verify the UI's resilience against varied data states.
- **Component Resilience**: Validates that components render correctly even with partial or missing data, ensuring graceful degradation.
- **UI Verification**: Tests the dynamic rendering logic, loading states, and error boundaries.

```bash
cd frontend         # first go to the frontend folder if you are not already there
npm run test        # run the tests in Terminal mode
npm run test:ui     # run the tests in Interactive Dashboard mode
```

---

## 🏗️ Design & Architecture

The application follows a **decoupled, two-tier architecture**: a Python backend that owns all data-fetching and transformation logic, and a React frontend that is purely responsible for rendering. The two communicate over a single REST endpoint, keeping each side independently testable and replaceable.

---

### Backend — FastAPI (Python)

#### App Factory Pattern
The application is bootstrapped via a `create_app()` factory function (`setup/startup.py`) instead of a bare module-level FastAPI instance. This decouples middleware registration, router mounting, and configuration from the entry point (`main.py`), making the app easy to test in isolation and straightforward to extend.

#### Layered Service Pipeline
All business logic is separated into three single-responsibility classes inside the `services/` package:

| Layer | File | Responsibility |
|---|---|---|
| **Fetcher** | `fetcher.py` | Makes the raw HTTP call to the Just Eat public API and returns the unprocessed JSON payload. |
| **Transformer** | `transformer.py` | Converts raw dicts into typed `Restaurant` Pydantic models; normalises names, classifies cuisines, and extracts coordinates. |
| **Orchestrator** | `orchestrator.py` | Coordinates the Fetcher and Transformer, applies the rating sort, enforces the result limit, and manages in-memory caching. |

#### Pydantic Data Model
A strict `Restaurant` model (`models/restaurant.py`) acts as the contract between the service layer and the API response. Pydantic validates every field at runtime, so malformed upstream data never silently reaches the client.

#### In-Memory Caching
The `RestaurantService` (Orchestrator) caches the last successful response in memory with a configurable TTL (`AppConfig.CACHE_TTL`). This prevents hammering the Just Eat API on repeated requests and avoids HTTP 429 rate-limit errors during development and testing.

#### Centralised Configuration (`config/`)
All magic strings (API paths, JSON schema keys, separator characters, cuisine taxonomy lists, fallback values) are consolidated inside `AppConfig`. No raw string literals appear inside business logic, making the application resilient to upstream API changes with a single-file edit.

#### Dependency Injection
FastAPI's `Depends()` system (`api/dependencies.py`) is used to inject the `RestaurantService` into route handlers. This means the full service graph (Fetcher → Transformer → Orchestrator) is wired up once and shared, not re-created on every request, and can be swapped for mocks in tests.

#### Directory Structure
Here is how the concepts map to the physical structural components:

```text
backend/
 ├── main.py                  ← application entry point, kept intentionally minimal
 ├── api/
 │    ├── dependencies.py     ← DI pipeline and cached singleton setup
 │    └── routes.py           ← API endpoints mapping
 ├── config/                  ← centralized constants and environmental configuration
 ├── models/
 │    └── restaurant.py       ← Pydantic schemas for strict data validation
 ├── services/
 │    ├── fetcher.py          ← raw HTTP network integration with Just Eat
 │    ├── transformer.py      ← data cleaning, normalization, and taxonomy logic
 │    └── orchestrator.py     ← coordinates service flows, handles caching and sorting
 ├── setup/
 │    ├── startup.py          ← App Factory pattern module (create_app)
 │    └── middleware.py       ← CORS and security configurations
 └── tests/                   ← Pytest suite with isolated testing layers
```

---

### Frontend — React + Vite

#### Technology Choice
I chose **Vite** as the build tool for its near-instant HMR (Hot Module Replacement) and minimal configuration overhead. The frontend itself is plain **React** with no external state management library, since the data requirements are simple enough that local component state and a custom hook are sufficient.

#### Styling Framework (Tailwind CSS)
All styling logic is handled using **Tailwind CSS**. I chose a utility-first CSS framework over traditional stylesheets or heavy component libraries (like Material UI) to keep the bundle size minimal, ensure a consistent design system, and maintain responsive layouts without leaving the JSX structure.

#### Custom Hook as the Data Layer (`useRestaurants`)
All data-fetching concerns (loading state, error state, API call) are encapsulated in a single custom hook (`hooks/useRestaurants.js`). Components that consume it receive a clean `{ restaurants, loading, error }` tuple and remain fully decoupled from any fetching implementation details.

#### Service Abstraction (`services/restaurantService.js`)
The raw `fetch()` call is isolated in a dedicated service module. This means the hook only calls a named function (`fetchRestaurants()`), so the transport layer (URL, headers, error handling) can be changed or mocked without touching any component.

#### Component Hierarchy
The UI is composed with a clear responsibility split:

```text
App
 └── MainView                               ← orchestrates layout, consumes useRestaurants hook
      ├── Header                            ← static branding / navigation
      └── RestaurantList/
           ├── RestaurantListFrame          ← layout wrapper for the list
           ├── LoaderList/                  ← skeleton/loading states (e.g. JETFetchLoader)
           ├── ErrorStatesList/             ← error boundaries (APIFetchError, RestaurantListEmpty)
           ├── SharedComponentsWithCards/   ← reusable sub-elements (e.g. Tag)
           └── RestaurantCards/
                ├── RestaurantPreviewCard   ← orchestrates a single restaurant card
                ├── LoaderCards/            ← card-specific loaders
                ├── ErrorStatesCards/       ← card-specific fallbacks
                └── RestaurantCardsComponents/
                     ├── CardHeader         ← restaurant name and tags
                     ├── CardBody           ← cuisines, rating, address
                     └── MiniMap            ← orchestrates map loading and state
                          └── MiniMapComponents/
                               └── MiniMapFrame  ← Google Maps iframe
```

Each sub-directory within `RestaurantList/` owns a specific UI state (loading, error, data), keeping individual files small and focused.

---

## 🛠️ Data Coverage (Assignment Requirements)

I have ensured that all four mandatory data points are explicitly and clearly displayed:
1.  **Name**: Isolated names of the restaurant as the title on each card.
2.  **Cuisines**: Highlighted the primary ethnical cuisines and displayed the other food and marketing related data as tags.
3.  **Rating**: Displayed as a clear numerical value (e.g., `4.5 / 5`).
4.  **Address**: Displayed the human readable address details as the main address data and used the humanly unreadable coordinate data to display the address on the map.

---

## 🧠 Assumptions & Unclear Parts of The Requirements and How I Dealt With Them

While building the application, I encountered several ambiguities in the raw Just Eat API data. Here is how I approached and resolved them:

1.  **Restaurant Names (Noise Reduction)**: 
    * **The Ambiguity:** The API often returns names appended with location or descriptive fluff using separators (e.g., `"McDonalds, Cattenbury"` or `"Greek Restaurant | Wraps"`). It was unclear if I should display the raw string or sanitize it.

    * **My Solution:** I assumed a cleaner UI was the priority. I implemented a normalization function to strip these separators and extract the pure brand name. Any relevant location data was left to the Address field where it belongs.


2.  **Cuisines (Data Overlap & Categorization)**: 
    * **The Ambiguity:** The `cuisines` array contained a chaotic mix of actual ethnic origins (Italian, Mexican), specific food items (Waffles, Kebab), and marketing tags (Deals, Freebies). It was unclear if these should all be rendered together as "cuisines."
    
    * **My Solution:** I decided not to discard this valuable data, but rather to organize it for better UX. I built a classification system:
        * *Ethnic Cuisines* are highlighted as the primary text.
        * *Food Items* are displayed as secondary visual tags next to the cuisine.
        * *Marketing Tags* are isolated and highlighted in the top-right corner of the card to catch the user's eye.


3.  **Address & Coordinates (Visual Context)**: 
    * **The Ambiguity:** The location data included raw latitude and longitude coordinates. Raw coordinates are not human-readable, and the brief didn't specify whether to display them alongside the address or discard them.
            
    * **My Solution:** Rather than dumping raw numbers on the screen or throwing the data away, I assumed visual context would be best. I used the coordinates to power a **MiniMap (Google Maps Embed)** on each card, showing the exact location visually.


4.  **Extraneous API Data (Scope Management)**:
    * **The Ambiguity:** The API response returned a massive payload with other highly valuable data points (e.g., delivery time, delivery cost, minimum order value). It wasn't mentioned whether adding these to the UI would be seen as a bonus or as failing to follow strict instructions.
    
    * **My Solution:** I decided to strictly adhere to the assignment brief. I intentionally ignored these extra fields to prevent scope creep, keeping the UI clean, focused, and exactly aligned with the four requested data points. (I did, however, note these fields in the "Future Improvements" section).


5.  **Incomplete Data & Marketplace Fairness**: 
    * **The Ambiguity:** The dataset is inconsistent. Some restaurants have rich arrays of marketing tags, specific food items while some lacked parts of it. Or in future cases which was not the case in the part of the dataset I used, some restaurant may lack other details like coordinates or rating. If the UI dynamically displays all this information being unconsiderate of the ones that does not have it, restaurants with complete profiles might appear visually superior or more prominent, potentially creating an unfair advantage on the platform. Details like this on how to treat the unbalanced data is not specified in the requirements. 
    
    * **My Solution:** For the scope of this assignment, I prioritized demonstrating my technical abilities. I implemented dynamic rendering to display all extracted data (e.g., rendering the MiniMap only if coordinates exist, and showing specialty tags if available) to showcase my ability to handle complex data structures and build a rich UI. However, I recognize that in a production environment, there should be a defined business standard (e.g., strict UI normalization or fallback placeholders) to ensure fair competition among all restaurant partners.


6.  **Display Ordering & Default Sorting**: 
    * **The Ambiguity:** The brief requested returning the "first 10 restaurants" but did not specify a sorting mechanism (e.g., default API order, highest rating, alphabetical). 
    
    * **My Solution:** I assumed that prioritizing user experience meant showing the highest-quality options first. Therefore, I implemented a sorting mechanism to display the top 10 restaurants based on their **Rating (highest to lowest)**. I recognize that in a real-world product, this default sort might instead be driven by commercial business logic, such as prioritizing sponsored restaurants or those with active marketing campaigns.


7.  **Graceful Degradation for Partial Data**: 
    * **The Ambiguity:** There were no guidelines on how to handle a restaurant entry if it was missing some of its data (e.g., the API returns a restaurant, but the name or address field is `null`). It was unclear whether to completely discard that restaurant from the top 10 list or display it anyway.

    * **My Solution:** I opted for **graceful degradation**. Rather than completely discarding a restaurant and artificially reducing the available choices for the user, I designed the UI to display whatever valid data is available. If a specific detail is missing, the component safely omits it or provides a sensible fallback, ensuring the restaurant remains visible without breaking the application.
---

    
---

## ✨ Future Improvements

If I had more time, I would expand the application with the following product and technical enhancements:

1. **Interactive Postcode Search**

    * Implement a fully validated UI input field, allowing users to dynamically fetch and explore restaurants for any valid UK postcode instead of relying on a static query.

2. **Dynamic Sorting Mechanisms**

    * Expand beyond the default "highest rating" sort. I would add user-controlled sorting preferences, allowing them to order the restaurant list alphabetically, by proximity (distance), or by total review count.

3. **Filtering Restaurants**

    * Introduce UI toggles and sliders to allow users to filter the fetched list by specific cultural cuisines or by food item tags (e.g. "Pizza", "Sushi" , "Halal" etc.) I have created for the solution of the second problem listed in the "Ambiguities" section or a strict minimum star rating.

4. **Geolocation Integration**

    * Utilize the browser's Geolocation API to capture the user's actual coordinates. I would then use a Haversine formula on the backend to calculate and display the exact physical distance between the user and each restaurant.

5. **Rich Commercial Data Integration**

    * Safely expand the project scope to utilize the other highly valuable data points available in the Just Eat API response, transforming the UI into a fully functional food delivery platform.

6. **Persistent Storage Architecture**

    * Transition from the current in-memory data management approach to securely store restaurant schemas, geographical data, and application states, possible user related data that may added in future such as user preferences, favorite restaurants, order history, etc.

7. **Identity Management & Social Engagement**

    * Implement a secure user authentication system (e.g., JWT or OAuth 2.0) to support personalized user accounts. This would unlock community-driven features, allowing users to save favorite restaurants, highlight specific menu items, and leave interactive comments or reviews.

8. **Cross-Platform Mobile Integration**

    * Acknowledging that food delivery is primarily a mobile-driven user journey, I would convert the web application into a Progressive Web App (PWA) for offline capabilities, or migrate the frontend UI components to **React Native** to deploy native iOS and Android applications.

9. **Two-Sided Marketplace & Vendor Portal**

    * Expand the application from a consumer-only interface into a full two-sided marketplace. I would develop a dedicated vendor portal where restaurant owners can create provider accounts, claim their business, and dynamically manage their own profiles, menus, and marketing tags.

---
*Created by Arda Guney - JET Coding Assignment*
