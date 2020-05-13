class Persona(object):
    __nom = str
    __dir = str
    __dni = str

    def __init__(self, nom, dir, dni):
        self.__nom = nom
        self.__dir = dir
        self.__dni = dni
    def getnom(self):
        return self.__nom
    def getdir(self):
        return self.__dir
    def getdni(self):
        return self.__dni
        
