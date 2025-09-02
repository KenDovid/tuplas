# funciones.py
from productos import productos

def supermercado():
    print("¡Bienvenido al Supermercado Verdulero!")
    print("=== Catálogo de productos ===")
    for codigo, (nombre, precio) in productos.items():
        print(f"{codigo}. {nombre} - {precio}$")
    print("=============================")

    carrito = {}
    seguir = "s"

    while seguir.lower() == "s":
        opcion = int(input("Seleccione el número del producto: "))
        if opcion in productos:
            nombre, precio = productos[opcion]
            unidades = int(input(f"¿Cuántos {nombre} llevará? "))
            carrito[opcion] = carrito.get(opcion, 0) + unidades
        else:
            print("Opción inválida.")
        seguir = input("¿Desea comprar otro producto? (s/n): ")

    print("\n=== Factura Electrónica ===")
    subtotal = 0
    for codigo, unidades in carrito.items():
        nombre, precio = productos[codigo]
        total_producto = unidades * precio
        subtotal += total_producto
        print(f"{nombre}: {unidades} x {precio}$ = {total_producto}$")

    iva = subtotal * 0.19
    total = subtotal + iva

    print("=============================")
    print(f"Subtotal: {subtotal}$")
    print(f"IVA (19%): {iva:.2f}$")
    print(f"Total a pagar: {total:.2f}$")
