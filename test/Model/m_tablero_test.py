from src.Model.m_tablero import Tablero

#gracias a este test arreglamos que puedan poner negativos
def test_inicializacion():
    tablero = Tablero(-5, -10)
    if tablero.filas == -5:
        print("[ERROR]: Se inicializa negativo")
    else:
        print("TEST PASSED")