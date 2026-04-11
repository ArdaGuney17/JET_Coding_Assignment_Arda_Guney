// Issue handled in RestaurantListFrame.jsx if no restaurant data retrieved.

export function EmptyState({
    icon = "🍽️",
    title = "No available deliciousness around you ;(",
    message = "It looks like we couldn't find any restaurants. Try adjusting your search or checking back later."
}) {
    return (
        <div className="flex flex-col items-center justify-center py-16 md:py-24 text-white text-center mt-4">
            <span className="text-6xl mb-4">{icon}</span>
            <h2 className="text-2xl md:text-3xl font-black tracking-wide mb-2">
                {title}
            </h2>
            <p className="text-lg text-white/90 font-medium max-w-md">
                {message}
            </p>
        </div>
    );
}