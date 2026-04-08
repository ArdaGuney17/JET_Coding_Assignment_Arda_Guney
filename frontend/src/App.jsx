import { useState, useEffect } from 'react'
import './App.css' // Import the styles specifically for this component

function App() {
  // Initialize state to hold the fetched restaurant array.
  // Updating this state via setRestaurants will tell React to automatically update the UI
  const [restaurants, setRestaurants] = useState([])

  // Execute the data fetch operation once when the app first loads
  useEffect(() => {
    // Request data from the local Python API endpoint
    fetch('http://localhost:8000/')
      // Parse the raw response into JSON
      .then(response => response.json())
      // Save the parsed data into our state so it can be displayed
      .then(data => setRestaurants(data))
      // Catch and display any network or parsing errors
      .catch(error => console.error("Error fetching data:", error))
  }, [])

  return (
    <div>
      <h1>Just Eat Takeaway Coding Assignment</h1>
      <p>Fetching local restaurants directly from the API</p>
      {/* Fetched data connects to the UI here
          React gets the restaurants list fetched from the API and creates a separate
          list item for every instance in the list to display all the restaurants' details.
      */}
      <ul>
        {restaurants.map((restaurant, index) => (
          <li key={index}>
            {/* Display the restaurant name hierarchically above the other details by h3 tag */}
            <hr />
            <h3>
              {restaurant.Name || restaurant.name}
            </h3>
            {/* Display the restaurant cuisines, rating, and address in same hierarchy */}
            <div>
              <p><strong>Cuisines:</strong> {restaurant.Cuisines || restaurant.cuisines}</p>
              <p><strong>Rating:</strong> {restaurant.Rating || restaurant.rating}</p>
              <p><strong>Address:</strong> {restaurant.Address || restaurant.address}</p>
            </div>

          </li>
        ))}
      </ul>
    </div>
  )
}

export default App  