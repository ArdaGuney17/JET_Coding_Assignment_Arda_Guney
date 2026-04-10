/* Icons needed for cuisines, rating, and address */
const ICONS = {
    cuisines: (
        <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5 mt-0.5 text-[#FF8000] shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M21 15.546c-.523 0-1.046.151-1.5.454a2.704 2.704 0 01-3 0 2.704 2.704 0 00-3 0 2.704 2.704 0 00-3 0 2.704 2.704 0 01-3 0 2.704 2.704 0 00-3 0 2.704 2.704 0 01-3 0 2.701 2.701 0 00-1.5-.454M9 6v2m3-2v2m3-2v2M9 3h.01M12 3h.01M15 3h.01M21 21v-7a2 2 0 00-2-2H5a2 2 0 00-2 2v7h18zm-3-9v-2a2 2 0 00-2-2H8a2 2 0 00-2 2v2h12z" />
        </svg>
    ),
    rating: (
        <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5 mt-0.5 text-[#FF8000] shrink-0" fill="currentColor" viewBox="0 0 24 24">
            <path d="M11.049 2.927c.3-.921 1.603-.921 1.902 0l1.519 4.674a1 1 0 00.95.69h4.915c.969 0 1.371 1.24.588 1.81l-3.976 2.888a1 1 0 00-.363 1.118l1.518 4.674c.3.922-.755 1.688-1.538 1.118l-3.976-2.888a1 1 0 00-1.176 0l-3.976 2.888c-.783.57-1.838-.197-1.538-1.118l1.518-4.674a1 1 0 00-.363-1.118l-3.976-2.888c-.784-.57-.38-1.81.588-1.81h4.914a1 1 0 00.951-.69l1.519-4.674z" />
        </svg>
    ),
    address: (
        <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5 mt-0.5 text-[#FF8000] shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.242-4.243a8 8 0 1111.314 0z" />
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15 11a3 3 0 11-6 0 3 3 0 016 0z" />
        </svg>
    ),
};

/**
 * DetailRow Sub-Component: Minimal row for cuisines, rating, and address.
 */
function DetailRow({ type, children }) {
    return (
        <div className="flex items-start gap-2.5 text-gray-700">
            {ICONS[type]}
            <p>{children}</p>
        </div>
    );
}

/**
 * CardDetails Component: Groups the list of detailed info about a restaurant.
 */
export function CardDetails({ cuisines, rating, address }) {
    return (
        <div className="space-y-3 text-left flex-1 shrink-0">
            <DetailRow type="cuisines"><span className="font-bold">Cuisines:</span> {cuisines}</DetailRow>
            <DetailRow type="rating"><span className="font-bold text-gray-900">Rating:</span> <span className="font-medium">{rating} / 5</span></DetailRow>
            <DetailRow type="address"><span className="font-bold">Address:</span> {address}</DetailRow>
        </div>
    );
}
