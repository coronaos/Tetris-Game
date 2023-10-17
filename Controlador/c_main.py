from Model.m_tablero import Tablero
from ontab import wait_for_input
import Model.m_fichas as ficha
import Model.m_ficheros as ficheros
from Model.m_print import print_all
from Model.m_puntuacion import Punts
import Vista.v_ranking as ranking
import os

def start(tecla):
    cls()
    if tecla == "1":
        print("Press a,s,d to move the piece to the left, down and right position")
        print("Introduce a three letter name")
        nombreJugador = input()
        while len(nombreJugador) > 3:
            print("[ERROR]: Only valid a three letter name")
            nombreJugador = input()
        playGame(nombreJugador)
        # llamada a funcion de inicial la partida
    elif tecla == "2":
        ranking.vistaRanking()
    elif tecla == "3":
        exit()
    else:
        print("[ERROR]: Press 1, 2 or 3 to navegate in the menu.")

def cls():
    os.system('clear') #PARA UNIX
    #os.system('cls') #PARA WINDOWS



def playGame(nombreJugador):
    m_tablero = Tablero(10, 20)
    m_puntuacio = Punts("1000")
    m_colocada = False
    m_pieza_actual = ficha.pieza_aleatoria()
    m_pos_pieza = [0, 3]
    m_tablero.colocar_pieza(m_pieza_actual, m_pos_pieza)
    cls()
    m_pieza_siguiente = ficha.pieza_aleatoria()
    print("HOLA ESTO ES UNA PRUEBA")
    print_all(m_tablero.tablero, m_pieza_siguiente)

    m_movimiento_jugador = input()
    cls()

    while m_movimiento_jugador != "q" or m_tablero.tablero_lleno(m_pieza_actual, m_pos_pieza) == False:
        if m_movimiento_jugador == "a":
            #left
            m_pos_pieza = m_tablero.mover_izquierda(m_pieza_actual, m_pos_pieza)

            pass
        elif m_movimiento_jugador == "d":
            #right
            m_pos_pieza = m_tablero.mover_derecha(m_pieza_actual, m_pos_pieza)

            pass
        elif(m_movimiento_jugador == "s"):
            #down
            result = m_tablero.mover_abajo(m_pieza_actual, m_pos_pieza)
            if(result == False):
                m_colocada = True
            else:
                m_pos_pieza = result

            pass
        elif(m_movimiento_jugador == "k"):
            #rotate
            m_tablero.borrar_pieza(m_pieza_actual, m_pos_pieza)
            if m_tablero.overlap_check(ficha.rotar_pieza(m_pieza_actual), m_pos_pieza):
                m_tablero.colocar_pieza(m_pieza_actual, m_pos_pieza)
                print("No se puede girar")
            else:
                m_pieza_actual = ficha.rotar_pieza(m_pieza_actual)
                m_tablero.colocar_pieza(m_pieza_actual, m_pos_pieza)

            pass
        else:
            pass

        # printamos el tablero con la pieza colocada

        num_filas_eliminas = m_tablero.linea_completa()


        print_all(m_tablero, m_pieza_siguiente)
        # miramos si se elimina fila, en caso de que si sumamos puntos y printamos tablero.
        if num_filas_eliminas > 0:
            m_puntuacio.sumar_puntos(20 * num_filas_eliminas)
            print("HOLA ESTO ES UNA PRUEBA")
            print_all(m_tablero, m_pieza_siguiente)

        if m_colocada == True:
            print("new piece")
            m_colocada = False
            m_pieza_actual = m_pieza_siguiente
            m_pieza_siguiente = ficha.pieza_aleatoria()
            m_pos_pieza = [0, 3]
            m_tablero.colocar_pieza(m_pieza_actual, m_pos_pieza)
            cls()
            print_all(m_tablero, m_pieza_siguiente)

        m_movimiento_jugador = wait_for_input(0.5)
        if(m_movimiento_jugador):
            pass
        else:
            m_movimiento_jugador = "s"

        cls()

    ficheros.escribirFichero(nombreJugador, m_puntuacio.get_puntos())
    print("Thank you for playing!")


