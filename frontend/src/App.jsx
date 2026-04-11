// Import the Just Eat Takeaway logo from the assets folder
import jetLogo from './assets/jet-logo-white.png'
// Import the necessary components and hooks from their new dedicated directories
import { Header } from './components/Header'
import { MainView } from './components/MainView'
import { useRestaurants } from './hooks/useRestaurants'

/**
 * App Component
 * The entry point of the application. Highly declarative and orchestrates top-level pieces.
 */
function App() {
  const { restaurants, loading, error } = useRestaurants()

  return (
    <div className="min-h-screen bg-white font-sans">
      <Header logo={jetLogo} />
      <MainView
        restaurants={restaurants}
        loading={loading}
        error={error}
      />
    </div>
  )
}

export default App