import sys
import src.Controlador.c_main as controlador
from io import StringIO
from unittest.mock import patch

def test_start_fail(): #Si le damos una tecla o nombre no aceptado, debería salir ERROR.
    tecla = "l"
    captura_print = StringIO()
    sys.stdout = captura_print
    controlador.start(tecla)
    sys.stdout = sys.__stdout__

    resultado = captura_print.getvalue().strip()

    assert(resultado == "[ERROR]: Press 1, 2 or 3 to navegate in the menu.")
def test_start_passed():  # Si le damos una tecla o nombre no aceptado, debería salir ERROR.

    tecla = "3"
    with patch('builtins.exit') as mock_exit:
        controlador.start(tecla)

    # Verificar si exit fue llamado
    mock_exit.assert_called()

