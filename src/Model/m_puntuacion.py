class Punts:
    def __init__(self, maximo):
        self.puntos = 0
        self.maximo = maximo

    def sumar_puntos(self,puntos):
        self.puntos += puntos
        return self.puntos

    def puntuacion_maxima(self):
        return True if self.puntos >= self.maximo else False

    def get_puntos(self):
        return self.puntos
