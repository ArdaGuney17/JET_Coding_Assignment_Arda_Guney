/**
 * MapErrorState Component
 * * WHAT IT FIXES: 
 * Handles timeouts or network failures when the Google Maps iframe takes too long to load.
 */
export function MapErrorState() {
    return (
        <div className="absolute inset-0 flex flex-col items-center justify-center bg-gray-50 z-10 p-4 text-center">
            <span className="text-xl mb-1">📍</span>
            <span className="text-[10px] text-gray-500 font-bold uppercase tracking-wider mb-1">
                Map Unavailable
            </span>
            <span className="text-[9px] text-gray-400 leading-tight">
                Check your connection or try again later
            </span>
        </div>
    );
}