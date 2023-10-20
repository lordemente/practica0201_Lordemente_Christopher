producto = input("Introduzca el nombre del producto: ")
precio = float(input("Introduzca el precio unitario: "))
unidades = int(input("Introduzca las unidades: "))

resultado = precio * unidades

#f"""  esta puede concadenar varias variables dentro de las llaves {} 

impresion = (f"producto: {producto} precio: {precio} unidad:  {unidades} total: {resultado}" )
print(impresion)

print(f"producto: {producto} precio: {precio} unidad:  {unidades} total: {resultado}" )

