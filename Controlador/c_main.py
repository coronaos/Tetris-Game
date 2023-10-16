from Model.m_tablero import Tablero
from ontab import wait_for_input
import Model.m_fichas as ficha
import Model.m_ficheros as ficheros
from Model.m_puntuacion import Punts
import Vista.v_main as vista
import os
import time
import signal


def cls():
    os.system('cls')
def playGame():
    pieza_actual = ficha.pieza_aleatoria()
    pos_pieza = [0,3]
    colocada = False
    tablero = Tablero(10,20)
    print("tablero")
    puntuacio = Punts("1000")
    tablero.colocar_pieza(pieza_actual, pos_pieza)
    cls()
    tablero.print_tablero()

    movimiento_jugador = input()
    cls()
    while(movimiento_jugador!="q" or tablero.tablero_lleno(pieza_actual,pos_pieza)):
        if(movimiento_jugador == "a"):
            #left
            pos_pieza = tablero.mover_izquierda(pieza_actual, pos_pieza)

            pass
        elif(movimiento_jugador == "d"):
            #right
            pos_pieza = tablero.mover_derecha(pieza_actual, pos_pieza)

            pass
        elif(movimiento_jugador == "s"):
            #down
            result = tablero.mover_abajo(pieza_actual, pos_pieza)
            if(result == False):
                colocada = True
            else:
                pos_pieza = result

            pass
        elif(movimiento_jugador == "k"):
            #rotate
            tablero.borrar_pieza(pieza_actual, pos_pieza)
            if(tablero.overlap_check(ficha.rotar_pieza(pieza_actual), pos_pieza)):
                tablero.colocar_pieza(pieza_actual, pos_pieza)
                print("No se puede girar")
            else:
                pieza_actual = ficha.rotar_pieza(pieza_actual)
                tablero.colocar_pieza(pieza_actual, pos_pieza)

            pass


        # printamos el tablero con la pieza colocada

        num_filas_eliminas = tablero.linea_completa()
        tablero.print_tablero()
        # miramos si se elimina fila, en caso de que si sumamos puntos y printamos tablero.
        if num_filas_eliminas > 0:
            puntuacio.sumar_puntos(20 * num_filas_eliminas)
            tablero.print_tablero()

        if(colocada == True):
            print("new piece")
            colocada = False
            pieza_actual = ficha.pieza_aleatoria()
            pos_pieza = [0, 3]
            tablero.colocar_pieza(pieza_actual, pos_pieza)
            cls()
            tablero.print_tablero()

        movimiento_jugador = wait_for_input(1)
        if(movimiento_jugador):
            pass
        else:
            movimiento_jugador = "s"



        cls()




    ficheros.escribirFichero(vista.nombreJugador, puntuacio.get_puntos())
    print("Thank you for playing!")


