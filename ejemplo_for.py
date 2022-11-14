# Calcula la tabla de multiplicar
numero=int(input('Introduce un número y calcularé su tabla de multiplicar: '))
for i in range(0,11):
    resultado=numero*i
    print(f'{numero}x{i}={resultado}')