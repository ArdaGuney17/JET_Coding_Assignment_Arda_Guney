import { describe, it, expect } from 'vitest';
import { render, screen } from '@testing-library/react';
import { JETFetchLoader } from '../JETFetchLoader';

describe('Loading States Components', () => {
  it('renders the JETFetchLoader with branded text', () => {
    // We can destructure 'container' directly from render to get the root element
    const { container } = render(<JETFetchLoader />);
    
    // 1. Verify the specific branded text exists
    expect(screen.getByText(/Fetching the best restaurants for you/i)).toBeInTheDocument();
    
    // 2. Verify the root div has the expected styling classes
    const rootDiv = container.firstChild;
    expect(rootDiv).toHaveClass('flex-col', 'items-center', 'justify-center');
  });
});
