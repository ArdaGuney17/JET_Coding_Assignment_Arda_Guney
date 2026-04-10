/**
 * API Service for fetching restaurant data.
 */

const API_URL = 'http://localhost:8000/';

export async function fetchRestaurants() {
  const response = await fetch(API_URL);
  
  if (!response.ok) {
    throw new Error(`Server responded with status ${response.status}`);
  }
  
  return response.json();
}
