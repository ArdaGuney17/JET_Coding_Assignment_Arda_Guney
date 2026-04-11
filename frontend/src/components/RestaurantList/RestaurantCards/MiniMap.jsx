import { useState, useEffect } from 'react';
import { MiniMapConfig } from '../../../config/MiniMapConfig';

/**
 * MapLoading Sub-Component: Displays the branded spinner while the map loads.
 */
function MapLoading() {
    return (
        <div className="absolute inset-0 flex flex-col items-center justify-center bg-gray-50 z-10 transition-opacity duration-300">
            <div className="w-6 h-6 border-2 border-[#FF8000] border-t-transparent rounded-full animate-spin mb-2"></div>
            <span className="text-[10px] text-gray-400 font-medium uppercase tracking-widest">Loading Map</span>
        </div>
    );
}

/**
 * MapError Sub-Component: Displays the locator icon and fallback text on failure.
 */
function MapError() {
    return (
        <div className="absolute inset-0 flex flex-col items-center justify-center bg-gray-50 z-10 p-4 text-center">
            <span className="text-xl mb-1">📍</span>
            <span className="text-[10px] text-gray-500 font-bold uppercase tracking-wider mb-1">Map Unavailable</span>
            <span className="text-[9px] text-gray-400 leading-tight">Check your connection or try again later</span>
        </div>
    );
}

/**
 * MapFrame Sub-Component: Contains the Google Maps iframe with smooth fade-in logic.
 */
function MapFrame({ lat, lng, isLoading, onMapLoad }) {
    return (
        <iframe
            width="100%"
            height="100%"
            style={{ border: 0 }}
            loading="lazy"
            allowFullScreen
            referrerPolicy="no-referrer-when-downgrade"
            src={`${MiniMapConfig.MAPS_BASE_URL}?q=${lat},${lng}&z=${MiniMapConfig.MAPS_DEFAULT_ZOOM}&output=embed`}
            onLoad={onMapLoad}
            className={`transition-opacity duration-500 ${isLoading ? 'opacity-0' : 'opacity-100'}`}
        ></iframe>
    );
}

/**
 * MiniMap component: Responsive Google Maps integration with state management.
 * Isolated into its own file to manage iframe loading and error states.
 */
export function MiniMap({ lat, lng }) {
    const [isLoading, setIsLoading] = useState(true);
    const [hasError, setHasError] = useState(false);

    useEffect(() => {
        const timer = setTimeout(() => {
            if (isLoading) {
                setHasError(true);
                setIsLoading(false);
            }
        }, 8000);

        return () => clearTimeout(timer);
    }, [isLoading]);

    if (!lat || !lng) return null;

    return (
        <div className="relative h-full min-h-[130px] w-full rounded-xl overflow-hidden border border-gray-200 shadow-sm transition-all hover:shadow-md bg-gray-50 flex items-center justify-center">
            {isLoading && !hasError && <MapLoading />}
            {hasError && <MapError />}

            {!hasError && (
                <MapFrame
                    lat={lat}
                    lng={lng}
                    isLoading={isLoading}
                    onMapLoad={() => setIsLoading(false)}
                />
            )}
        </div>
    );
}
