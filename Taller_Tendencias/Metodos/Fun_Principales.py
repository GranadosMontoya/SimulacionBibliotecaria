from datetime import date
from time import sleep
from Clases.Historial import *
from Clases.registro import RegistroMaterial, RegistroPersona


dicMaterial = {}
dicPersona = {}
listaMaterial = []
listaPersona = []
objpersona = RegistroPersona()
objmaterial = RegistroMaterial()
objHistorial = Historial()
opcion = ''

def RegistrarUnMaterial():
    while True:
        identificador = input("Ingrese el identificador: ")
        while ValidarID(identificador) == False or YaExiste(identificador,listaMaterial):
            identificador = input("Ingrese el identificador: ")
        titulo = input("Ingrese el titulo del articulo: ")
        while ValidarName(titulo) == False:
            titulo = input("Ingrese el titulo del articulo: ")
        tipo = ""
        while tipo != 'libro' and tipo != 'revista' and tipo != 'audiovisual':
            tipo = input("Ingrese el tipo de articulo(libro, revista, audivisual): ")
            tipo.lower()
            if ValidarVacio(tipo) == False:
                continue
            elif tipo != "libro" and tipo != "revista" and tipo!="audiovisual":
                print("Escriba una de las opciones")
        cantidad = input("Ingrese la cantidad: ")
        while ValidarVacio(cantidad) == False or ValidarEntero(cantidad)== False:
            cantidad = input("Ingrese la cantidad: ")
        cantidad = int(cantidad)
        print("***** La fecha de ingreso es *****")
        fecha = date.today() 
        print("*******", fecha, "*******")
        fecha = str(fecha)

        listaMaterial.append(identificador)
        objmaterial.setIdentificador(identificador)
        objmaterial.setTitulo(titulo)
        objmaterial.setfecha(fecha)
        objmaterial.settipo(tipo)
        objmaterial.setCantidad(cantidad)


        registroMaterial = {'Identificador': objmaterial.getIdentificador(), 'Titulo': objmaterial.gettitulo(
        ), 'fecha de registro': objmaterial.getfecha(), 'Tipo': objmaterial.gettipo(), 'Cantidad actual': objmaterial.getCantidad()}
        dicMaterial[objmaterial.getIdentificador()] = registroMaterial
        print("Proceso finalizado")
        sleep(1)
        break

def RegistrarUnaPersona():
    while True:
        cedula = input("Ingrese la cedula: ")
        while ValidarID(cedula) == False or YaExiste(cedula,listaPersona):
            cedula = input("Ingrese el cedula: ")
        nombre = input("Ingrese el nombre: ")
        while ValidarName(nombre) == False:
            nombre = input("Ingrese el nombre: ")
        rol = ""
        while rol != 'estudiante' and rol != 'profesor' and rol != 'administrativo':
            rol = input("Ingrese el rol(estudiante, profesor, administrativo): ")
            rol.lower()
            if ValidarVacio(rol) == False:
                continue
            elif rol != "estudiante" and rol != "profesor" and rol!="administrativo":
                print("Escriba una de las opciones")

        listaPersona.append(cedula)
        objpersona.setIdentificador(cedula)
        objpersona.setTitulo(nombre)
        objpersona.settipo(rol)

        registroPersona = {'Cedula': objpersona.getIdentificador(), 'Nombre': objpersona.gettitulo(), 'Rol': objpersona.gettipo(), 'Derecho de prestamo': objpersona.DerechoDePrestamo(), 'Identificadores de articulos asociados': [], 'Cantidad de articulos asociados': 0}
        dicPersona[objpersona.getIdentificador()] = registroPersona
        print("Proceso finalizado")
        sleep(1)
        break

def EliminarUnaPersona():
    cedula = ""
    while True:
        cedula = input("Ingrese la cedula:")
        if not(ValidarVacio(cedula)) or not(ValidarEntero(cedula)) or not(NoExiste(cedula,listaPersona)):
            continue
        if dicPersona[cedula]['Cantidad de articulos asociados'] == 0: 
            listaPersona.remove(cedula)
            print("'"+str(dicPersona[cedula]["Nombre"])+"'-"+"'"+str(dicPersona[cedula]["Cedula"])+"'"+" han sido eliminados con exito")
            dicPersona.pop(cedula)
            sleep(2)
            print("Proceso finalizado")
            break
        else:
            print("No se puede borrar porque la persona tiene prestamos pendientes")
            sleep(1)

