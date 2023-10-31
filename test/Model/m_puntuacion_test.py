from src.Model.m_puntuacion import Punts

#con este test vemos problemas con los valores negativos.
def test_inicializacion():

    puntos = Punts(-100)
    assert(puntos.get_puntos() == 0)
    assert(puntos.maximo == 100)

def test_sumar_puntos():

    puntos = Punts(100)
    punts_test1 = puntos.sumar_puntos(30)
    if punts_test1 == 30:
        punts_test2 = puntos.sumar_puntos(40)
        if punts_test2 == 70:
            print("PASSED TEST")
        else:
            print("[ERROR]: No suma correctamente quando hay puntos.")
    else:
        print("[ERROR]: No suma correctamente")



def test_puntuacion_maxima():
    m_puntos = Punts(50)
    m_puntos.puntos = 45
    if(m_puntos.puntuacion_maxima() == True):
        print("Se ha pasado del maximo, paramos el juego")
    else:
        print("No nos hemos pasado ni llegado al maximo")

def test_get_puntos():
    puntos = Punts(50)
    assert(puntos.get_puntos() == 0)
    puntos.puntos = 50
    assert(puntos.get_puntos() == 50)