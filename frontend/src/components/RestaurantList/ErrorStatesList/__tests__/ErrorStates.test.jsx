import { render, screen } from '@testing-library/react';
import { APIFetchError } from '../APIFetchError';
import { EmptyState } from '../RestaurantListEmpty';

describe('Error States Components', () => {
  describe('APIFetchError', () => {
    it('renders the custom error message', () => {
      const testMessage = "Test Error Message";
      render(<APIFetchError message={testMessage} />);
      
      expect(screen.getByText(/Something went wrong/i)).toBeInTheDocument();
      expect(screen.getByText(testMessage)).toBeInTheDocument();
      expect(screen.getByRole('button', { name: /Try Again/i })).toBeInTheDocument();
    });

    it('renders fallback message if no message provided', () => {
      render(<APIFetchError />);
      expect(screen.getByText(/We couldn't connect to the server/i)).toBeInTheDocument();
    });
  });

  describe('EmptyState', () => {
    it('renders with default props', () => {
      render(<EmptyState />);
      expect(screen.getByText(/No available deliciousness around you/i)).toBeInTheDocument();
      expect(screen.getByText(/🍽️/)).toBeInTheDocument();
    });

    it('renders with custom props', () => {
      render(<EmptyState icon="🔍" title="Nothing found" message="Try again" />);
      expect(screen.getByText(/Nothing found/i)).toBeInTheDocument();
      expect(screen.getByText(/🔍/)).toBeInTheDocument();
      expect(screen.getByText(/Try again/i)).toBeInTheDocument();
    });
  });
});
