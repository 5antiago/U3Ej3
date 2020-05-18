from inscripcion import Inscripcion
class TallerCapacitacion(object):
    __id    = int
    __nom   = str
    __vac   = int
    __monto = float

    def __init__(self, ide, nom, vac, monto):
        self.__id    = ide
        self.__nom   = nom
        self.__vac   = vac
        self.__monto = monto
    def getid(self):
        return self.__id
    def getnom(self):
        return self.__nom
    def getvac(self):
        return self.__vac
    def getmonto(self):
        return self.__monto
    def inscribir(self):
        if self.__vac != 0:
            self.__vac -= 1
            return True
        else:
            return False