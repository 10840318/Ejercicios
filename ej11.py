#!/usr/bin/env python3
"""
Autor : Brian Miró <10840318@iespenyagolosa.es>
Fecha   : 9/11/22
Propósito: Escribir mayor, menor y media
"""

valores=int(input('¿Cuántos valores vas a introducir?: '))
media=0
minimo=1000000000000000000000
maximo=0
for i in range(1,valores+1):
    numero=int(input(f'Dime el número {i}: '))
    media+=numero
    if numero<minimo:
        minimo=numero
    elif numero>maximo:
        maximo=numero
media/=valores
print(f'El número más pequeño de los introducidos es: {minimo}')
print(f'El número más grande de los introducidos es: {maximo}')
print(f'La media de los números introducidos es: {media}')