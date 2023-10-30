from src.Model.m_tablero import Tablero

#gracias a este test arreglamos que puedan poner negativos
def test_inicializacion():
    tablero = Tablero(-5, -10)
    if tablero.filas == -5:
        print("[ERROR]: Se inicializa negativo")
    else:
        print("TEST PASSED")

def test_tablero_lleno(): #Se introduce un 1 en la fila 0 para ver si la función detecta correctamente que has perdido.
    tablero = Tablero(5, 10)
    for i in tablero.tablero:
        i[0] = 1
    if(tablero.tablero_lleno(True) == True):
        print("Fin de partida")
    else:
        print("Aún no ha acabado")
