import { render, screen } from '@testing-library/react';
import { MiniMap } from '../MiniMap';

describe('MiniMap Component Resilience', () => {
    it('renders the map frame when valid coordinates are provided', () => {
        // Valid London coordinates
        render(<MiniMap lat={51.5074} lng={-0.1278} />);
        
        // The iframe for Google Maps should be present (via MiniMapFrame)
        // Note: Using getByTitle since the iframe has a title "Restaurant Location Map"
        expect(screen.getByTitle(/Restaurant Location Map/i)).toBeInTheDocument();
    });

    it('renders the MapErrorState when coordinates are null', () => {
        render(<MiniMap lat={null} lng={null} />);
        
        // Assert that the error state message is displayed
        expect(screen.getByText(/Map Unavailable/i)).toBeInTheDocument();
    });

    it('renders the MapErrorState when coordinates are invalid strings', () => {
        render(<MiniMap lat="apple" lng="banana" />);
        
        expect(screen.getByText(/Map Unavailable/i)).toBeInTheDocument();
    });

    it('renders the MapErrorState when coordinates are missing', () => {
        render(<MiniMap />);
        
        expect(screen.getByText(/Map Unavailable/i)).toBeInTheDocument();
    });
});
