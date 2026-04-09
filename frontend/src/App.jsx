import { useState, useEffect } from 'react'

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
    /* max-width 800px, centered, with padding */
    <div className="max-w-[800px] mx-auto p-5 font-sans">

      {/* Title: White to pop against your orange background, bold and centered */}
      <h1 className="text-4xl font-bold text-white text-center mb-2">
        Just Eat Takeaway Coding Assignment
      </h1>

      <p className="text-white text-center mb-8 opacity-90">
        Fetching local restaurants directly from the API
      </p>
      {/* Fetched data connects to the UI here
          React gets the restaurants list fetched from the API and creates a separate
          list item for every instance in the list to display all the restaurants' details.
      */}
      {/* The List: No bullets, centered in the frame */}
      <ul className="list-none p-0 space-y-4">
        {restaurants.map((restaurant, index) => (
          /* The Card: White background, rounded corners, soft shadow, and a hover effect */
          <li key={index} className="bg-white border-2 border-gray-100 rounded-2xl p-6 shadow-md transition-transform hover:scale-[1.01]">

            {/* Display the restaurant name hierarchically above the other details by h3 tag */}
            {/* Restaurant Name: The official JET Orange color */}
            <h3 className="text-2xl font-bold text-[#ff8000] mb-3 text-left">
              {restaurant.Name || restaurant.name}
            </h3>

            {/* Display the restaurant cuisines, rating, and address in same hierarchy */}
            <div className="space-y-1 text-left">
              <p className="text-gray-700">
                <span className="font-bold">Cuisines:</span> {restaurant.Cuisines || restaurant.cuisines}
              </p>
              <p className="text-gray-700">
                <span className="font-bold">Rating:</span> {restaurant.Rating || restaurant.rating}
              </p>
              <p className="text-gray-700">
                <span className="font-bold">Address:</span> {restaurant.Address || restaurant.address}
              </p>
            </div>

          </li>
        ))}
      </ul>
    </div>
  )
}

export default App  