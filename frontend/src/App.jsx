import { useState } from "react";
import BuscarProducto from "./components/BuscarProducto";
function App() {
    const [nombre, setNombre] = useState("");
    const [precio, setPrecio] = useState("");
    const [stock, setStock] = useState("");


    const API_URL = import.meta.env.VITE_API_URL;

    async function handleSubmit() {
        const producto = {
            nombre,
            precio,
            stock
        };

        const response = await fetch(`${API_URL}/products`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(producto)
        });

        const data = await response.json()
        console.log(data)
    }


    return (
        <div>
            <h1>Productos</h1>
            <BuscarProducto />
            <label htmlFor="">Nombre</label>
            <input
                type="text"
                value={nombre}
                onChange={(e) => setNombre(e.target.value)}
            />

            <label htmlFor="">precio</label>
            <input
                type="number"
                value={precio}
                onChange={(e) => setPrecio(e.target.value)}
            />

            <label htmlFor="">stock</label>
            <input
                type="number"
                value={stock}
                onChange={(e) => setStock(e.target.value)}
            />
            <button
                onClick={handleSubmit}
            >
                Crear prodcuto
            </button>

        </div>
    )
}

export default App;