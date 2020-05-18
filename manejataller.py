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
        aux = None
        id = int(id)
        while i < len(self.__talleres):
            if self.__talleres[i].getid() != id:
                i +=1
            else:
                aux = self.__talleres[i]
        return aux