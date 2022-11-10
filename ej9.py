#!/usr/bin/env python3
"""
Autor : Brian Miró <10840318@iespenyagolosa.es>
Fecha   : 8/11/22
Propósito: Escribir una lista de números pares
"""

valor_i=int(input('Dime el valor inicial: '))
valor_f=int(input('Dime el valor final: '))

while valor_i>=valor_f:
    print('El valor final no es mayor que el valor inicial')
    valor_f=int(input('Dime el valor final: '))

for i in range(valor_i,valor_f+1):
    if i%2==0:
        print(i,end=', ')
print()