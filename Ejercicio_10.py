productos_cesta = input("Introduzca los productos de la cesta entre comas: ")

separacion = productos_cesta.split(",")

for variable in separacion:
    print(variable)

