
from funciones import obtener_opciones,saludar

nombre = input("¿Cómo te llamás?")
opcion = 0
while opcion !=3:
    opcion = obtener_opciones()
    if (opcion == 1) :
        saludar(nombre)
    elif(opcion == 2):
        print(nombre)
    elif (opcion == 3):
        print("ADIOS")
    else:
        print ("opcion incorrecta")

    
