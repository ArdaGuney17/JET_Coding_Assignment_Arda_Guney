/**
 * APIFetchError Component
 * * WHAT IT FIXES: 
 * Handles global network failures or 500-level backend errors when fetching the initial restaurant list.
 * Prevents a blank screen when the API goes down and provides a recovery action (Try Again).
 */
export function APIFetchError({ message }) {
    // Adding defensive fallback for the message just in case the error object is weird
    const safeMessage = typeof message === 'string' ? message : "We couldn't connect to the server.";

    return (
        <div className="max-w-[1000px] mx-auto p-10 mt-10 bg-red-50 border border-red-100 rounded-3xl text-center">
            <div className="text-4xl mb-4">⚠️</div>
            <h2 className="text-red-900 text-xl font-bold mb-2">Something went wrong</h2>
            <p className="text-red-600 mb-6">{safeMessage}</p>
            <button
                onClick={() => window.location.reload()}
                className="bg-red-600 text-white px-6 py-2 rounded-full font-bold hover:bg-red-700 transition-colors shadow-md"
            >
                Try Again
            </button>
        </div>
    );
}