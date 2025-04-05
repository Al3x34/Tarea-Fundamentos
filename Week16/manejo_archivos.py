# Abrimos el archivo en modo escritura ("w") para escribir nuestras notas personales
with open("my_notes.txt", "w") as archivo:
    # Escribimos tres líneas de notas personales
    archivo.write("Hoy aprendi a manejar archivos en Python.\n")
    archivo.write("El modo 'w' sirve para escribir archivos.\n")
    archivo.write("El modo 'r' se usa para leer archivos.\n")

# Ahora abrimos el archivo en modo lectura ("r") para leer lo que escribimos
with open("my_notes.txt", "r") as archivo:
    # Leemos línea por línea y las mostramos en consola
    for linea in archivo:
        print(linea.strip())  # .strip() elimina los saltos de línea extra al imprimir
