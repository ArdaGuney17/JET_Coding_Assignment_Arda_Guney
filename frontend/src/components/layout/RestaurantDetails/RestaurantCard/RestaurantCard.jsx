import { CardHeader } from './CardHeader';
import { CardDetails } from './CardDetails';
import { MiniMap } from './MiniMap';

/**
 * RestaurantCard Component: Displays individual restaurant details.
 * Completely modularized into CardHeader, CardDetails, and MiniMaporganisms.
 */
export function RestaurantCard({ name, cuisines, rating, address, tags = [], lat, lng }) {
    return (
        <li className="bg-white border-2 border-gray-100 rounded-2xl p-6 shadow-md transition-transform hover:scale-[1.01]">
            <CardHeader name={name} tags={tags} />
            <div className="mt-4 border-t border-gray-100 pt-4 flex flex-col md:flex-row gap-5 items-stretch justify-between">
                <CardDetails cuisines={cuisines} rating={rating} address={address} />
                <div className="w-full md:w-[280px] lg:w-[380px] xl:w-[450px] shrink-0">
                    <MiniMap lat={lat} lng={lng} />
                </div>
            </div>
        </li>
    );
}
