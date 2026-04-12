import { render, screen } from '@testing-library/react';
import { FallbackRestaurantCard } from '../components/RestaurantList/RestaurantCards/ErrorStatesCards/FallbackRestaurantCard';

describe('FallbackRestaurantCard Component', () => {
  it('renders the Restaurant Unavailable text correctly', () => {
    // 1. Arrange & Act: Render the component in the virtual DOM
    render(<FallbackRestaurantCard />);

    // 2. Assert: Check if the main error text is visible to the user
    const titleElement = screen.getByText(/Restaurant Unavailable/i);
    expect(titleElement).toBeInTheDocument();
  });

  it('renders the helper message', () => {
    render(<FallbackRestaurantCard />);
    
    // Check for the sub-text that explains why this card appears
    const subtitleElement = screen.getByText(/Trouble loading the details/i);

    expect(subtitleElement).toBeInTheDocument();
  });
});
