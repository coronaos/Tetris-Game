from src.Model.m_puntuacion import Punts
import random

'''
Test de inicialización de Puntuación.
Comprobar que no de error al intorducir negativos
'''
def test_inicializacion():
    puntos_min = Punts(20)
    assert(puntos_min.get_puntos() == 0 & puntos_min.maximo == 20)

    puntos_neg = Punts(-20)
    assert (puntos_neg.get_puntos() == 0 & puntos_neg.maximo == 20)

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

def test_puntuacion_pairwise_testing():
    random1 = 1
    random2 = 1
    random3 = 1
    puntos = Punts(200)
    p = 20
    puntos.puntuacion_pairwise_testing(random1, random2, random3, p)
    assert (puntos.get_puntos() == 20)

    random1 = 1
    random2 = 2
    random3 = 2
    puntos = Punts(200)
    p = 20
    puntos.puntuacion_pairwise_testing(random1, random2, random3, p)
    assert (puntos.get_puntos() == 20)

    random1 = 2
    random2 = 1
    random3 = 2
    puntos = Punts(200)
    p = 20
    puntos.puntuacion_pairwise_testing(random1, random2, random3, p)
    assert (puntos.get_puntos() == 20)

    random1 = 2
    random2 = 2
    random3 = 1
    puntos = Punts(200)
    p = 20
    puntos.puntuacion_pairwise_testing(random1, random2, random3, p)
    assert (puntos.get_puntos() == 23)
