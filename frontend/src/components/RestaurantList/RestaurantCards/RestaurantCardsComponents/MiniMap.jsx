import { useState, useEffect } from 'react';
import { MapLoader } from '../LoaderCards/MapLoader';
import { MapErrorState } from '../ErrorStatesCards/MapErrorState';
import { MiniMapFrame } from './MiniMapComponents/MiniMapFrame';

/**
 * MiniMap component: Responsive Google Maps integration with state management.
 * Orchestrates loading timeouts, error states, and the iframe presentation.
 */
export function MiniMap({ lat, lng }) {
    const [isLoading, setIsLoading] = useState(true);
    const [hasError, setHasError] = useState(false);

    // 8-second timeout safety net
    useEffect(() => {
        const timer = setTimeout(() => {
            if (isLoading) {
                setHasError(true);
                setIsLoading(false);
            }
        }, 8000);

        return () => clearTimeout(timer);
    }, [isLoading]);

    // 1. Validation: Ensure lat and lng are valid numbers (or can be converted to numbers)
    const isValidLat = lat !== null && !isNaN(parseFloat(lat)) && isFinite(lat);
    const isValidLng = lng !== null && !isNaN(parseFloat(lng)) && isFinite(lng);
    const isValidLocation = isValidLat && isValidLng;

    return (
        <div className="relative h-full min-h-[130px] w-full rounded-xl overflow-hidden border border-gray-200 shadow-sm transition-all hover:shadow-md bg-gray-50 flex items-center justify-center">
            {/* If location is invalid, show the Error state immediately */}
            {!isValidLocation ? (
                <MapErrorState />
            ) : (
                <>
                    {isLoading && !hasError && <MapLoader />}

                    {hasError && <MapErrorState />}

                    {!hasError && (
                        <MiniMapFrame
                            lat={lat}
                            lng={lng}
                            isLoading={isLoading}
                            onMapLoad={() => setIsLoading(false)}
                        />
                    )}
                </>
            )}
        </div>
    );
}