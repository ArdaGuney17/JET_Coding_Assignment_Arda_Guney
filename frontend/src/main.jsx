// React's built-in tool for highlighting potential problems in an application.
import { StrictMode } from 'react'

// The method used to create a React root, which manages rendering the app into the browser.
import { createRoot } from 'react-dom/client'

// Importing the Tailwind styles globally for use in the application.
import './index.css'

// Importing the main component that contains all of our UI logic and restaurant cards.
import App from './App.jsx'

// Finds the 'root' div in the HTML and puts our App inside it
createRoot(document.getElementById('root')).render(
  <StrictMode>
    <App />
  </StrictMode>,
)