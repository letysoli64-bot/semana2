Algoritmo NumeroNegativo_Y_SumaDeLosPositivos
	
	Definir numx, suma Como Entero
	suma <-0
	Repetir
		escribir "Ingrese un numero"
		Leer numx
		Si numx>= 0 Entonces
			suma<- suma + numx
			
		FinSi
		
	Hasta Que numx<=0
	
	Escribir " La suma de los positivos es:", suma
	
	
FinAlgoritmo
