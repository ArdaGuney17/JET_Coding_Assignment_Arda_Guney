# 📋 Functional Requirements & Technical Implementation

This document provides a detailed breakdown of the logic powering the **Restaurant Scout** application. It separates the core project mandates from the advanced architectural improvements implemented during development.

---

## 1. Core Task Requirements
As per the assignment brief, the following mandatory data points are successfully fetched, transformed, and displayed. The list is strictly limited to the **first 10 restaurants** returned:

* **Restaurant Name**: Isolated the clean brand names of the restaurants and displayed them as the primary title on each card.
* **Cuisines**: Highlighted the primary cultural cuisines and extracted secondary food types/marketing data to display as supporting helper tags.
* **Rating**: Parsed and displayed as a clear, verified numerical value (e.g., `4.5 / 5`).
* **Address**: Rendered the human-readable text (City, Street, Postcode) as the main address line, while utilizing the raw, unreadable GPS coordinates to visually display the location on a map.

---

## 2. Architectural & UX Enhancements

Beyond the basic requirements, several sophisticated logic layers were added to ensure the application feels professional, intuitive, and highly resilient.

### ✨ Intelligent Data Cleaning (`_clean_name`)
The raw Just Eat API often includes extra data in the name field (e.g., `"Subway - London | High Street"`). 
- **Implementation**: I built a normalization engine that detects separators like `-`, `|`, and `,`. 
- **Outcome**: The UI displays only the clean brand name (**Subway**), while the supporting location data is implicitly handled by the Address field where it belongs.

### 🍱 Multi-Tier Cuisine Classification
Raw API data often lumps "Italian" (Cultural) together with "Pizza" (Food Type) and "Deals" (Marketing). I implemented a three-tier classification system:
1.  **Primary Cuisines**: Dedicated list of 70+ cultural identities (Italian, Japanese, etc.) rendered in large branded text.
2.  **Specialty Tags**: Specific food items (Burgers, Tacos) displayed as helper tags next to the cuisine.
3.  **Marketing Insights**: High-value tags like "Free Delivery" or "Offers" are automatically moved to the top-right of the card to catch the user's eye.

### 📍 Geographic Mapping (From GPS to Visuals)
Raw coordinates (like `0.12, 51.52`) are unreadable to humans. 
- **Implementation**: Instead of letting these strings "go astray," I integrated a **MiniMap** component. 
- **Outcome**: The backend extracts these coordinates and the frontend injects them into a Google Maps Embed frame, giving the user instant visual context of where the restaurant is located.

### 🛡️ The 5 Layers of Resilience (Error Handling)

I assumed that every external dependency (the API, the network, the GPS data) could fail. I built 5 distinct layers of protection:

#### Layer 1: Network & Timeout Safety (Backend)
- **`JETDataFetcher`**: All network calls are wrapped in `try-except urllib` blocks. If the external Just Eat API is down or times out, the backend doesn't crash; it logs the error and returns a clean `None`, preventing a system-wide failure.

#### Layer 2: Data Schema Defense (Backend)
- **`RestaurantTransformer`**: I used defensive `.get()` calls for every nested field (Address, Rating, Location). This ensures that if the API schema changes or a field is missing, the code doesn't throw a `KeyError`.
- **`_clean_name`**: The name-cleaning logic is isolated in its own `try-except` block. If the cleaning logic encounters a bizarre character or null value, it falls back to a branded "New Restaurant" label instead of breaking the transformer.

#### Layer 3: Architectural Orchestration (Backend)
- **`RestaurantService`**: Before attempting to loop through data, I checked for `if not raw_data`. If the API returns an empty object or a 404, the service simply returns an empty list `[]`, which the frontend can then handle gracefully.

#### Layer 4: Lifecycle & UI States (Frontend)
- **State Management**: The main application tracks `isLoading` and `error` states. 
    - **`APIFetchError`**: If the entire backend fails, the user sees a helpful, styled error message instead of a blank white screen.
    - **`EmptyState`**: If the postcode has no restaurants, the `RestaurantListFrame` detects `isEmpty` and renders a themed "No Restaurants Found" illustration.

