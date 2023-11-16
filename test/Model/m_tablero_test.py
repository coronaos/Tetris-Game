from src.Model.m_tablero import Tablero

#gracias a este test arreglamos que puedan poner negativos
def test_inicializacion():
    tablero = Tablero(-5, -10)
    assert(tablero.filas == -5), "[ERROR]: Se inicializa negativo"

def test_tablero_lleno(): #Se introduce un 1 en la fila 0 para ver si la función detecta correctamente que has perdido.
    tablero = Tablero(5, 10)
    for i in tablero.tablero:
        i[0] = 1
    assert(tablero.tablero_lleno(True) == True), "Fin de partida"

def test_overlap_check_final():
    tablero = Tablero(5, 10)
    pieza = [[]]
    posicion = [5,3]

def test_overlap_check_fueratablero():
    tablero = Tablero(5, 10)
    pieza = [[]]
    posicion = [5,3]

def test_overlap_check_choquedepiezas():
    tablero = Tablero(5, 10)
    pieza = [[]]
    posicion = [5,3]