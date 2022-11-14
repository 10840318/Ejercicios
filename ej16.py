#!/usr/bin/env python3
"""
Autor : Brian Miró <10840318@iespenyagolosa.es>
Fecha   : 9/11/22
Propósito: Crear una lista de palabras e invertir orden
"""

palabras=int(input('Dime cuántas palabras tiene la lista: '))
lista=[]
for i in range(1,palabras+1):
    palabra=input(f'Dime la palabra {i}: ')
    lista.insert(i,palabra)
print(f'La lista creada es: {lista}')
lista.reverse()
lista_inversa=lista
print(f'La lista inversa es: {lista_inversa}')