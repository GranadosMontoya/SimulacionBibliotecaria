class Historial:
    def __init__(self) -> None:
        self.vector = []
    def setHistorial(self,cedula,nombre,identificador,titulo,fecha,Tipo):
        self.nombre = nombre
        self.cedula = cedula
        self.identificador = identificador
        self.titulo = titulo
        self.fecha = str(fecha)
        Diccionario_historial = {
            'nombre':self.nombre,
            'cedula':self.cedula,
            'identificador':self.identificador,
            'Titulo':self.titulo,
            'Fecha':self.fecha,
            'Tipo':Tipo
        }
        self.vector.append(Diccionario_historial)
    def GetHistorial(self):
        return self.vector