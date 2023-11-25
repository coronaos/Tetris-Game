import sys
import src.Controlador.c_main as controlador
from io import StringIO
from unittest.mock import patch

'''
Test que comrpueba que si se pone una tecla erronea salte un error. 
'''
def test_start_fail():
    tecla = "l"
    captura_print = StringIO()
    sys.stdout = captura_print
    controlador.start(tecla)
    sys.stdout = sys.__stdout__

    #coge el print que realiza
    resultado = captura_print.getvalue().strip()

    assert(resultado == "[ERROR]: Press 1, 2 or 3 to navegate in the menu.")

'''
Test que comprueba que si apretamos tecla de exit, salga del juego
'''
def test_start_passed():

    tecla = "3"
    with patch('builtins.exit') as mock_exit:
        controlador.start(tecla)

    # Verificar si exit fue llamado
    mock_exit.assert_called()

'''
Classe creada para simular juego
'''
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

    '''Test del Path Coverage que comprueba que si apretamos la tecla "k", la pieza gire correctamente'''
    @patch('builtins.input', side_effect=['k'])
    @patch('builtins.print')
    def test_path_coverage(self, mock_print, mock_input):
        controlador.playGame("tst")
        mock_print.assert_any_call('Pieza girada correctamente')