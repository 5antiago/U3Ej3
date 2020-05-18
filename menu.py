from persona import Persona
from inscripcion import Inscripcion
from taller import TallerCapacitacion
from coleccionpersona import ColeccionPersona
from coleccioninscripcion import Coleccioninscripcion
from manejataller import manejataller
class Menu(object):
    __switcher = dict
    def __init__(self):
        self.__switcher = {1: self.Inscribir, 2: self.consultarins, 3: self.inscriptaller, 4:self.regispago, 5: self.guardar}
    def opcion(self, op, taller, persona, inscripcion):
        self.__switcher.get(op, lambda: print("Opcion Incorrecta"))(taller, persona, inscripcion)


    def Inscribir(self, taller, persona, inscripcion ):
        pers = Persona(input("Ingrese nombre: "), input("Ingrese Direccion: "), input("Ingrese Dni: "))
        persona.agregarpersona(pers)
        
        tall = taller.gettaller(int(input("Ingrese id del taller: ")))
        #Verifica si se encuentra el taller
        while tall == None:
            tall = taller.gettaller(int(input("Taller no encontrado \n Ingrese id del taller: ")))

        inscip = Inscripcion(input("Ingrese fecha: "), pers, tall)
        inscripcion.agregarinscripcion(inscip)
        #Verifica si hay cupo disponible
        if tall.inscribir():
            print("{} Inscripto en taller: {}".format(inscip.getpersona().getnom(), inscip.gettaller().getnom()))
        else:
            print("No hay cupo disponible para el taller")

    def consultarins(self, taller, persona, inscripcion):
        aux = inscripcion.consultarinscrip(input("Ingrese Dni: "))
        if aux == "":
            print("No se encontro a la persona")
        else:
            print(aux)

    def inscriptaller(self, taller, persona, inscripcion):
        cod = int(input("Ingrese id del taller: "))
        aux = inscripcion.inscriptaller(cod)
        #Verifica si hay inscriptos en el taller
        if aux == "":
            print ("No se encontraron Inscriptos")
        else:
            print(aux)

    def regispago(self, taller, persona, inscripcion):
        if inscripcion.registrarpago(input("Ingrese DNI: ")):
            print("Pago Exitoso")
        else:
            print("No se encontro la persona")

    def guardar(self, taller, persona, inscripcion):
        if inscripcion.guardar():
            print("Guardado Exitoso")
        else:
            print("Error al Guardar")