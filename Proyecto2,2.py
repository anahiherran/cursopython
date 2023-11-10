#Encuentra el cuadrante
#Definamos las variables que debemos utilizar

x = int(input("Introduce una numero para X: "))
y = int(input("Introduce otro numero para Y: "))


if x == 0 and y == 0:
    print("Punto ubicado en el origen")
if x == 0:
    print("punto ubicado en el eje Y, tus coordenadas son: ("+ str(x) + "," + str(y) +")")
if y == 0:
    print("Punto ubicado en el eje X, tus coordenadas son: ("+ str(x) + "," + str(y) +")")
if x > 0 and y > 0:
    print("Estas en el cuadrante I, tus coordenadas son: ("+ str(x) + "," + str(y) +")")
if x < 0 and y > 0:
    print("Estas en el cuadrante II, tus coordenadas son: ("+ str(x) + "," + str(y) +")")
if x <0 and y < 0:
    print("Estas en el cuadrante III, tus coordenadas son: ("+ str(x) + "," + str(y) +")")
if x > 0 and y < 0:
    print("Estas en el cuadrante IV, tus coordenadas son: ("+ str(x) + "," + str(y) +")")





