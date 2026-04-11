// src/components/ErrorStatesCards/FallbackRestaurantCard.jsx

/**
 * FallbackRestaurantCard
 * * WHAT IT FIXES: 
 * Prevents app crashes (TypeErrors) when a restaurant data object is completely 
 * malformed, null, or missing critical rendering data from the API.
 * It provides a graceful UI degradation instead of breaking the entire list loop.
 */
export function FallbackRestaurantCard() {
    return (
        <li className="bg-gray-50 border-2 border-gray-200 dashed rounded-2xl p-6 shadow-sm opacity-70">
            <div className="flex flex-col items-center justify-center h-full py-8 text-center text-gray-400">
                <span className="text-3xl mb-2">⚠️</span>
                <h3 className="font-bold text-gray-500 mb-1">
                    Restaurant Unavailable
                </h3>
                <p className="text-sm">
                    We're having trouble loading the details for this spot.
                </p>
            </div>
        </li>
    );
}