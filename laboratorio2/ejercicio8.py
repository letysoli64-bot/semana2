def transformar_texto(texto, numero):
    if numero == 1:
        return texto.upper()
    elif numero == 2:
        return texto.lower()
    elif numero == 3:
        return texto.capitalize()
    else:
        return "Opción inválida"


while True:
    print("\n1. Mayúsculas")
    print("2. Minúsculas")
    print("3. Primera letra mayúscula")
    print("4. Salir")

    try:
        opcion = int(input("Elige una opción: "))
    except:
        print("Debes ingresar un número")
        continue

    if opcion == 4:
        print("Programa finalizado")
        break

    texto = input("Ingresa un texto: ")
    resultado = transformar_texto(texto, opcion)
    print("Resultado:", resultado)
