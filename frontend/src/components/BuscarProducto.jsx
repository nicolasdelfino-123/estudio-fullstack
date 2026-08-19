import { useState } from "react";

function BuscarProducto() {
    const [id, setId] = useState("")
    const [producto, setProducto] = useState(null)

    const API_URL = import.meta.env.VITE_API_URL;

    async function handleBuscar() {
        const response = await fetch(`${API_URL}/products/${id}`);
        const data = await response.json()
        console.log(data)
        setProducto(data)
    }

    return (< div >
        <h2>Buscar Producto</h2>
        <input
            type="text"
            value={id}
            onChange={(e) => setId(e.target.value)}
        />
        <button
            onClick={handleBuscar}
        >
            Buscar
        </button>
        {producto && (
            <div>
                <h2>Nombre: {producto.nombre}</h2>
                <h3>Precio: {producto.precio}</h3>
                <h3>Strock: {producto.stock}</h3>
            </div>
        )}
    </div >


    )
}

export default BuscarProducto;