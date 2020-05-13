from inscripcion import Inscripcion
class TallerCapacitacion(object):
    __id    = int
    __nom   = str
    __vac   = int
    __monto = float
    __inscriptos = list

    def __init__(self, ide, nom, vac, monto):
        self.__id    = ide
        self.__nom   = nom
        self.__vac   = vac
        self.__monto = monto
        self.__inscriptos = []
    def getid(self):
        return self.__id
    def getnom(self):
        return self.__nom
    def getvac(self):
        return self.__vac
    def getmonto(self):
        return self.__monto
    def getinscriptos(self):
        return self.__inscriptos
    def inscribir(self, inscrip):
        if type(inscrip) == Inscripcion:
            self.__vac -= 1
            self.__inscriptos.append(inscrip)