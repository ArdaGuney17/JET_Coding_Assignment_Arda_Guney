export function Tag({
    text,
    color = "bg-gradient-to-r from-[#FF8000] to-orange-400",
    textColor = "text-white",
    textTransform = "uppercase",          // Parameterized: defaults to all-caps
    borderStyle = "border border-white/20" // Parameterized: defaults to current frame
}) {
    const getIcon = (tagStr) => {
        if (!tagStr || typeof tagStr !== 'string') return null;
        const lower = tagStr.toLowerCase();
        if (lower.includes('ranking')) return '🏆';
        if (lower.includes('freebies')) return '🎁';
        if (lower.includes('deals') || lower.includes('offers')) return '🔥';
        if (lower.includes('stamps')) return '🎟️';
        return null;
    };

    return (
        <span className={`
            inline-flex items-center gap-1.5 
            ${color} ${textColor} ${textTransform} ${borderStyle}
            text-[11px] px-3.5 py-1.5 
            rounded-xl font-black shadow-md 
            tracking-widest 
            transition-all duration-300 hover:scale-105
        `}>
            {getIcon(text) && <span className="text-sm">{getIcon(text)}</span>}
            {text}
        </span>
    );
}