import src.Controlador.c_main as controlador

tecla = "l"
def test_start(tecla): #Si le damos una tecla o nombre no aceptado, debería salir ERROR.
    controlador.start(tecla)