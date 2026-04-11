import { Tag } from '../SharedComponents/Tag';

/* Icons needed for cuisines, rating, and address */
const ICONS = {
    cuisines: (
        <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5 mt-0.5 text-[#FF8000] shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M3 2v7c0 1.1.9 2 2 2h4a2 2 0 002-2V2M7 2v20M21 15V2a5 5 0 00-5 5v6c0 1.1.9 2 2 2h3zm0 0v7" />
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
            <div className="flex flex-wrap items-center gap-x-2 gap-y-1.5">
                {children}
            </div>
        </div>
    );
}

/**
 * CardDetails Component: Groups the list of detailed info about a restaurant.
 */
export function CardDetails({ cuisines, rating, address, specialties = [] }) {
    return (
        <div className="space-y-3 text-left flex-1 shrink-0">
            <DetailRow type="cuisines">
                <span className="font-bold whitespace-nowrap">Cuisines:</span>
                <span className="text-gray-600 font-medium" style={{ color: '#FF8000' }}>{cuisines || (specialties.length > 0 ? '' : 'Not specified')}</span>
                {specialties.map((spec, index) => (
                    <Tag key={index} text={spec} color="white" textColor="black" textTransform="none" borderStyle="border border-[#FF8000]" />
                ))}
            </DetailRow>
            <DetailRow type="rating"><span className="font-bold text-gray-900">Rating:</span> <span className="font-medium">{rating} / 5</span></DetailRow>
            <DetailRow type="address"><span className="font-bold">Address:</span> {address}</DetailRow>
        </div>
    );
}
