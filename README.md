# 🍽️ Return First 10 Restaurants - JET Complete at Home Coding Assignment

My solution to the JET Complete at Home Coding Assignment. Returns the first 10 restaurants for a given postcode with their requested data: name, cuisines, rating, and address.

---

## 🚀 Quick Start: How to Run

### 0. Clone the Repository
First, clone the project to your local machine:

```bash
git clone [https://github.com/ArdaGuney17/JET_Coding_Assignment_Arda_Guney.git](https://github.com/ArdaGuney17/JET_Coding_Assignment_Arda_Guney.git)
```

Go to the project folder:

```bash
cd JET_Coding_Assignment_Arda_Guney
```

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

- **Interactive Postcode Search**: Implement a fully validated UI input field, allowing users to dynamically fetch and explore restaurants for any valid UK postcode instead of relying on a static query.
- **Dynamic Sorting Mechanisms**: Expand beyond the default "highest rating" sort. I would add user-controlled sorting preferences, allowing them to order the restaurant list alphabetically, by proximity (distance), or by total review count.
- **Granular Faceted Filtering**: Introduce UI toggles and sliders to allow users to filter the fetched list by specific cultural cuisines, individual food items, or a strict minimum star rating.
- **Geolocation Integration**: Utilize the browser's Geolocation API to capture the user's actual coordinates. I would then use a Haversine formula on the backend to calculate and display the exact physical distance between the user and each restaurant.
- **Rich Commercial Data Integration**: Safely expand the project scope to utilize the other highly valuable data points available in the Just Eat API response, transforming the UI into a fully functional food delivery platform.
- **Persistent Storage Architecture**: Transition from the current in-memory data management approach to securely store restaurant schemas, geographical data, and application states, possible user related data that may added in future such as user preferences, favorite restaurants, order history, etc.
- **Identity Management & Social Engagement**: Implement a secure user authentication system (e.g., JWT or OAuth 2.0) to support personalized user accounts. This would unlock community-driven features, allowing users to save favorite restaurants, highlight specific menu items, and leave interactive comments or reviews.
- **Cross-Platform Mobile Integration**: Acknowledging that food delivery is primarily a mobile-driven user journey, I would convert the web application into a Progressive Web App (PWA) for offline capabilities, or migrate the frontend UI components to **React Native** to deploy native iOS and Android applications.
- **Two-Sided Marketplace & Vendor Portal**: Expand the application from a consumer-only interface into a full two-sided marketplace. I would develop a dedicated vendor portal where restaurant owners can create provider accounts, claim their business, and dynamically manage their own profiles, menus, and marketing tags.

---
*Created by Arda Guney - JET Coding Assignment*
