#!/usr/bin/env python3
"""
Autor : Brian Miró <10840318@iespenyagolosa.es>
Fecha   : 25/10/22
Propósito: Suma de cifras
"""

print('Suma de las cifras de un número')
numero=input('Dime un número: ')
lista=list(numero)
cifra1=int(numero[0])
cifra2=int(numero[1])
cifra3=int(numero[2])
cifra4=int(numero[3])
suma=cifra1+cifra2+cifra3+cifra4
print(f'La suma de las cifras del número {numero} es {suma}.')