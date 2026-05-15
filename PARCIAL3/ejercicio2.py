from decimal import Decimal, InvalidOperation

total = Decimal("0")

while True:

    try:
        precio = input("Ingrese el precio del producto (0 para salir): ")

        precio_decimal = Decimal(precio)

        if precio_decimal == 0:
            break

        total += precio_decimal

    except InvalidOperation:
        print("Advertencia: Debe ingresar un número válido.")

print(f"Total acumulado: ${total}")
