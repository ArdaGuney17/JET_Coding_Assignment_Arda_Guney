/**
 * JETFetchLoader Component
 * Displays a branded Just Eat orange spinner during initial API requests.
 */
export function JETFetchLoader() {
    return (
        <div className="flex flex-col items-center justify-center p-20 space-y-4">
            <div className="w-12 h-12 border-4 border-[#FF8000] border-t-transparent rounded-full animate-spin"></div>
            <p className="text-gray-500 font-medium animate-pulse">
                Fetching the best restaurants for you...
            </p>
        </div>
    );
}