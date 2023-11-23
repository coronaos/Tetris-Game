import os

class Fichero:
    def __init__(self, fichero):
        self.path = os.path.dirname(os.path.abspath(__file__))
        self.fichero = self.path + fichero

    def leerFichero(self):
        with open(self.fichero) as f:
            texto = f.readlines()
            f.close()
            return texto


    def escribirFichero(self,nombre, puntuacion):
        f = open(self.fichero, "a+")
        f.write(f"{puntuacion} {nombre[0:3]}\n")
        f.close()


    def rankingFichero(self):
        puntos = self.leerFichero()
        ordenadoP = sorted(puntos, reverse=True)
        return ordenadoP[0:3]