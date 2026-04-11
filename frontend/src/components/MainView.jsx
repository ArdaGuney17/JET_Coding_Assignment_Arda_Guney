import { RestaurantListFrame } from './RestaurantList/RestaurantListFrame';
import { RestaurantPreviewCard } from './RestaurantList/RestaurantCard/RestaurantPreviewCard';

/**
 * LoadingState Component: Displays a professional loading spinner.
 */
function LoadingState() {
    return (
        <div className="flex flex-col items-center justify-center p-20 space-y-4">
            <div className="w-12 h-12 border-4 border-[#FF8000] border-t-transparent rounded-full animate-spin"></div>
            <p className="text-gray-500 font-medium animate-pulse">Fetching the best restaurants for you...</p>
        </div>
    );
}

/**
 * ErrorState Component: Displays a helpful error message when the API fails.
 */
function ErrorState({ message }) {
    return (
        <div className="max-w-[1000px] mx-auto p-10 mt-10 bg-red-50 border border-red-100 rounded-3xl text-center">
            <div className="text-4xl mb-4">⚠️</div>
            <h2 className="text-red-900 text-xl font-bold mb-2">Something went wrong</h2>
            <p className="text-red-600 mb-6">{message}</p>
            <button
                onClick={() => window.location.reload()}
                className="bg-red-600 text-white px-6 py-2 rounded-full font-bold hover:bg-red-700 transition-colors shadow-md"
            >
                Try Again
            </button>
        </div>
    );
}

/**
 * MainView Component: Orchestrates the high-level application states.
 */
export function MainView({ restaurants, loading, error }) {
    if (loading) return <LoadingState />;
    if (error) return <ErrorState message={error} />;

    return (
        <RestaurantListFrame>
            {restaurants.map((res, index) => (
                <RestaurantPreviewCard key={index} {...res} />
            ))}
        </RestaurantListFrame>
    );
}
