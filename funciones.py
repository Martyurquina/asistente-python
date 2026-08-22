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
            return opcion
        except ValueError:  
            print("Eso no es un número.")
            