#!/usr/bin/env python3
"""
Autor : Brian Miró <10840318@iespenyagolosa.es>
Fecha   : 9/11/22
Propósito: Divisores de un número
"""

NUMERO=int(input('Dime un número: '))
numero=NUMERO
divisores=0
lista=[]
for i in range(1,numero+1):
    if numero%i==0:
        divisores+=1
        lista.insert(i,i)
print(f'{NUMERO} tiene {divisores} divisores: {lista}')