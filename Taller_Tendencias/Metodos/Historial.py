
def setHistorial(self,nombre,cedula,identificador,titulo,fecha):
    self.nombre = nombre
    self.cedula = cedula
    self.identificador = identificador
    self.titulo = titulo
    self.fecha = fecha
    Diccionario_historial = {
        'nombre':self.nombre,
        'cedula':self.cedula,
        'identificador':self.identificador,
        'Titulo':self.titulo,
        'Fecha':self.fecha
    }
    self.vector.append(Diccionario_historial)

def GetHistorial(self):
    return self.vector
