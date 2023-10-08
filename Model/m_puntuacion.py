class Punts:
    def __init__(self, maximo):
        self.puntos = 0
        self.maximo = maximo

    def sumar_puntos(self,puntos):
        self.puntos += puntos
        return self.puntos

    def puntuacion_maxima(self):
        return (true if self.puntos >= self.maximo else false)


    def get_puntos(self):
        return self.puntos
