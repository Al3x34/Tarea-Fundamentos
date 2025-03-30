# Diccionario con información personal ficticia sobre una persona de Ecuador
informacion_personal = {
    "nombre": "Carlos Gómez",  # Nombre
    "edad": 28,                # Edad
    "ciudad": "Quito",         # Ciudad
    "profesion": "Abogado"     # Profesión
}

# Mostrar el diccionario original
print(informacion_personal)

# Cambiar la ciudad de Quito a Guayaquil
informacion_personal["ciudad"] = "Guayaquil"

# Agregar un teléfono (clave: telefono)
informacion_personal["telefono"] = "0998765432"

# Verificar si ya existe la clave "telefono"
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0998765432"  # Si no, la agregamos

# Eliminar la clave "edad" del diccionario
del informacion_personal["edad"]

# Imprimir el diccionario final después de las modificaciones
print(informacion_personal)
