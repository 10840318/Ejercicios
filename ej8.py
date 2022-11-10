#!/usr/bin/env python3
"""
Autor : Brian Miró <10840318@iespenyagolosa.es>
Fecha   : 8/11/22
Propósito: Escribir una lista de números consecutivos
"""

numero=int(input('Dime un número positivo: '))
while numero<=0:
    print('¡Te he pedido un número positivo!')
    numero=int(input('Dime un número positivo: '))
for i in range(0,numero+1):
    print(i,end=', ')
print()
for j in range(numero,-1,-1):
    print(j,end=', ')
print()
for k in range(1,numero):
    print(k,end=', ')
print()
for l in range(numero-1,0,-1):
    print(l,end=', ')
print()
for m in range(0,numero+1):
    print(m,end=', ')
for n in range(numero-1,-1,-1):
   print(n,end=', ')
print()