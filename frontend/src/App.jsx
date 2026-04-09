import { useState, useEffect } from 'react'
// 1. Import the logo from your assets folder
import jetLogo from './assets/jet-logo-white.png'

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
    /* max-width 800px, centered, with padding and making the background color JET orange */
    <div className="min-h-screen bg-[#ff000] font-sans">

      {/* This inner div is the 'Content Frame'.
       - max-w-[800px]: Keeps the list from getting too wide on big monitors.
       - mx-auto: Centers this frame horizontally.
      */}
      {/* Fetched data connects to the UI here
          React gets the restaurants list fetched from the API and creates a separate
          list item for every instance in the list to display all the restaurants' details.
      */}
      <header className="bg-[#ff8000] py-1 px-5 shadow-md">
        <div className="max-w-[1000px] mx-auto">
          <img
            src={jetLogo}
            alt="Just Eat Takeaway Logo"
            className="h-30 mx-auto"
          />
        </div>
      </header>
      <main className="max-w-[1000px] mx-auto p-5 pt-8">
        <h1 className="text-[#ff8000] text-2xl md:text-4xl font-bold text-center">
          Complete at Home Coding Assignment
        </h1>

        <p className="text-[#ff8000] text-center mb-8 opacity-90">
          Displaying the details of the first 10 restaurants fetched from the Just Eat Takeaway API
        </p>
        <ul className="list-none p-0 space-y-4" >
          {restaurants.map((restaurant, index) => (
            /* Card Styling adding border, rounded corners, padding, shadow, and hover effect */
            /* Use the official JET Cupcake Blue color for restaurant cards */
            <li key={index} className="bg-[#C1DADE] border-2 border-gray-100 rounded-2xl p-6 shadow-md transition-transform hover:scale-[1.01]">
              {/* Display the restaurant name hierarchically above the other details by h3 tag */}
              {/* Use the official JET Orange color for restaurant names */}
              <h3 className="text-2xl font-bold text-[#ff8000] mb-3 text-left">
                {restaurant.Name || restaurant.name}
              </h3>

              {/* Display the restaurant cuisines, rating, and address in same hierarchy and bold the labels*/}
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
      </main>
    </div>
  )
}

export default App  