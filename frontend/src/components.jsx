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
 * RestaurantCard Component displays the four mandatory data points: 
 * Name, Cuisines, Rating, and Address.
 * bg-white border-2 border-gray-100 rounded-2xl p-6 shadow-md to ensure the card has a border and shadow.
 * transition-transform hover:scale-[1.01] to ensure the card scales up when hovered over.
 */
export function RestaurantCard({ name, cuisines, rating, address }) {
    return (
        <li className="bg-white border-2 border-gray-100 rounded-2xl p-6 shadow-md transition-transform hover:scale-[1.01]">
            <h3 className="text-2xl font-bold text-[#FF8000] mb-3 text-left">
                {name}
            </h3>
            <div className="space-y-1 text-left">
                <p className="text-gray-700">
                    <span className="font-bold">Cuisines:</span> {cuisines}
                </p>
                <p className="text-gray-700">
                    <span className="font-bold">Rating:</span> {rating}
                </p>
                <p className="text-gray-700">
                    <span className="font-bold">Address:</span> {address}
                </p>
            </div>
        </li>
    );
}

