def transformar_lista(lista, numero):
    nueva_lista = []

    for palabra in lista:
        if numero == 1:
            nueva_lista.append(palabra.upper())
        elif numero == 2:
            nueva_lista.append(palabra.lower())
        elif numero == 3:
            nueva_lista.append(palabra.capitalize())
        else:
            return "Opción inválida"

    return nueva_lista


lista = ["hola", "mundo", "python"]
print(transformar_lista(lista, 1))
