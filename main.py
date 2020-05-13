import csv
from persona import Persona
from inscripcion import Inscripcion
from taller import TallerCapacitacion
from coleccionpersona import ColeccionPersona
from coleccioninscripcion import Coleccioninscripcion
from manejataller import manejataller
from menu import Menu
if __name__ == "__main__":
    talleres = manejataller()
    personas = ColeccionPersona()
    inscripcion = Coleccioninscripcion()
    with open("Talleres.csv") as f:
        reader = csv.reader(f, delimiter=",")
        first = True
        cant = int
        for row in reader:
            if first:
                cant = row[0]
                first = False
            else:
                talleres.agregataller(TallerCapacitacion(int(row[0]), row[1], int(row[2]), int(row[3])))
    menu = Menu()
    print(" 1. Inscribir \n 2. Consulta de Inscripcion \n 3. Inscripciones al Taller \n 4. Pagar \n 5. Guardar \n 0. Salir")
    op = int(input("\n Ingrese opcion: "))
    while op > 0:
        menu.opcion(op, talleres, personas, inscripcion)
        print(" 1. Inscribir \n 2. Consulta de Inscripcion \n 3. Inscripciones al Taller \n 4. Pagar \n 5. Guardar \n 0. Salir")
        op = int(input("\n Ingrese opcion: "))
