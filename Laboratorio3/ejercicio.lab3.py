# Ejericicio registro de ventas
total_general = 0

while True:
    print("\n--- REGISTRO DE VENTAS ---")

    cantidad = int(input("¿Cuántos productos desea registrar?: "))
    total_compra = 0

    # FOR: recorrer productos
    for i in range(cantidad):
        print(f"\nProducto {i+1}")
        nombre = input("Nombre: ")
        precio = float(input("Precio: $"))

        # IF: descuento
        if precio > 20:
            descuento = precio * 0.10
            precio_final = precio - descuento
            print(f"Descuento aplicado: ${descuento:.2f}")
        else:
            precio_final = precio
            print("Sin descuento")

        total_compra += precio_final

    # SELECT CASE
    print("\nTipo de cliente:")
    print("1. Regular")
    print("2. VIP")
    print("3. Mayorista")

    tipo = int(input("Seleccione opción: "))

    match tipo:
        case 1:
            print("Cliente Regular")
        case 2:
            descuento = total_compra * 0.05
            total_compra -= descuento
            print("Cliente VIP - 5% descuento")
        case 3:
            descuento = total_compra * 0.10
            total_compra -= descuento
            print("Cliente Mayorista - 10% descuento")
        case _:
            print("Opción inválida")

    print(f"\nTotal compra: ${total_compra:.2f}")
    total_general += total_compra

    continuar = input("\n¿Desea continuar? (s/n): ").lower()
    if continuar != "s":
        break

print(f"\nTOTAL GENERAL: ${total_general:.2f}")
