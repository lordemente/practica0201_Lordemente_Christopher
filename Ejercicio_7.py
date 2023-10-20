correo_electronico = input("Introduzca su correo electronico: ")

nuevo, dominio = correo_electronico.split("@")

correo_nuevo = f"{nuevo}@ceu.es"

print("correo electronico:", correo_nuevo.lower())
