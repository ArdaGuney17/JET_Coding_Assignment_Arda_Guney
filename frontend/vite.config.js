// Vite dependencies and plugins
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import tailwindcss from '@tailwindcss/vite'

/**
 * Vite Configuration
 * https://vite.dev/config/
 */
export default defineConfig({
  plugins: [
    // Enables React Fast Refresh and JSX support
    react(),

    // The official Tailwind CSS v4 Vite plugin. 
    // This provides lightning-fast CSS processing directly within the Vite build pipeline,
    // allowing for modern features like @import "tailwindcss" in our CSS files.
    tailwindcss(),
  ],
})