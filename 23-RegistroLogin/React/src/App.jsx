import { useState, useEffect } from 'react'

function App() {
  const [count, setCount] = useState([])

  useEffect(() => {
    const consumirApi = async () => {
      const response = await fetch('http://127.0.0.1:8000/articulos');
      const respuesta = await response.json()

      console.log(respuesta)
    }

    consumirApi()
  }, [])

  return (
    <>
      <div className="App">
        <h1>Consumidor de React</h1>
    </div>
    </>
  )
}

export default App
