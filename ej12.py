#!/usr/bin/env python3
"""
Autor : Brian Miró <10840318@iespenyagolosa.es>
Fecha   : 9/11/22
Propósito: Dibujar un rectángulo
"""

anchura=int(input('Anchura del rectángulo: '))
altura=int(input('Altura del rectángulo: '))
longitud='*'
for i in range(1,altura+1):
    print(longitud*anchura)