import src.Controlador.c_main as controlador

'''
Vista y ejecutable principal del juego. Selección de menu
'''
if __name__ == "__main__":
    print("TETRIS GAME")
    print("\n")
    print("by Maties & Esther")

    print("1- To play")
    print("2- Ranking")
    print("3- Exit")
    tecla = input()
    controlador.start(tecla)


