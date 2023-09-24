# Primer proyecto Fundamentos de Python M1

print("BIENVENIDOS")
print("CALCULADORA DE IMC")

# Solicitamos escriban su información

print("A continuación intoduzca sus datos")
nombre = input("Nombre Completo: ")
apellido1 = input("Apellido Paterno: ")
apellido2 = input("Apellido Materno: ")
edad = int(input("Edad: "))
peso = float(input("Peso en Kilogramos: "))
estatura = float(input("Estatura en metros: "))

# Procedemos a que se muestren los datos introducidos por el usuario

print("Su nombre es: ", end = " ")
print(nombre, end = " ")
print(apellido1, end = " ")
print(apellido2)

# Redefinimos las variables para poder imprimirlas como texto

print("Usted tiene: " + str(edad) + " años")
print("Usted mide: " + str(estatura) + " metros")
print("Su peso es: " + str(peso) + " kilogramos")

# Calculamos el IMC

IMC = peso / estatura ** 2
print("Su IMC es: " + str(IMC))

print("Muchas Gracias, esperamos la información se útil a usted")
