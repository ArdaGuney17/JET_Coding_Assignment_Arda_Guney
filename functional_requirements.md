# 📋 Functional Requirements & Technical Implementation

This document provides a detailed breakdown of the logic powering the **Restaurant Scout** application. It separates the core project mandates from the advanced architectural improvements implemented during development.

---

## 1. Core Task Requirements
As per the assignment brief, the following mandatory data points are successfully fetched, transformed, and displayed:

*   **Restaurant Name**: Cleaned brand representation.
*   **Cuisines**: Culturally accurate identifiers.
*   **Rating**: Verified numerical value out of 5.
*   **Address**: Formatted city, street, and postcode.

---

## 2. Advanced Improvements (The "Arda" Edition)

Beyond the basic requirements, several sophisticated logic layers were added to ensure the application feels professional and resilient.

### ✨ Intelligent Data Cleaning (`_clean_name`)
The raw Just Eat API often includes extra data in the name field (e.g., `"Subway - London | High Street"`). 
- **Implementation**: We implemented a normalization engine that detects separators like `-`, `|`, and `,`. 
- **Outcome**: The UI displays only the clean brand name (**Subway**), while the supporting location data is moved to the Address field where it belongs.

### 🍱 Multi-Tier Cuisine Classification
Raw API data often lumps "Italian" (Cultural) together with "Pizza" (Food Type) and "Deals" (Marketing). We implemented a three-tier classification system:
1.  **Primary Cuisines**: Dedicated list of 70+ cultural identities (Italian, Japanese, etc.) rendered in large branded text.
2.  **Specialty Tags**: specific food items (Burgers, Tacos) displayed as helper tags next to the cuisine.
3.  **Marketing Insights**: High-value tags like "Free Delivery" or "Offers" are automatically moved to the top-right of the card to catch the user's eye.

### 📍 Geographic Mapping (From GPS to Visuals)
Raw coordinates (like `0.12, 51.52`) are unreadable to humans. 
- **Implementation**: Instead of letting these strings "go astray," we integrated a **MiniMap** component. 
- **Outcome**: The backend extracts these coordinates and the frontend injects them into a Google Maps Embed frame, giving the user instant visual context of where the restaurant is located.

### 🛡️ The 5 Layers of Resilience (Error Handling)

We assumed that every external dependency (the API, the network, the GPS data) could fail. We built 5 distinct layers of protection:

#### Layer 1: Network & Timeout Safety (Backend)
- **`JETDataFetcher`**: All network calls are wrapped in `try-except urllib` blocks. If the external Just Eat API is down or times out, the backend doesn't crash; it logs the error and returns a clean `None`, preventing a system-wide failure.

#### Layer 2: Data Schema Defense (Backend)
- **`RestaurantTransformer`**: We use defensive `.get()` calls for every nested field (Address, Rating, Location). This ensures that if the API schema changes or a field is missing, the code doesn't throw a `KeyError`.
- **`_clean_name`**: The name-cleaning logic is isolated in its own `try-except` block. If the cleaning logic encounters a bizarre character or null value, it falls back to a branded "New Restaurant" label instead of breaking the transformer.

#### Layer 3: Architectural Orchestration (Backend)
- **`RestaurantService`**: Before attempting to loop through data, the Orchestrator checks for `if not raw_data`. If the API returns an empty object or a 404, the service simply returns an empty list `[]`, which the frontend can then handle gracefully.

#### Layer 4: Lifecycle & UI States (Frontend)
- **State Management**: The main application tracks `isLoading` and `error` states. 
    - **`APIFetchError`**: If the total backend fails, the user sees a helpful, styled error message instead of a blank white screen.
    - **`EmptyState`**: If the postcode has no restaurants, the `RestaurantListFrame` detects `isEmpty` and renders a themed "No Restaurants Found" illustration.

#### Layer 5: Component-Level Isolation (Frontend)
- **`MiniMap.isCoordValid`**: Before asking Google to render a map, we validate the GPS coordinates. If they are malformed or missing, we render an "In-Card Error" message specifically for that map, keeping the rest of the restaurant card interactive.
- **`FallbackRestaurantCard`**: This acts as an "Emergency Buffer." If a specific restaurant's data is so corrupted that it can't be displayed, we render a standalone "Restaurant Unavailable" card for that item only, allowing the other 9 restaurants to still be visible to the user.

---

## 3. Full Project Function Registry

| Layer | Function / Component | Purpose |
| :--- | :--- | :--- |
| **Backend (Setup)** | `setup.startup.create_app` | The "Factory" that assembles and returns the FastAPI instance. |
| **Backend (Setup)** | `setup.middleware.setup_middleware` | Configures security policies (CORS) for every incoming request. |
| **Backend (API)** | `api.routes.get_restaurants` | The primary entry point that exposes the data to the internet. |
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
*Documented by Arda Guney - Strategic Implementation*
