from persona import Persona
class ColeccionPersona(object):
    __Personas = list

    def __init__(self):
        self.__Personas = []

    def agregarpersona(self, persona):
        if type(persona) == Persona:
            self.__Personas.append(persona)
    def getpersona(self, dni):
        i = 0
        while i < len(self.__Personas) and self.__Personas[i].getdni() != dni:
            i += 1
        if i < len(self.__Personas):
            return self.__Personas[i]
