import { useState, useEffect } from 'react'
import { fetchRestaurants } from '../services/restaurantService'

/**
 * Custom Hook: useRestaurants
 * Handles data fetching logic and manages loading/error states.
 */
export function useRestaurants() {
  const [restaurants, setRestaurants] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)

  useEffect(() => {
    fetchRestaurants()
      .then(data => {
        setRestaurants(data)
        setLoading(false)
      })
      .catch(err => {
        console.error("Error fetching data:", err)
        setError(err.message)
        setLoading(false)
      })
  }, [])

  return { restaurants, loading, error }
}
