#!/usr/bin/env python3
"""
Autor : Brian Miró <10840318@iespenyagolosa.es>
Fecha   : 9/11/22
Propósito: Divisores de un número
"""

numero_final= int(input('Dime un número: '))
lista=[]

if numero_final < 2: #si es menor de 2 no es primo, devolverá Falso
   print('Por definición los números primos empiezan con el 2.')
else:
	
	for i in range(1, numero_final+1): 
		es_primo = True
		for j in range(2,i): #un bucle desde el 2 hasta el numero en cada pasada del bucle
			if (i % j) == 0: #si el resto da 0 no es primo, rompemos el bucle para no continuar
				es_primo = False
				break
		if es_primo:
			lista.append(i)
	
	print (f'Primos hasta {numero_final}: {lista}')