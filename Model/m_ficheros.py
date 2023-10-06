def leerFichero():
    with open('/Users/matieslopezalarcon/Documents/GitHub/Tetris-Game/historial.txt') as f:
        texto = f.readlines()
        return texto
print(leerFichero())