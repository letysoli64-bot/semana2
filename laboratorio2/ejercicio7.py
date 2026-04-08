def transformar_multiple(texto, lista_numeros):
    for numero in lista_numeros:
        if numero == 1:
            texto = texto.upper()
        elif numero == 2:
            texto = texto.lower()
        elif numero == 3:
            texto = texto.capitalize()
        else:
            return "Opción inválida"
    return texto


print(transformar_multiple("hola mundo", [1, 2, 3]))
