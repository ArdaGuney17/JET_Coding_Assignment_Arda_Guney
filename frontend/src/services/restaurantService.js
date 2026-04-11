/**
 * API Service for fetching restaurant data.
 */

import { restaurantServiceConfig } from '../config/restaurantServiceConfig.js';

const API_URL = restaurantServiceConfig.BACKEND_API_BASE;

export async function fetchRestaurants() {
  const response = await fetch(API_URL);
  
  if (!response.ok) {
    throw new Error(`Server responded with status ${response.status}`);
  }
  
  return response.json();
}
