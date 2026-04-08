def transformar_y_contar(texto, numero):
    if numero == 1:
        resultado = texto.upper()
    elif numero == 2:
        resultado = texto.lower()
    elif numero == 3:
        resultado = texto.capitalize()
    else:
        return "Opción inválida"

    return len(resultado)


print(transformar_y_contar("hola mundo", 1))
