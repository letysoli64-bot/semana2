archivo = "Sunombre.txt"
sin_txt = archivo.removesuffix(".txt")
sin_prefijo = sin_txt.removeprefix("ING. ")
resultado = sin_prefijo.lower()

print(resultado)
