from time import sleep
from Metodos.Fun_Principales import *
from Metodos.Historial import *


while opcion != 8:
    try:
        if opcion == 1:
            RegistrarUnMaterial()   
        elif opcion == 2:
            RegistrarUnaPersona()
        elif opcion == 3:
            EliminarUnaPersona()
        elif opcion == 4:
            RealizarUnPrestamo()
        elif opcion == 5:
            RealizarUnaDevolucion()
        elif opcion == 6:
            IncrementarCantidad()
        elif opcion == 7:
            ConsultarHistorial()
            sleep(10)
        elif opcion == 0:
            oe = int(input("opc: "))
            if oe == 1:
                print(list(dicMaterial.values()))
            elif oe == 2:
                print(list(dicPersona.values()))
        opcion = preguntar()
    except KeyboardInterrupt:
        print("salida con exito")
        sleep(1)
        opcion = preguntar()
print("Proceso finalizado")