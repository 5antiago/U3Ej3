from inscripcion import Inscripcion

class Coleccioninscripcion(object):
    __Inscripciones = list

    def __init__(self):
        self.__Inscripciones = []

    def agregarinscripcion(self, inscip):
        if type(inscip) == Inscripcion:
            self.__Inscripciones.append(inscip)
    def getinscripciones(self):
        return self.__Inscripciones
    def getinscripcion(self, index):
        return self.__Inscripciones[index]
    def cant(self):
        return len(self.__Inscripciones)