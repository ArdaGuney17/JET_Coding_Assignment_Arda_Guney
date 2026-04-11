import { render, screen } from '@testing-library/react';
import { JETFetchLoader } from '../JETFetchLoader';

describe('Loading States Components', () => {
  it('renders the JETFetchLoader with branded text', () => {
    render(<JETFetchLoader />);
    
    // Verify the specific branded text exists
    expect(screen.getByText(/Fetching the best restaurants for you/i)).toBeInTheDocument();
    
    // Verify the container has the expected styling classes (optional but good for visual components)
    const container = screen.getByText(/Fetching the best restaurants/i).parentElement;
    expect(container).toHaveClass('flex-col', 'items-center', 'justify-center');
  });
});
