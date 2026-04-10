// File that contains the components used in the application to enable better readability and reusability

/**
 * Header Component displays the brand logo and assignment titles.
 * sticky ensures the brand remains visible while scrolling.
 * Has the JET Orange #FF8000 color scheme to match the brand identity.
 * max-w-[1000px] max width to match the list and keeps the header from getting too wide on large screens.
 * mx-auto centers this frame horizontally.
 */
export function Header({ logo }) {
    return (

        <div className="sticky top-0 z-50 bg-white pb-4">
            <header className="bg-[#FF8000] py-4 shadow-sm">
                <div className="max-w-[1000px] mx-auto px-5">
                    <img
                        src={logo}
                        alt="Just Eat Takeaway Logo"
                        className="h-28 mx-auto object-contain"
                    />
                </div>
            </header>

            <div className="max-w-[1000px] mx-auto px-5 mt-6">
                <h1 className="text-[#FF8000] text-2xl md:text-4xl font-bold text-center">
                    Complete at Home Coding Assignment
                </h1>
                <p className="text-[#FF8000] text-center opacity-90">
                    Displaying the details of the first 10 restaurants fetched from the Just Eat Takeaway API
                </p>
            </div>
        </div>
    );
}

/**
 * RestaurantList Component a scrollable container that maps the 
 * restaurant data into individual cards.
 * max-w-[1000px] max width to match the header and keeps the list from getting too wide on large screens.
 * max-h-[calc(100vh-320px)] max height to ensure the list doesn't cover the entire screen and allows for scrolling.
 * overflow-y-auto pr-4 border-2 border-gray-100 rounded-2xl p-6 shadow-md to ensure the list is scrollable and has a border and shadow.
 * mx-auto centers this frame horizontally.
 */
export function RestaurantList({ children }) {
    return (
        <main className="max-w-[1000px] mx-auto p-5 pt-4">
            <div className="bg-[#FF8000] max-h-[calc(100vh-320px)] overflow-y-auto pr-4 border-2 border-gray-100 rounded-2xl p-6 shadow-md">
                <ul className="list-none p-0 space-y-4">
                    {children}
                </ul>
            </div>
        </main>
    );
}

/**
 * Tag Component displays a small visual indicator for marketing tags.
 */
export function Tag({ text }) {
    // Dynamically assign a fun emoji based on what kind of promotion it is!
    const getIcon = (tagStr) => {
        const lower = tagStr.toLowerCase();
        if (lower.includes('freebies')) return '🎁';
        if (lower.includes('deals') || lower.includes('offers')) return '🔥';
        if (lower.includes('stamps')) return '🎟️';
        return '✨';
    };

    return (
        <span className="inline-flex items-center gap-1.5 bg-gradient-to-r from-[#FF8000] to-orange-400 text-white text-[11px] px-3 py-1.5 rounded-lg font-extrabold shadow-sm uppercase tracking-wider border border-orange-300/50">
            <span className="text-sm">{getIcon(text)}</span>
            {text}
        </span>
    );
}

// MiniMap component to display the location of the restaurant
export function MiniMap({ lat, lng }) {
    // Safety guard: Don't render anything if coordinates are missing
    if (!lat || !lng) return null;

    return (
        <div className="h-full min-h-[130px] w-full rounded-xl overflow-hidden border border-gray-200 shadow-sm transition-all hover:shadow-md">
            <iframe
                width="100%"
                height="100%"
                style={{ border: 0 }}
                loading="lazy"
                allowFullScreen
                referrerPolicy="no-referrer-when-downgrade"
                src={`https://maps.google.com/maps?q=${lat},${lng}&z=15&output=embed`}
            ></iframe>
        </div>
    );
}

/**
 * RestaurantCard Component displays the four mandatory data points: 
 * Name, Cuisines, Rating, and Address.
 * bg-white border-2 border-gray-100 rounded-2xl p-6 shadow-md to ensure the card has a border and shadow.
 * transition-transform hover:scale-[1.01] to ensure the card scales up when hovered over.
 */
export function RestaurantCard({ name, cuisines, rating, address, tags = [], lat, lng }) {
    return (
        <li className="bg-white border-2 border-gray-100 rounded-2xl p-6 shadow-md transition-transform hover:scale-[1.01]">
            {/* Name and Tags are grouped in a flex container to align them left and right respectively */}
            <div className="flex justify-between items-start mb-3 gap-4">
                <h3 className="text-2xl font-bold text-[#FF8000] text-left m-0">
                    {name}
                </h3>

                {/* Display Tags if there are any, wrapped securely on the right */}
                {tags && tags.length > 0 && (
                    <div className="flex flex-wrap justify-end gap-2 shrink-0">
                        {tags.map((tag, index) => (
                            <Tag key={index} text={tag} />
                        ))}
                    </div>
                )}
            </div>

            <div className="mt-4 border-t border-gray-100 pt-4 flex flex-col md:flex-row gap-5 items-stretch justify-between">
                <div className="space-y-3 text-left flex-1 shrink-0">
                    <div className="flex items-start gap-2.5 text-gray-700">
                        {/* Utensils / Burger Icon */}
                        <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5 mt-0.5 text-[#FF8000] shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M21 15.546c-.523 0-1.046.151-1.5.454a2.704 2.704 0 01-3 0 2.704 2.704 0 00-3 0 2.704 2.704 0 01-3 0 2.704 2.704 0 00-3 0 2.704 2.704 0 01-3 0 2.701 2.701 0 00-1.5-.454M9 6v2m3-2v2m3-2v2M9 3h.01M12 3h.01M15 3h.01M21 21v-7a2 2 0 00-2-2H5a2 2 0 00-2 2v7h18zm-3-9v-2a2 2 0 00-2-2H8a2 2 0 00-2 2v2h12z" />
                        </svg>
                        <p>
                            <span className="font-bold">Cuisines:</span> {cuisines}
                        </p>
                    </div>

                    <div className="flex items-start gap-2.5 text-gray-700">
                        {/* Solid Star Icon */}
                        <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5 mt-0.5 text-[#FF8000] shrink-0" fill="currentColor" viewBox="0 0 24 24">
                            <path d="M11.049 2.927c.3-.921 1.603-.921 1.902 0l1.519 4.674a1 1 0 00.95.69h4.915c.969 0 1.371 1.24.588 1.81l-3.976 2.888a1 1 0 00-.363 1.118l1.518 4.674c.3.922-.755 1.688-1.538 1.118l-3.976-2.888a1 1 0 00-1.176 0l-3.976 2.888c-.783.57-1.838-.197-1.538-1.118l1.518-4.674a1 1 0 00-.363-1.118l-3.976-2.888c-.784-.57-.38-1.81.588-1.81h4.914a1 1 0 00.951-.69l1.519-4.674z" />
                        </svg>
                        <p>
                            <span className="font-bold text-gray-900">Rating:</span> <span className="font-medium">{rating} / 5</span>
                        </p>
                    </div>

                    <div className="flex items-start gap-2.5 text-gray-700">
                        {/* Map Pin Icon */}
                        <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5 mt-0.5 text-[#FF8000] shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.242-4.243a8 8 0 1111.314 0z" />
                            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15 11a3 3 0 11-6 0 3 3 0 016 0z" />
                        </svg>
                        <p>
                            <span className="font-bold">Address:</span> {address}
                        </p>
                    </div>
                </div>

                {/* MiniMap component perfectly aligned flush to the right */}
                <div className="w-full md:w-[250px] lg:w-[320px] shrink-0">
                    <MiniMap lat={lat} lng={lng} />
                </div>
            </div>
        </li>
    );
}

