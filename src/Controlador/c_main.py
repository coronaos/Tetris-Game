from src.Model.m_tablero import Tablero
from ontab import wait_for_input
import src.Model.m_fichas as ficha
from src.Model.m_ficheros import Fichero
from src.Model.m_print import print_all
from src.Model.m_puntuacion import Punts
import src.Vista.v_ranking as ranking
import os

'''
Funcion para empezar segun parametro de la letra. Realiza la acción segun la tecla indicada. 
'''
def start(tecla):
    cls()
    if tecla == "1":
        print("Press a,s,d to move the piece to the left, down and right position")
        print("Press q to quit while you're playing")
        print("Introduce a three letter name")
        nombreJugador = input()
        while len(nombreJugador) > 3:
            print("[ERROR]: Only valid a three letter name")
            nombreJugador = input()
        playGame(nombreJugador.upper())
        # llamada a funcion de inicial la partida
    elif tecla == "2":
        ranking.vistaRanking()
    elif tecla == "3":
        exit()
    else:
        print("[ERROR]: Press 1, 2 or 3 to navegate in the menu.")

'''
Funcion que limpia la consola.
Importante utilizar la linea correcta 
según sistema operativo de utilización del juego.  
'''
def cls():
    #os.system('clear')  # LINEA PARA UNIX
    os.system('cls')  # LINEA PARA WINDOWS

'''
Funcion principal del juego. 
Recibe como parametro el nombre del jugador. 
'''
def playGame(nombreJugador):
    # setup variables para poder jugar
    m_tablero = Tablero(10, 20)
    m_puntuacio = Punts(100)
    m_colocada = False
    m_pieza_actual = ficha.pieza_aleatoria()
    m_pos_pieza = [0, 3]
    m_fichero = Fichero("\historial.txt")
    m_tablero.colocar_pieza(m_pieza_actual, m_pos_pieza)
    cls()
    m_pieza_siguiente = ficha.pieza_aleatoria()
    print_all(m_tablero.tablero, m_pieza_siguiente, m_puntuacio.get_puntos(), nombreJugador)
    tablero_lleno = False

    # Primer tecla de jugador. En este caso controlamos que sea una de las indicadas.
    m_movimiento_jugador = input()
    while m_movimiento_jugador not in ('q', 'a', 'd', 's', 'k'):
        print("Invalid input")
        m_movimiento_jugador = input()

    cls()

    '''
    bucle principal que controla el juego. 
    Mientras jugar no pierda, no llegue maxima puntuació o no salga del juego,
    se sigue ejecutanddo. 
    '''
    while m_movimiento_jugador != "q" and not m_puntuacio.puntuacion_maxima() and not tablero_lleno:
        if m_movimiento_jugador == "a":
            # Movimiento a la izquierda
            m_pos_pieza = m_tablero.mover_izquierda(m_pieza_actual, m_pos_pieza)

            pass
        elif m_movimiento_jugador == "d":
            # Moviemiento a la derecha
            m_pos_pieza = m_tablero.mover_derecha(m_pieza_actual, m_pos_pieza)

            pass
        elif(m_movimiento_jugador == "s"):
            # Moviemiento a abajo
            result = m_tablero.mover_abajo(m_pieza_actual, m_pos_pieza)

            '''
            Se revisa que haya llegando al final de movimiento hacia abajo,
            debido a choque con otra pieza o del tablero. 
            '''
            if(result == False):
                m_colocada = True
            else:
                m_pos_pieza = result
            pass
        elif(m_movimiento_jugador == "k"):
            # Rotar pieza
            m_tablero.borrar_pieza(m_pieza_actual, m_pos_pieza)

            # Comprobar que no el giro no choque con otra pieza.
            if m_tablero.overlap_check(ficha.rotar_pieza(m_pieza_actual), m_pos_pieza):
                # No se gira
                m_tablero.colocar_pieza(m_pieza_actual, m_pos_pieza)
                print("No se puede girar")
            else:
                m_pieza_actual = ficha.rotar_pieza(m_pieza_actual)
                m_tablero.colocar_pieza(m_pieza_actual, m_pos_pieza)
                print("Pieza girada correctamente")
            pass
        else:
            # En cualquier otro paso hacia abajo
            pass

        # Print del tablero con los nuevos estados.
        print_all(m_tablero.tablero, m_pieza_siguiente, m_puntuacio.get_puntos(), nombreJugador)

        # La ficha a llegado a su posicion final.
        if m_colocada == True:
            # Calcular filas eliminadas (lineas completas)
            num_filas_eliminas = m_tablero.linea_completa()
            if num_filas_eliminas > 0:
                # si se elimina fila sumamos puntos.
                m_puntuacio.sumar_puntos(20 * num_filas_eliminas)
            if not m_tablero.tablero_lleno(m_colocada):
                # Si no se ha llenado todo el tablero calculamos nuevos estados
                print("new piece")
                m_colocada = False
                m_pieza_actual = m_pieza_siguiente
                m_pieza_siguiente = ficha.pieza_aleatoria()
                m_pos_pieza = [0, 3]
                m_tablero.colocar_pieza(m_pieza_actual, m_pos_pieza)
                cls()
                print_all(m_tablero.tablero, m_pieza_siguiente, m_puntuacio.get_puntos(), nombreJugador)
            else:
                tablero_lleno = True

        # Esperar tecla de jugador, si no detecta ninguna, hacia abajo.
        m_movimiento_jugador = wait_for_input(0.3)
        if(m_movimiento_jugador):
            pass
        else:
            m_movimiento_jugador = "s"

        cls()

    # Finalización del juego.
    m_fichero.escribirFichero(nombreJugador, m_puntuacio.get_puntos())
    print_all(m_tablero.tablero, m_pieza_siguiente, m_puntuacio.get_puntos(), nombreJugador)
    print("Thank you for playing!")


