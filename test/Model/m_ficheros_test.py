import src.Model.m_ficheros as ficheros

nombre = "MATIES"
puntuacion = "200"
def test_escribirFichero(): #Test para revisar que se escribe bien la puntuación y nombre en el historial
    ficheros.escribirFichero(nombre, puntuacion)