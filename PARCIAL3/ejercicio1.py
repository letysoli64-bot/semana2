etiqueta = input("Ingrese la etiqueta de rastreo: ")

if etiqueta == "" or etiqueta is None:
    print("Error: La etiqueta está vacía.")
else:
    try:

        partes = etiqueta.split("-")

        categoria = partes[1]

        print(f"Categoría: {categoria}")

        ruta = "Ruta Local" if etiqueta.endswith("SV") else "Ruta Internacional"

        print(ruta)

    except IndexError:
        print("Error: Formato incorrecto.")
