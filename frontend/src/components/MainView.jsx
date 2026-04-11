import { RestaurantListFrame } from './RestaurantList/RestaurantListFrame';
import { RestaurantPreviewCard } from './RestaurantList/RestaurantCards/RestaurantPreviewCard';
import { FallbackRestaurantCard } from './RestaurantList/RestaurantCards/ErrorStatesCards/FallbackRestaurantCard';
import { APIFetchError } from './RestaurantList/ErrorStatesList/APIFetchError';
import { JETFetchLoader } from './RestaurantList/LoaderList/JETFetchLoader';

/**
 * MainView Component: Orchestrates the high-level application states.
 */
export function MainView({ restaurants, loading, error }) {
    if (loading) return <JETFetchLoader />;
    if (error) return <APIFetchError message={error} />;

    const restaurantList = Array.isArray(restaurants) ? restaurants : [];
    /*const testData = [
        ...restaurants,
        {
            name: "Pizeraaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            cuisines: "Mexican",
            specialties: null,
            address: null,
            rating: null,
            lat: "arxda",
            lng: null
        }
    ];*/

    return (
        <RestaurantListFrame>
            {restaurantList.map((restaurant, index) => {
                // If the restaurant object is missing or has no name, render a fallback card
                if (!restaurant || !restaurant.name) {
                    return <FallbackRestaurantCard key={`fallback-${index}`} />;
                }

                // Otherwise, render the normal card
                // Using name + index since the backend doesn't provide a unique ID field
                return <RestaurantPreviewCard key={`${restaurant.name}-${index}`} {...restaurant} />;
            })}
        </RestaurantListFrame>
    );
}
