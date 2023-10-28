import src.Model.m_ficheros as ficheros
"""
def escribirFichero(nombre, puntuacion):
    f = open(script_dir + "/historial.txt", "a+")
    f.write(f"\n {puntuacion} {nombre[0:3]}")
    f.close()
"""

nombre = "MATIES"
puntuacion = "200"
def test_escribirFichero(): #Test para revisar que se escribe bien la puntuación y nombre en el historial
    ficheros.escribirFichero(nombre, puntuacion)
