texto = "Su nombre"
normalizado = texto.casefold().replace(" ", "")
es_letras = normalizado.isalpha()

print(normalizado)
print(es_letras)
