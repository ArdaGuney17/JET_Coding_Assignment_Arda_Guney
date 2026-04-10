/**
 * RestaurantList Component: A branded frame for the restaurant cards.
 */
export function RestaurantList({ children }) {
    return (
        <main className="px-5 md:px-8 py-8 min-h-screen">
            <div className="border-2 border-[#FF8000] rounded-3xl p-5 md:p-8 shadow-lg bg-[#FF8000]">
                <ul className="list-none p-0 space-y-6 md:space-y-8">
                    {children}
                </ul>
            </div>
        </main>
    );
}
