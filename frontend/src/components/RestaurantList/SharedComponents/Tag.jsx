/**
 * Tag Sub-Component: Small branded badge for promotions or status.
 */
export function Tag({ 
    text, 
    color = "bg-gradient-to-r from-[#FF8000] to-orange-400", 
    textColor = "text-white" 
}) {
    const getIcon = (tagStr) => {
        const lower = tagStr.toLowerCase();
        if (lower.includes('ranking')) return '🏆';
        if (lower.includes('freebies')) return '🎁';
        if (lower.includes('deals') || lower.includes('offers')) return '🔥';
        if (lower.includes('stamps')) return '🎟️';
        return '✨';
    };

    return (
        <span className={`
            inline-flex items-center gap-1.5 
            ${color} ${textColor} 
            text-[11px] px-3.5 py-1.5 
            rounded-xl font-black shadow-md 
            uppercase tracking-widest 
            border border-white/20
            transition-all duration-300 hover:scale-105
        `}>
            <span className="text-sm">{getIcon(text)}</span>
            {text}
        </span>
    );
}