def RealizarUnPrestamo():
    while True:
        cedula = input("Ingrese la cedula: ")
        while not(ValidarID(cedula)) or not(NoExiste(cedula,listaPersona)):
            cedula = input("Ingrese el cedula: ")
        prestar = dicPersona[cedula]["Derecho de prestamo"]
        if prestar > 0:
            print("Articulos asociados: "+str(dicPersona[cedula]["Identificadores de articulos asociados"]))
            identificador = input("Ingrese el identificador: ")
            while not(ValidarID(identificador)) or not(NoExiste(identificador,listaMaterial)):
                identificador = input("Ingrese el identificador: ") 
            lista = dicPersona[cedula]["Identificadores de articulos asociados"]
            if buscar(identificador,lista):
                print("No se puede prestar el mismo articulo")
                break
            elif dicMaterial[identificador]["Cantidad actual"] == 0:
                print("No existen unidades disponibles")
                sleep(1)
                break
            else:
                objpersona.setArticulosPrestados(lista,identificador)
                dicPersona[cedula]["Derecho de prestamo"] = dicPersona[cedula]["Derecho de prestamo"]-1
                dicPersona[cedula]['Cantidad de articulos asociados'] = dicPersona[cedula]['Cantidad de articulos asociados']+1
                dicMaterial[identificador]["Cantidad actual"] = dicMaterial[identificador]["Cantidad actual"]-1
                print(list(dicMaterial[identificador].items()))
                print("Prestamo realizado con exito")
                nombre = dicPersona[cedula]["Nombre"]
                titulo = dicMaterial[identificador]["Titulo"]
                hoy = date.today()
                objHistorial.setHistorial(cedula,nombre,identificador,titulo,hoy,"Prestamo")
                sleep(1)
                break
        else:
            print("No se tiene derecho a prestamo")
            sleep(1)
            break

def RealizarUnaDevolucion():
    while True:
        cedula = input("Ingrese la cedula: ")
        while not(ValidarID(cedula)) or not(NoExiste(cedula,listaPersona)):
            cedula = input("Ingrese la cedula: ")
        articulos = dicPersona[cedula]["Cantidad de articulos asociados"]
        if  articulos > 0:
            print("Articulos asociados: "+str(dicPersona[cedula]["Identificadores de articulos asociados"]))
            identificador = input("Ingrese el identificador: ")
            while not(ValidarID(identificador)) or not(NoExiste(identificador,listaMaterial)):
                identificador = input("Ingrese el identificador: ")
            lista = dicPersona[cedula]["Identificadores de articulos asociados"]
            if not(buscar(identificador,lista)):
                print("El articulo no está asociado a la cedula")
                sleep(1)
                break
            else:
                lista = dicPersona[cedula]["Identificadores de articulos asociados"]
                dicPersona[cedula]["Identificadores de articulos asociados"] = objpersona.eliminadordeArticulos(lista , identificador)
                dicPersona[cedula]["Derecho de prestamo"] = dicPersona[cedula]["Derecho de prestamo"]+1
                dicPersona[cedula]['Cantidad de articulos asociados'] = dicPersona[cedula]['Cantidad de articulos asociados']-1
                dicMaterial[identificador]["Cantidad actual"] = dicMaterial[identificador]["Cantidad actual"]+1
                print(list(dicMaterial[identificador].items()))
                print("Devolución realizada con exito")
                nombre = dicPersona[cedula]["Nombre"]
                titulo = dicMaterial[identificador]["Titulo"]
                hoy = date.today()
                objHistorial.setHistorial(nombre,cedula,identificador,titulo,hoy,"Devolucion")
                sleep(1)
                break
        else:
            print("La cedula ingresada no tiene articulos asociados")
            sleep(1)
            break

def IncrementarCantidad():
    identificador = input("Ingrese el identificador: ")
    while not(ValidarID(identificador)) or not(NoExiste(identificador,listaMaterial)):
        identificador = input("Ingrese el identificador: ")
    cantidad = input ("Ingrese la cantidad a agregar: ")
    while not(ValidarID(cantidad)):
        cantidad = input("Ingrese cantidad a agregar: ")
    cantidad = int(cantidad)
    cant = dicMaterial[identificador]["Cantidad actual"]
    nuevaCant = cantidad + cant
    objmaterial.setCantidad(nuevaCant)
    print(str(objmaterial.getCantidad()))
    dicMaterial[identificador]["Cantidad actual"] = objmaterial.getCantidad()
    print("Articulos agreagdos con exito")
    print(list(dicMaterial[identificador].items()))
    sleep(1)

def ConsultarHistorial():
    mostrar = objHistorial.GetHistorial()
    print(mostrar)



###################################### Funciones de Validacion ######################################################


def ValidarVacio(id):
    if len(id) == 0:
       print("El campo no puede estar vacio")
       return False
    return True

def ValidarEntero(id):
    if id.isdigit() == False:
       print("Solo se permiten números enteros")
       return False
    return True

def ValidarID(id):
    if not(ValidarVacio(id)) or not(ValidarEntero(id)):
        return False
    else:
        return True

def ValidarName(nombre):
    if not(ValidarVacio(nombre)):
        return False

def buscar(a,b):
    if a in b:
        return True
    else:
        return False

def YaExiste(a,b):
    if buscar(a,b):
        print("El dato ya existe")
        return True
    return False

def NoExiste(a,b):

    if not(buscar(a,b)):
        print("El dato no existe")
        return False
    return True

def preguntar():
    while True:
        try:
            print("\n")
            opcion = int(input("Ingrese una de las opciones: \n 1. Registrar un material en el catálogo. \n 2. Registrar una persona.\n 3. Eliminar una persona. \n 4. Registrar un préstamo. \n 5. Registrar una devolución. \n 6. Modificar cantidad de material . \n 7. Consultar el historial de la biblioteca.\n 8.Salir\n"))
            if opcion < 0 or opcion > 8:
                raise Exception()
            return opcion
        except:
            print("No ha ingresado una opcion correcta. Vuelva a intentarlo")
            sleep(2)