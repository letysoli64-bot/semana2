def transformar_palabra(palabra, numero):
    if numero == 1:
        print(palabra.upper())
    elif numero == 2:
        print(palabra.lower())
    elif numero == 3:
        print(palabra.capitalize())
    else:
        print("Opción inválida")
