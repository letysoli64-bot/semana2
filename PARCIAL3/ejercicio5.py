nombre_completo = input("Ingrese su nombre y apellido: ")

# Convertir en lista
lista_nombre = nombre_completo.split()

# Invertir usando slicing
lista_invertida = lista_nombre[::-1]

# Recorrer palabras
for palabra in lista_invertida:

    # Recorrer letras
    for letra in palabra:
        print(letra, end=".")
        print()
