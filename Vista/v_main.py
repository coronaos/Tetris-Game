import Controlador.c_main as controlador
if __name__ == "__main__":
    """
    tablero = Tablero(20, 10)
    tablero2 = Tablero(20, 10)
    piexa = [[1,0],
     [1,0],
     [1,1]]
    tablero2.colocar_pieza(piexa, (0, 8))
    pieza = ficha.rotar_pieza(piexa)
    tablero.colocar_pieza(pieza, (0, 8))
    print(tablero)
    """
    ranking = controlador.ficheros.rankingFichero()
    print("TETRIS GAME")
    print("by Maties & Esther")
    print("Press P to start the game")
    print("Press a,s,d to move the piece to the left, down and right position")
    print("RANKING TOP 3!")
    print("--------------")
    print(ranking)
    tecla = input()
    if(tecla == "p"):
        print("Introduce a three letter name")
        nombreJugador = input()
        controlador.playGame()
        #llamada a funcion de inicial la partida
