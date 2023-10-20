fecha_de_nacimiento = input("Introduzca su fecha de nacimiento en este formato: dd/mm/aaaa: ")

día, mes, año = fecha_de_nacimiento.split("/")

día = fecha_de_nacimiento[0:2]
mes = fecha_de_nacimiento[3:5]
año = fecha_de_nacimiento[6:10]
print(f"día {día} Mes: {mes} Año: {año}")


