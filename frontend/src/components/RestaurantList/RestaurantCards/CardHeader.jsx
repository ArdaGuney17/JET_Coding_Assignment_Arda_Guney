import { Tag } from '../SharedComponents/Tag';

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
