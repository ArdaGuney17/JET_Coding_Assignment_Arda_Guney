import React from 'react';
import { Tag } from './SharedComponentsWithCards/Tag';
import { EmptyState } from './ErrorStatesList/RestaurantListEmpty';

/**
 * RestaurantListFrame Component: A branded frame in the JET Orange color for the restaurant cards.
 */
export function RestaurantListFrame({ children }) {
    // 1. Safely check if we have zero restaurant cards passed in
    const isEmpty = React.Children.count(children) === 0;

    return (
        <main className="px-5 md:px-8 py-8 min-h-screen">
            <div className="border-2 border-[#FF8000] rounded-3xl p-5 md:p-8 shadow-2xl bg-[#FF8000] relative">
                <div className="absolute -top-5 left-6 md:left-12 transform hover:-translate-y-1 transition-transform duration-300">
                    <Tag
                        text="Sorted by Ranking"
                        color="bg-white/90 backdrop-blur-xl"
                        textColor="text-[#FF8000]"
                    />
                </div>

                {/* Look how clean this logic is now! */}
                {isEmpty ? (
                    <EmptyState />
                ) : (
                    <ul className="list-none p-0 space-y-6 md:space-y-8 mt-4 md:mt-2">
                        {children}
                    </ul>
                )}
            </div>
        </main>
    );
}