#!/usr/bin/env python3
"""
Autor : Brian Miró <10840318@iespenyagolosa.es>
Fecha   : 9/11/22
Propósito: Cambiar vocales de una frase
"""

frase=input('Dime algo: ')
vocal=input('Dime una vocal: ')
VOCALES='aeiou'
while vocal not in VOCALES:
    vocal=input('No es una vocal, dime una vocal: ')
for i in range(len(frase)):
    if frase[i] in VOCALES:
        frase=frase.replace(frase[i],vocal)
print(f'La frase es ahora: {frase}')