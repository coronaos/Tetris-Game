import os

script_dir = os.path.dirname(os.path.abspath(__file__))


def leerFichero():
    with open(script_dir + "/historial.txt") as f:
        texto = f.readlines()
        f.close()
        return texto


def escribirFichero(nombre, puntuacion):
    f = open(script_dir + "/historial.txt", "a+")
    f.write(f"{puntuacion} {nombre[0:3]}\n")
    f.close()


def rankingFichero():
    puntos = leerFichero()
    ordenadoP = sorted(puntos, reverse=True)
    return ordenadoP[0:3]