def transformar_texto(texto, numero):
    if numero == 1:
        return texto.upper()
    elif numero == 2:
        return texto.lower()
    elif numero == 3:
        return texto.capitalize()
    else:
        return "Opción inválida"


texto = input("Ingresa un texto: ")

try:
    numero = int(input("Ingresa una opción (1, 2, 3): "))
except:
    print("Debes ingresar un número")
    numero = 0

resultado = transformar_texto(texto, numero)
print("Resultado:", resultado)
