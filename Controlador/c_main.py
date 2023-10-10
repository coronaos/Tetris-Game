from Model.m_tablero import Tablero
import Model.m_fichas as ficha
import Model.m_ficheros as ficheros
import Model.m_puntuacion as Puntuacion
import Vista.v_main as vista


def playGame():
    pieza_actual = ficha.pieza_aleatoria()
    pos_pieza = [0,5]
    tablero = Tablero(20,10)
    puntuacio = Puntuacion(1000)
    tablero.print_tablero()
    movimiento_jugador = input()
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
            pos_pieza = tablero.mover_abajo(pieza_actual, pos_pieza)
            pass
        elif(movimiento_jugador == "k"):
            #rotate
            if(tablero.overlap_check(pieza_actual, pos_pieza)):
                pieza_actual = ficha.rotar_pieza(pieza_actual)
                tablero.colocar_pieza(pieza_actual, pos_pieza)
            pass

        # printamos el tablero con la pieza colocada
        tablero.print_tablero()
        num_filas_eliminas = tablero.linea_completa()

        # miramos si se elimina fila, en caso de que si sumamos puntos y printamos tablero.
        if num_filas_eliminas > 0:
            puntuacio.sumar_puntos(20 * num_filas_eliminas)
            tablero.print_tablero()

    ficheros.escribirFichero(vista.nombreJugador, puntuacio.get_puntos())
    print("Thank you for playing!")