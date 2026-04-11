import { render, screen } from '@testing-library/react';
import { CardHeader } from '../CardHeader';
import { CardDetails } from '../CardBody';

describe('Card Content Resilience', () => {
    describe('CardHeader', () => {
        it('renders the restaurant name', () => {
            render(<CardHeader name="Pizza Palace" tags={['Deals']} />);
            expect(screen.getByText(/Pizza Palace/i)).toBeInTheDocument();
            expect(screen.getByText(/Deals/i)).toBeInTheDocument();
        });

        it('handles missing tags safely', () => {
            render(<CardHeader name="Generic Food" tags={null} />);
            expect(screen.getByText(/Generic Food/i)).toBeInTheDocument();
            // Should not crash, and no tags container should be rendered
        });
    });

    describe('CardDetails (Body)', () => {
        it('renders full data correctly', () => {
            render(
                <CardDetails 
                    cuisines="Italian" 
                    rating={4.5} 
                    address="123 Spaghetti St" 
                    specialties={['Pasta', 'Wine']} 
                />
            );
            expect(screen.getByText(/Italian/i)).toBeInTheDocument();
            expect(screen.getByText(/4.5 \/ 5/i)).toBeInTheDocument();
            expect(screen.getByText(/123 Spaghetti St/i)).toBeInTheDocument();
            expect(screen.getByText(/Pasta/i)).toBeInTheDocument();
        });

        it('handles missing rating with N/A', () => {
            render(<CardDetails rating={null} />);
            expect(screen.getByText(/N\/A/i)).toBeInTheDocument();
        });

        it('handles missing address with Not available', () => {
            render(<CardDetails address={null} />);
            expect(screen.getByText(/Not available/i)).toBeInTheDocument();
        });

        it('handles missing cuisines and specialties gracefully', () => {
            render(<CardDetails cuisines={null} specialties={null} />);
            expect(screen.getByText(/Not specified/i)).toBeInTheDocument();
        });
    });
});
