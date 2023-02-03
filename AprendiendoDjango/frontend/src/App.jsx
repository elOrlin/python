import React, {useEffect, useState, Fragment} from 'react';

function App() {

  const [guardar, setGuardar] = useState([])

  useEffect(() => {
    const consumirApi = async () => {
      const response = await fetch("http://127.0.0.1:8000/articulos/")
      const respuesta = await response.json()

      setGuardar([respuesta])
    }
    consumirApi()
  }, [guardar])

  return (
    <Fragment>
      <div>
        <h1>Listado desde la base de datos con Django</h1>
      </div>
    </Fragment>
  )
}

export default App
