import src.Model.m_ficheros as ficheros
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

nombre = "MATIES"
puntuacion = "200"
def test_escribirFichero(): #Test para revisar que se escribe bien la puntuación y nombre en el historial
    escribirFichero(nombre, puntuacion)
    #with open(script_dir + "/historial_test.txt") as f:

def leerFichero():
    with open(script_dir + "/historial_test.txt") as f:
        texto = f.readlines()
        f.close()
        return texto


def escribirFichero(nombre, puntuacion):
    f = open(script_dir + "/historial_test.txt", "a+")
    f.write(f"{puntuacion} {nombre[0:3]}\n")
    f.close()


def rankingFichero():
    puntos = leerFichero()
    ordenadoP = sorted(puntos, reverse=True)
    return ordenadoP[0:3]