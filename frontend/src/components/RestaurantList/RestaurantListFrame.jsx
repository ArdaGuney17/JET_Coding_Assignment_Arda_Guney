import React from 'react';
import { Tag } from './SharedComponents/Tag';

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

                {/* 2. Conditional Rendering: Show Empty State OR the Restaurant List */}
                {isEmpty ? (
                    <div className="flex flex-col items-center justify-center py-16 md:py-24 text-white text-center mt-4">
                        {/* You can replace this emoji with your ForkIcon if you prefer! */}
                        <span className="text-6xl mb-4">🍽️</span>
                        <h2 className="text-2xl md:text-3xl font-black tracking-wide mb-2">
                            No available deliciousness around you!
                        </h2>
                        <p className="text-lg text-white/90 font-medium max-w-md">
                            It looks like we couldn't find any restaurants. Try adjusting your search or checking back later.
                        </p>
                    </div>
                ) : (
                    <ul className="list-none p-0 space-y-6 md:space-y-8 mt-4 md:mt-2">
                        {children}
                    </ul>
                )}
            </div>
        </main>
    );
}