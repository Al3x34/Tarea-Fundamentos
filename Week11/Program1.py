matriz = [
    [5, 8, 3],
    [2, 9, 4],
    [6, 1, 7]
]

valor = int(input("Que numero quieres localizar?: "))

for i in range(3):
    for j in range(3):
        if matriz[i][j] == valor:
            print(f"Se encuentra en ({i}, {j})")
            exit()  # Sale del programa si encuentra el número

print("No se puede encontrar")
