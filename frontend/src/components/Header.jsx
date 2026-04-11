/**
 * NavBar Sub-Component: The sticky orange logo bar pinned to the top of the screen.
 */
// We add altText as a prop, but give it your current string as the default fallback
export function NavBar({ logo, altText = "Just Eat Takeaway Logo" }) {
    return (
        <header className="sticky top-0 z-50 bg-[#FF8000] py-3 shadow-md">
            <div className="px-5 md:px-8">
                <img
                    src={logo}
                    alt={altText}
                    className="h-10 md:h-12 object-contain"
                />
            </div>
        </header>
    );
}

/**
 * TitleSection Sub-Component: The editorial landing block with the assignment
 * title and description.
 */
function TitleSection() {
    return (
        <div className="px-5 md:px-8 mt-8 mb-2">
            <h1 className="text-gray-900 text-2xl md:text-4xl font-extrabold tracking-tight mb-2">
                Complete at Home <span className="text-[#FF8000]">Coding Assignment</span>
            </h1>
            <p className="text-gray-400 text-sm md:text-base leading-relaxed max-w-xl">
                Displaying the details of the first 10 restaurants dynamically fetched from the Just Eat Takeaway API.
            </p>
        </div>
    );
}

/**
 * Header Component: Composes NavBar and TitleSection.
 */
export function Header({ logo }) {
    return (
        <div className="bg-[#fafafa] pb-10 border-b border-gray-100">
            <NavBar logo={logo} />
            <TitleSection />
        </div>
    );
}
