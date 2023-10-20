# invirtiendo el string

frase1 = input("Introduzca una frase celebre: ")
invirtiendo = frase1[::-1]

print(invirtiendo)


#Invirtiendo el string con bucle for

frase2 = input("Introduzca una frase celebre: ")
variable2= ""

for character in frase2:
    variable2 = character + variable2
print(f"{variable2}")