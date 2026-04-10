/**
 * Tag Sub-Component: Small branded badge for promotions.
 */
function Tag({ text }) {
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

/**
 * CardHeader Component: Displays the restaurant name and its tags.
 */
export function CardHeader({ name, tags }) {
    return (
        <div className="flex justify-between items-start mb-3 gap-4">
            <h3 className="text-2xl font-bold text-[#FF8000] text-left m-0">
                {name}
            </h3>
            {tags && tags.length > 0 && (
                <div className="flex flex-wrap justify-end gap-2 shrink-0">
                    {tags.map((tag, index) => (
                        <Tag key={index} text={tag} />
                    ))}
                </div>
            )}
        </div>
    );
}
