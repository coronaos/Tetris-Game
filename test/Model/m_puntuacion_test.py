from src.Model.m_puntuacion import Punts

"""
    def puntuacion_maxima(self):
        return True if self.puntos >= self.maximo else False

"""

def test_puntuacion_maxima():
    m_puntos = Punts(50)
    m_puntos.puntos = 45
    if(m_puntos.puntuacion_maxima() == True):
        print("Se ha pasado del maximo, paramos el juego")
    else:
        print("No nos hemos pasado ni llegado al maximo")