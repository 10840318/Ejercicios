#!/usr/bin/env python3
"""
Autor : Brian Miró <10840318@iespenyagolosa.es>
Fecha   : 9/11/22
Propósito: Calcular factorial de un número
"""

numero=int(input('Dime un número: '))
factorial=1
for i in range(1,numero+1):
    factorial*=i
print(f'El factorial de {numero} es: {factorial}')