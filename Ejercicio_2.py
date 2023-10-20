 
nombre = input("Introduzca nombre y apellido: ")

#En cambio de linea "\n"

cambio_linea = nombre.lower() + "\n" + nombre.upper() + "\n" + nombre.title() + "\n"

print(cambio_linea)

# En una sola linea
print(nombre.lower() + " " + nombre.upper() + " " + nombre.title())

 