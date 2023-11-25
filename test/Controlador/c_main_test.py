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

class TestPlayGame():
    @patch('builtins.input', side_effect=['s', 'q'])
    @patch('builtins.print')
    def test_basic_flow(self, mock_print, mock_input):
        controlador.playGame("tst")
        mock_print.assert_any_call('-----------------------------------TETRIS GAME-----------------------------------')

    @patch('builtins.input', side_effect=['x', 'q'])
    @patch('builtins.print')
    def test_invalid_input(self, mock_print, mock_input):
        controlador.playGame("tst")
        mock_print.assert_any_call('Invalid input')

    @patch('builtins.input', side_effect=['s', 'k', 'x', 's', 's', 's', 's', 's', 's', 's', 's', 's'])
    @patch('builtins.print')
    def test_gameover(self, mock_print, mock_input):
        controlador.playGame("tst")
        mock_print.assert_any_call('Thank you for playing!')