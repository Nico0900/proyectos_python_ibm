def main():
    print("=== LISTA DE COMPRAS ===\n")
    
    # Lista para almacenar los productos
    productos = []
    
    # 1. Pedir al usuario el nombre y precio de 3 productos
    for i in range(3):
        print(f"Producto {i + 1}:")
        nombre = input("  Nombre del producto: ")
        while True:
            try:
                precio = float(input("  Precio del producto: $"))
                break
            except ValueError:
                print("  Por favor, ingresa un precio válido (número)")
        
        # 2. Guardar los datos en una estructura (diccionario)
        producto = {
            'nombre': nombre,
            'precio': precio
        }
        productos.append(producto)
        print()
    
    # 3. Calcular el total a pagar y determinar el producto más caro
    total = sum(producto['precio'] for producto in productos)
    producto_mas_caro = max(productos, key=lambda x: x['precio'])
    
    # 4. Mostrar la lista de productos, el total y cuál fue el producto de mayor costo
    print("=" * 40)
    print("RESUMEN DE LA COMPRA")
    print("=" * 40)
    
    print("\nLista de productos:")
    for i, producto in enumerate(productos, 1):
        print(f"{i}. {producto['nombre']}: ${producto['precio']:.2f}")
    
    print(f"\nTotal a pagar: ${total:.2f}")
    print(f"Producto más caro: {producto_mas_caro['nombre']} (${producto_mas_caro['precio']:.2f})")

if __name__ == "__main__":
    main()