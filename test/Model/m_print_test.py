import sys
import src.Model.m_print as print
from src.Model.m_tablero import Tablero
from io import StringIO
def test_valores_normales():
    tablero = Tablero(5, 5)
    ficha = [[0, 1],
     [0, 1],
     [1, 1]]
    punts = "100"
    nom = "hola"
    captura_print = StringIO()
    sys.stdout = captura_print
    print.print_all(tablero.tablero, ficha, punts, nom)
    sys.stdout = sys.__stdout__

    resultado = captura_print.getvalue().strip()

    assert (resultado)