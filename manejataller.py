from taller import TallerCapacitacion
class manejataller(object):
    __talleres = list

    def __init__(self):
        self.__talleres = []

    def agregataller(self, taller):
        if type(taller) == TallerCapacitacion:
            self.__talleres.append(taller)
    def gettaller(self, id):
        i=0
        id = int(id)
        while i < len(self.__talleres) and self.__talleres[i].getid() != id:
            i +=1
        if i < len(self.__talleres):
            return self.__talleres[i]
