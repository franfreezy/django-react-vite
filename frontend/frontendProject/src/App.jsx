import { useState } from 'react'

import './App.css'
import 'vite/modulepreload-polyfill'

function App() {
  const [count, setCount] = useState(0)
  const reactLogo ='/static/react.svg'
  const viteLogo ='/static/vite.svg'
  const djangoLogo='/static/django.svg'
  const graphLogo='/static/GraphQL_Logo.svg'


  return (
    <>
      <div>
        <a href="https://vitejs.dev" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <a href="https://react.dev" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
        <a href="https://react.dev" target="_blank">
          <img src={djangoLogo} className="logo react" alt="django logo" />
        </a>
        <a href="https://react.dev" target="_blank">
          <img src={graphLogo} className="logo react" alt="django logo" />
        </a>
      </div>
      <h1>Vite + React + Django+ GraphQL</h1>
      <div className="card">
        <button onClick={() => setCount((count) => count + 1)}>
          count is {count}
        </button>
        <p>
          Edit <code>src/App.jsx</code> and save to test HMR
        </p>
      </div>
      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p>
    </>
  )
}

export default App
