import csv
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
        inscip = Inscripcion(input("Ingrese fecha: "), pers, tall)
        inscripcion.agregarinscripcion(inscip)
        print("{} Inscripto en taller: {}".format(inscip.getpersona().getnom(), inscip.gettaller().getnom()))
    def consultarins(self, taller, persona, inscripcion):
        dni = input("Ingrese Dni: ")
        for inscrip in inscripcion.getinscripciones():
            if inscrip.getpersona().getdni() == dni:
                if inscrip.getpago():
                    print("Inscripto en el taller {}, no adeuda ".format(inscrip.gettaller().getnom()))
                else:
                    print("Inscripto en el taller {}, adeuda {}".format(inscrip.gettaller().getnom(),inscrip.gettaller().getmonto() ))
    def inscriptaller(self, taller, persona, inscripcion):
        cod = int(input("Ingrese id del taller: "))
        for inscrip in inscripcion.getinscripciones():
            if inscrip.gettaller().getid() == cod:
                print("Alumno: {} \n\t DNI: {} \n\t Domicilio: {}  ".format(inscrip.getpersona().getnom(), inscrip.getpersona().getdni(), inscrip.getpersona().getdir()))
    def regispago(self, taller, persona, inscripcion):
        i = 0
        dni = input("Ingrese DNI: ")
        while i<inscripcion.cant() and dni != inscripcion.getinscripcion(i).getpersona().getdni():
            i += 1
        if i < inscripcion.cant():
            inscripcion.getinscripcion(i).pago()
    def guardar(self, taller, persona, inscripcion):
        with open('Inscripciones.csv', 'w', newline='') as f:
            writer = csv.writer(f, delimiter=',')
            for inscripcion in inscripcion.getinscripciones():
                writer.writerow([inscripcion.getpersona().getdni(), inscripcion.gettaller().getid(), inscripcion.getfecha(), inscripcion.getpago()])