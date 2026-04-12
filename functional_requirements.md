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

### 🛡️ Resilience & Error Handling
We assumed the external API might fail or provide corrupted data. We built a "Safety Net" system:
- **Backend**: Every data point is wrapped in a `try-except` block or a defensive `.get()` call with fallbacks like "Unknown Restaurant" or "N/A".
- **Frontend**: We implemented **Component Isolation**. If one restaurant has corrupted data, we show a `FallbackRestaurantCard` for that item only. This prevents a single broken piece of data from crashing the entire application.

---

## 3. Major Function Registry

| Layer | Function | Purpose |
| :--- | :--- | :--- |
| **Backend** | `RestaurantTransformer._clean_name` | Removes noise and separators from the brand name. |
| **Backend** | `RestaurantTransformer._extract_cuisines_and_tags` | Categorizes raw tags into Cultural, Specialty, or Marketing. |
| **Backend** | `RestaurantFetcher.fetch_restaurants` | Handles HTTP communication and timeouts with the external API. |
| **Backend** | `Orchestrator.get_top_rated_restaurants` | Manages the flow between Fetching -> Transforming -> Caching. |
| **Frontend** | `MiniMap.isCoordValid` | Validates that GPS data exists before attempting to render a map. |
| **Frontend** | `RestaurantListFrame.useEffect` | Manages the API lifecycle (Loading -> Success -> Error). |
| **Frontend** | `FallbackRestaurantCard` | Renders a "Safety State" if a component enters an error state. |

---
*Documented by Arda Guney - Strategic Implementation*
