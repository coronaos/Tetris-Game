from src.Model.m_tablero import Tablero

#gracias a este test arreglamos que puedan poner negativos
def test_inicializacion():
    # <5 maximo --> partciones eqv= 0 2, frontera = 5, limite = 4, 6
    # Test negatiu
    tablero = Tablero(-6, -10)
    assert(tablero.filas == 6 and tablero.columnas == 10), "Pone el valor en absoluto"

    # Test particio equivalent 1
    tablero = Tablero(2, 3)
    assert (tablero.filas == 5 and tablero.columnas == 5), "Pone los valores por defecto"
    # Test particio equivalent 2
    tablero = Tablero(10, 15)
    assert (tablero.filas == 10 and tablero.columnas == 15), "Pone los valores indicados"

    #Test frontera
    tablero = Tablero(5, 5)
    assert (tablero.filas == 5 and tablero.columnas == 5), "Se incializa con los valores dados."

    # Test limit 1
    tablero = Tablero(6, 6)
    assert (tablero.filas == 6 and tablero.columnas == 6), "Se incializa con los valores dados."
    # Test limit 2
    tablero = Tablero(4, 4)
    assert (tablero.filas == 5 and tablero.columnas == 5), "Se incializa con los valores dados."

def test_tablero_lleno(): #Se introduce un 1 en la fila 0 para ver si la función detecta correctamente que has perdido.
    tablero = Tablero(5, 10)
    for i in tablero.tablero:
        i[0] = 1
    assert(tablero.tablero_lleno(True) == True), "Fin de partida"

def test_overlap_check_finaltablero():
    tablero = Tablero(5, 10)
    pieza = [[1, 0],
             [1, 0],
             [1, 1]]
    posicion = [3, 7]
    resultado = tablero.overlap_check(pieza, posicion)
    assert (resultado == [20, 20]), "Colocada al final del tablero correctamente"
def test_overlap_check_fueratablero():
    tablero = Tablero(5, 10)
    pieza = [[1, 0],
             [1, 0],
             [1, 1]]
    posicion = [4, 7]
    resultado = tablero.overlap_check(pieza, posicion)
    assert (resultado == True), "Colocada fuera del tablero"

def test_overlap_check_choquedepiezas():
    tablero = Tablero(5, 10)
    pieza = [[1, 0],
             [1, 0],
             [1, 1]]
    posicion = [3, 7]
    tablero.colocar_pieza(pieza, posicion) #CAMBIAR POR EL TEST DE COLOCAR PIEZA

    piezaTest = [[1, 1],
                [1, 1]]

    posicionTest = [3, 5]
    resultado = tablero.overlap_check(piezaTest, posicionTest)
    assert (resultado == [21, 21]), "Choque de piezas, colocada correctamente"

def test_looptesting_1():
    tablero = Tablero(5,5)
    respuesta = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    pieza = [[0]]
    posicion = [0, 0]
    tablero.borrar_pieza(pieza,posicion)
    assert(tablero.tablero == respuesta)
def test_looptesting_2():
    # Caso en el que el bucle se ejecuta una vez
    tablero = Tablero(5,5)
    respuesta = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    respuesta2 = [[0, 1, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    pieza = [[1]]
    posicion = [0, 1]
    tablero.colocar_pieza(pieza, posicion)
    assert (tablero.tablero == respuesta2)
    tablero.borrar_pieza(pieza, posicion)
    assert(tablero.tablero == respuesta)

def test_looptesting_3():
    # Caso en el que el bucle se ejecuta una vez
    tablero = Tablero(5,5)
    respuesta = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    respuesta2 = [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    pieza = [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]
    posicion = [0, 0]
    tablero.colocar_pieza(pieza, posicion)
    assert (tablero.tablero == respuesta2)
    tablero.borrar_pieza(pieza, posicion)
    assert(tablero.tablero == respuesta)
