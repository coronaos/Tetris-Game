import src.Controlador.c_main as controlador
from src.Model.m_ficheros import Fichero
import time

# Vista donde se printa top 3 jugadores del fichero.
def vistaRanking():
    m_fichero = Fichero("\historial.txt")
    ranking = m_fichero.rankingFichero()

    print("RANKING TOP 3!")
    print("--------------")
    for r in ranking:
        print(r)

    time.sleep(2)
    print("\n \n")
    print("1- To play")
    print("2- Ranking")
    print("3- Exit")
    tecla = input()
    controlador.start(tecla)