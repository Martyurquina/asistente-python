def mostrar_menu():
    print ("Que queres hacer?")
    print ("1.Saludar")
    print("2.Mostrar nombre")
    print ("3.Salir")

def saludar(nombre):
    print("Hola " + nombre + " soy tu asistente personal" )

def obtener_opciones():
    while True:
        mostrar_menu()
        try:
            opcion = int(input("Ingrese su opción: "))
            if opcion in [1, 2, 3]:
                return opcion
            else:
                print("Esa opcion no existe, intentelo de nuevo")       
        except ValueError:  
            print("Eso no es un número.")

def ejecutar_opcion (opcion,nombre):
    if opcion == 1:
        saludar(nombre)
        return True
    elif opcion == 2:
        print (nombre)
        return True
    elif opcion == 3:
        print("ADIOS")
        return False
    else:
        print ("opcion incorrecta")