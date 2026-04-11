import { MiniMapConfig } from '../../../../../config/MiniMapConfig';

/**
 * MiniMapFrame Component
 * Contains the Google Maps iframe with smooth fade-in logic.
 */
export function MiniMapFrame({ lat, lng, isLoading, onMapLoad }) {
    return (
        <iframe
            title="Restaurant Location Map"
            width="100%"
            height="100%"
            style={{ border: 0 }}
            loading="lazy"
            allowFullScreen
            referrerPolicy="no-referrer-when-downgrade"
            src={`${MiniMapConfig.MAPS_BASE_URL}?q=${lat},${lng}&z=${MiniMapConfig.MAPS_DEFAULT_ZOOM}&output=embed`}
            onLoad={onMapLoad}
            className={`transition-opacity duration-500 ${isLoading ? 'opacity-0' : 'opacity-100'}`}
        ></iframe>
    );
}