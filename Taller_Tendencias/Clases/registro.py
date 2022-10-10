class Registro:
    def __init__(self):
        pass

    def setIdentificador(self, identificador):
        self.identificador = identificador

    def getIdentificador(self):
        return self.identificador

    def setTitulo(self, titulo):
        self.titulo = titulo

    def gettitulo(self):
        return self.titulo

    def settipo(self, tipo):
        self.tipo = tipo

    def gettipo(self):
        return self.tipo

class RegistroMaterial(Registro):
    def setfecha(self, fecha):
        self.fecha = fecha

    def getfecha(self):
        return self.fecha

    def setCantidad(self, cant):
        self.cant = cant

    def getCantidad(self):
        return self.cant

class RegistroPersona(Registro):
    def __init__(self):
        pass
    def DerechoDePrestamo(self):
        self.rol = Registro.gettipo(self)
        if self.rol == 'estudiante':
            derechoPrestamo = 5
        elif self.rol == 'profesor':
            derechoPrestamo = 3
        else:
            derechoPrestamo = 1
        return derechoPrestamo

    def setArticulosPrestados(self,lista, id):
        self.lista = lista
        self.lista.append(id)

    def getArticulosPrestados(self):
        return self.lista

    def eliminadordeArticulos(self, lista, a):
        self.lista = lista
        self.lista.remove(a)
        return self.lista