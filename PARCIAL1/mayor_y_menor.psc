
	Algoritmo mayor_y_menor
		Definir num1, num2 Como Entero
		
		Escribir "Ingrese el primer numero:"
		Leer num1
		
		Escribir "Ingrese el segundo numero:"
		Leer num2
		
		Si num1 > num2 Entonces
			Escribir "Mayor: ", num1
			Escribir "Menor: ", num2
		Sino
			Si num2 > num1 Entonces
				Escribir "Mayor: ", num2
				Escribir "Menor: ", num1
			Sino
				Escribir "Los numeros son iguales"
			FinSi
		FinSi
FinAlgoritmo

