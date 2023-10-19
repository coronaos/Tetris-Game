import src.Controlador.c_main as controlador
import src.Model.m_ficheros as ficheros
import time
def vistaRanking():
    ranking = ficheros.rankingFichero()

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