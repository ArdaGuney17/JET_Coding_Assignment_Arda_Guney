import { describe, it, expect } from 'vitest';
import { render, screen } from '@testing-library/react';
import { JETFetchLoader } from '../components/RestaurantList/LoaderList/JETFetchLoader';

describe('Loading States Components', () => {
  it('renders the JETFetchLoader with branded text', () => {
    const { container } = render(<JETFetchLoader />);

    // Verify the specific branded text exists
    expect(screen.getByText(/Fetching the best restaurants for you/i)).toBeInTheDocument();

    // Verify the root div has the expected styling classes
    const rootDiv = container.firstChild;
    expect(rootDiv).toHaveClass('flex-col', 'items-center', 'justify-center');
  });
});
