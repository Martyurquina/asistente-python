
from funciones import obtener_opciones,ejecutar_opcion

nombre = input("¿Cómo te llamás?")
continuar = True

while continuar:
    opcion = obtener_opciones()
    continuar = ejecutar_opcion(opcion,nombre)

    
