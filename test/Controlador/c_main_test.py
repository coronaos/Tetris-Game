import src.Controlador.c_main as controlador

def test_start(): #Si le damos una tecla o nombre no aceptado, debería salir ERROR.
    tecla = "l"
    controlador.start(tecla)