from inscripcion import Inscripcion
import csv
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
    def guardar(self):
        with open('Inscripciones.csv', 'w', newline='') as f:
            writer = csv.writer(f, delimiter=',')
            for inscripcion in self.__Inscripciones:
                writer.writerow([inscripcion.getpersona().getdni(), inscripcion.gettaller().getid(), inscripcion.getfecha(), inscripcion.getpago()])
            return True
    def inscriptaller(self, cod):
        aux = ""
        for inscrip in self.__Inscripciones:
            if inscrip.gettaller().getid() == cod:
                aux += "Alumno: {} \n\t DNI: {} \n\t Domicilio: {}  ".format(inscrip.getpersona().getnom(), inscrip.getpersona().getdni(), inscrip.getpersona().getdir())
        return aux
    def registrarpago(self, dni):
        i = 0
        aux = False
        while i<len(self.__Inscripciones):
            if dni != self.__Inscripciones[i].getpersona().getdni():
                i += 1
            else:
                self.__Inscripciones[i].pago()
                aux = True
                
        return aux
    def consultarinscrip(self, dni):
        aux = ""
        for inscrip in self.__Inscripciones:
            if inscrip.getpersona().getdni() == dni:
                if inscrip.getpago():
                    aux += "Inscripto en el taller {}, no adeuda \n".format(inscrip.gettaller().getnom())
                else:
                    aux += "Inscripto en el taller {}, adeuda {} \n ".format(inscrip.gettaller().getnom(),inscrip.gettaller().getmonto() )
        return aux