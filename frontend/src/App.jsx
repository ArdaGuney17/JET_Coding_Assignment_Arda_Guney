import { useState, useEffect } from 'react'
// Import the Just Eat Takeaway logo from the assets folder
import jetLogo from './assets/jet-logo-white.png'
// Import the necessary components from the components.jsx file
import { Header, RestaurantList, RestaurantCard } from './components'

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
    // The empty array [] ensures this effect runs only once after the initial render
  }, [])

  return (
    // The main container for the entire application
    <div className="min-h-screen bg-white font-sans">
      {/* Header Component displays the brand logo and assignment titles. */}
      <Header logo={jetLogo} />
      {/* RestaurantList Component is a scrollable container that maps the 
      restaurant data into individual cards. */}
      <RestaurantList>
        {/* Iterate over the restaurants array and render a RestaurantCard Component for each */}
        {restaurants.map((res, index) => (
          <RestaurantCard key={index} {...res} />
        ))}
      </RestaurantList>
    </div>
  )
}

export default App