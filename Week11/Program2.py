matriz = [
    [5, 8, 3],
    [2, 9, 4],
    [6, 1, 7]
]

print("Matriz antes:")
for f in matriz:
    print(f)

fila = int(input("Fila a ordenar (0-2): "))

matriz[fila] = sorted(matriz[fila])  # Ordena la fila

print("Matriz después:")
for f in matriz:
    print(f)
