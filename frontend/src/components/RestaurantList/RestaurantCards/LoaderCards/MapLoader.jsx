/**
 * MapLoader Component
 * Displays the branded Just Eat spinner specifically scaled for the MiniMap.
 */
export function MapLoader() {
    return (
        <div className="absolute inset-0 flex flex-col items-center justify-center bg-gray-50 z-10 transition-opacity duration-300">
            <div className="w-6 h-6 border-2 border-[#FF8000] border-t-transparent rounded-full animate-spin mb-2"></div>
            <span className="text-[10px] text-gray-400 font-medium uppercase tracking-widest">
                Loading Map
            </span>
        </div>
    );
}