#### Layer 5: Component-Level Isolation (Frontend)
- **`MiniMap.isCoordValid`**: Before asking Google to render a map, I validated the GPS coordinates. If they are malformed or missing, I render an "In-Card Error" message specifically for that map, keeping the rest of the restaurant card interactive.
- **`FallbackRestaurantCard`**: This acts as an "Emergency Buffer." If a specific restaurant's data is so corrupted that it can't be displayed, we render a standalone "Restaurant Unavailable" card for that item only, allowing the other 9 restaurants to still be visible to the user.

---

## 3. Full Project Function Registry

| Layer | Function / Component | Purpose |
| :--- | :--- | :--- |
| **Backend (Setup)** | `setup.startup.create_app` | The "Factory" that assembles and returns the FastAPI instance. |
| **Backend (Setup)** | `setup.middleware.setup_middleware` | Configures security policies (CORS) for every incoming request. |
| **Backend (API)** | `api.routes.get_restaurants` | The primary entry point that exposes the data to the frontend. |
| **Backend (Logic)** | `RestaurantTransformer._clean_name` | Removes noise and separators from the raw brand names. |
| **Backend (Logic)** | `RestaurantTransformer._extract_cuisines_and_tags` | Categorizes raw tags into Cultural, Specialty, or Marketing groups. |
| **Backend (Logic)** | `RestaurantFetcher.fetch_restaurants` | Handles low-level HTTP communication and network timeouts. |
| **Backend (Logic)** | `Orchestrator.get_top_rated_restaurants` | Orchestrates the data flow and manages the in-memory cache. |
| **Frontend (Core)** | `App.jsx / useEffect` | The "State Engine" that manages Loading, Success, and Error cycles. |
| **Frontend (UI)** | `RestaurantPreviewCard` | The high-level orchestrator for individual restaurant entries. |
| **Frontend (UI)** | `CardDetails` | Ensures Name, Cuisines, Rating, and Address are formatted for the user. |
| **Frontend (UI)** | `MiniMap` | Converts coordinate data into a visual Google Maps experience. |
| **Frontend (UI)** | `Tag` | A reusable, branded styling element used for all metadata and tags. |
| **Frontend (UI)** | `JETFetchLoader` | Provides a branded, themed loading experience for the user. |
| **Frontend (Safety)** | `FallbackRestaurantCard` | Isolates errors so broken data doesn't impact the rest of the UI. |

---

---

## 4. Automated Testing & Quality Assurance

To ensure the long-term stability and resilience of the application, I implemented a dual-layer automated testing suite with **27/27 successful test cases**.

### 🐍 Backend Testing (Pytest)
**Command:** `cd backend && .\venv\Scripts\python -m pytest tests/`

I utilized `pytest` to verify the highly decoupled modularity of our backend architecture:
- **Transformer Unit Tests**: Verified name-cleaning logic, address formatting, and the three-tier cuisine classification.
- **Service Mocking**: Implemented `unittest.mock` to isolate the Orchestrator, allowing us to test business logic independently of external network conditions.
- **Integration Tests**: Used FastAPI's `TestClient` to conduct high-level API route testing, ensuring our endpoints return correct status codes and JSON schemas.

### ⚛️ Frontend Testing (Vitest & RTL)
**Command:** `cd frontend && npm run test`

I utilized `Vitest` and `React Testing Library` to verify UI resilience and component behavior:
- **Requirement Verification**: Component tests ensure that Name, Cuisine, Rating, and Address are always rendered as expected.
- **Data Resilience (The Stress Test)**: Specifically tested components against **null, undefined, and corrupted data**. These tests confirm that our "Fallback" UI prevents a single broken restaurant from crashing the entire list.
- **Interactive Mapping Logic**: Verified that the `MiniMap` correctly detects missing coordinates and renders a graceful error state rather than a broken iframe.
---
*Documented by Arda Guney - JET Coding Assignment*