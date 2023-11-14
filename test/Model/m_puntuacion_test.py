from src.Model.m_puntuacion import Punts

#con este test vemos problemas con los valores negativos.
def test_inicializacion():
    # Partició equivalent, valors forntera, valors limits [20, MAX_CAPACITY_INT]
    puntos_min = Punts(20)
    assert(puntos_min.get_puntos() == 0 & puntos_min.maximo == 20)


def test_sumar_puntos():

    puntos = Punts(100)
    punts_test1 = puntos.sumar_puntos(30)
    assert (punts_test1 == 30), "[ERROR]: No suma correctamente"
    punts_test2 = puntos.sumar_puntos(40)
    assert (punts_test2 == 70), "[ERROR]: No suma correctamente quando hay puntos."



def test_puntuacion_maxima():
    m_puntos = Punts(50)
    m_puntos.puntos = 49
    assert(m_puntos.puntuacion_maxima() == False), "Puntuación maxima"

def test_get_puntos():
    puntos = Punts(50)
    assert(puntos.get_puntos() == 0), "Puntos iniciales no son 0"
    puntos.puntos = 50
    assert(puntos.get_puntos() == 50), "No se han añadido los puntos correctamente"

#def test_puntuacio_particions():
    #(-algo a 19) (20 a maxvalorint) (mas del max valor int)


#def test_puntuacio_fronteras_limits():
    #(-algo a 19) (20 a maxvalorint) (mas del max valor int)