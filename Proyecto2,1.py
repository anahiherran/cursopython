#Segundo proyecto Fundamentos Python

print("Bienvenido")
print("Proyecto 2; Validación de datos")

#Solicitaremos al usuario crear una contraseña de 4 a 8 dígitos

palabra = input("Introduce una palabra: ")

while not(4 <len(palabra) <8):
    if len(palabra) < 4:
        print("Solo tiene ", len(palabra), "letras, intenta agregar letras")
        palabra = input("Introduce nuevamente una palabra: ")
    elif len(palabra) > 8:
        print("Ahora tiene ", len(palabra), "letras, intenta hacerla mas corta")
        palabra = input("Introduce nuevamente una palabra: ")
    elif len(palabra) == 4 or len(palabra) == 8:
        print("Tu palabra es: " + palabra)
        break
else:
    print("Palabra correcta, la palabra es: " + palabra)
    

