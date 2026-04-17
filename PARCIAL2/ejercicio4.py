texto = "CANTANDO"
minusculas = texto.lower()
sin_sufijo = minusculas.removesuffix("ando")
indice_t = sin_sufijo.find("t")

print(sin_sufijo)
print(indice_t)
