
class Inscripcion(object):
    __fecha = str
    __pago = bool
    __persona = None
    __taller = None
    def __init__(self, fecha, persona, taller):
        self.__fecha = fecha
        self.__pago = False
        self.__persona = persona
        self.__taller = taller
    def pago(self):
        self.__pago = True
    def getpago(self):
        return self.__pago
    def getfecha(self):
        return self.__fecha
    def getpersona(self):
        return self.__persona
    def gettaller(self):
        return self.__taller