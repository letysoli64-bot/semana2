texto = "Python2026"

if texto.isalnum():
    minusculas = texto.lower()
    separado = minusculas.replace("2026", "")
    print(separado)
else:
    print("No es alfanumérico")
