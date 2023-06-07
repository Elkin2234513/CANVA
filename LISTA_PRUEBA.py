
edades = [20, 41, 6, 18, 23]

mi_lista = ['Juan', 'Pedro', 'Laura', 'Carmen', 'Susana']


print(mi_lista[0]) # Muestra Juan (la primera posición es la 0)
print(mi_lista[-1]) # Muestra Susana
print(mi_lista[1]) # Muestra Pedro
print(mi_lista[2]) # Muestra Laura
print(mi_lista[-2]) # Muestra Carmen


# Recorriendo los elementos
for edad in edades:
    print(edad)

# Recorriendo los índices
for i in range(len(edades)):
    print(edades[i])

# Con while y los índices
indice = 0

while indice < len(edades):
    print(edades[indice])
    indice += 1



#La función pop, removerá un elemento según el índice que se indique.
palabras = ['hola', 'hello', 'ola']

palabras.pop(-1)

print(palabras)
# Mostrará ['hola', 'ola']



#La función remove, removerá un elemento según el valor que este tenga al interior de la lista.
palabras = ['hola', 'hello', 'hello', 'ola']

palabras.remove('ola')

print(palabras)
# Mostrará ['hola', 'hello', 'ola']



#EJEMPLOS DE LISTA EN PYTHON

# Creamos las listas (vacías al comienzo)
nombres = []
identificaciones = []

# Definimos un tamaño para las listas
# Lo puedes cambiar si quieres
tamaño = 3

# Leemos los datos y los agregamos a la lista
for i in range(tamaño):
    print("Ingrese los datos de la persona", i + 1)
    nombre = input("Nombre: ")
    identificación = input("Identificación: ")

    nombres.append(nombre)
    identificaciones.append(identificación)

# Ahora mostremos las listas
for i in range(tamaño):
    print("Mostrando los datos de la persona", i + 1)

    print("Nombre:", nombres[i])
    print("Identificación:", identificaciones[i])






#DICCIONARIO 
nombre_del_diccionario = {}

otro_diccionario = {
    "nombre": "Alberto",
    "usuario": "alb_123",
}

mi_diccionario = {
    "nombre": "Juan",
    "usuario": "jn123",
}

# Muestra Juan
print(mi_diccionario["nombre"])

# Muestra jn123
print(mi_diccionario["usuario"])


mi_diccionario = {
    "nombre": "Juan",
    "edad": "23",
    "usuario": "jn23",
}

# Recorriendo los elementos

for llave in mi_diccionario:
    print(llave, ": ", mi_diccionario[llave], sep='')




#ejemplos de diccionario 

# Creamos el diccionario con listas vacías en su interior
usuarios = {
    "nombres": [],
    "identificaciones": []
}

# Definimos un tamaño para las listas del diccionario
# Lo puedes cambiar si quieres
tamaño = 3

# Leemos los datos y los agregamos a el diccionario
for i in range(tamaño):
    print("Ingrese los datos de la persona", i + 1)
    nombre = input("Nombre: ")
    identificación = input("Identificación: ")

    # La primera lista es para los nombres
    usuarios["nombres"].append(nombre)

    # La segunda lista es para las identificaciones
    usuarios["identificaciones"].append(identificación)

# Ahora mostremos los valores en el diccionario
for i in range(tamaño):
    print("Mostrando los datos de la persona", i + 1)

    print("Nombre:", usuarios["nombres"][i])
    print("Identificación:", usuarios["identificaciones"][i])