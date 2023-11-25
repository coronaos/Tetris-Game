import os

'''
 Classe de Fichero. Necesario implementarlo asi para testing.
'''
class Fichero:

    # Inicialización segun nombre de fichero en la ruta de este archivo
    def __init__(self, fichero):
        self.path = os.path.dirname(os.path.abspath(__file__))
        self.fichero = self.path + fichero

    # Función de lectura de fichero
    def leerFichero(self):
        with open(self.fichero) as f:
            texto = f.readlines()
            f.close()
            return texto

    # Función de escritura de fichero
    def escribirFichero(self,nombre, puntuacion):
        f = open(self.fichero, "a+")
        f.write(f"{puntuacion} {nombre[0:3]}\n")
        f.close()

    # Función que devuelve top 3
    def rankingFichero(self):
        puntos = self.leerFichero()
        datos_reordenadors = []
        # Al ser string, no coge bien puntación. Se transforma a int y se ordena segun valor.
        for p in puntos:
            aux = p.split()
            puntos = int(aux[0])
            datos_reordenadors.append((puntos, p))
        ordenado_P = sorted(datos_reordenadors, key=lambda x: x[0], reverse=True)
        return [x[1] for x in ordenado_P[0:3]]

