def laberinto(dimension, obstaculos):
    # La función que construye el laberinto se mantiene igual
    laberinto = []
    for i in range(dimension):
        fila = []
        for j in range(dimension):
            if tuple([i, j]) in obstaculos:
                fila.append('X')
            else:
                fila.append('0')
        laberinto.append(fila)
    return laberinto

def recorre_laberinto(laberinto):
    n = len(laberinto)  # Obtener la dimensión del laberinto
    fila = columna = 0  # Fila y columna iniciales
    movimientos = []  # Lista de movimientos

    while fila < n - 1 or columna < n - 1:
        if (len(movimientos) == 0 or movimientos[-1] != 'Arriba') and fila + 1 < n and laberinto[fila + 1][columna] != 'X':
            fila += 1
            movimientos.append('Abajo')
        elif (len(movimientos) == 0 or movimientos[-1] != 'Abajo') and fila - 1 >= 0 and laberinto[fila - 1][columna] != 'X':
            fila -= 1
            movimientos.append('Arriba')
        elif (len(movimientos) == 0 or movimientos[-1] != 'Izquierda') and columna + 1 < n and laberinto[fila][columna + 1] != 'X':
            columna += 1
            movimientos.append('Derecha')
        elif (len(movimientos) == 0 or movimientos[-1] != 'Derecha') and columna - 1 >= 0 and laberinto[fila][columna - 1] != 'X':
            columna -= 1
            movimientos.append('Izquierda')
        else:
            # No hay salida
            movimientos.append('No hay salida')
            break

    return movimientos

obstaculo = ((0, 1), (0, 2), (0, 3), (0, 4), (1, 1), (2, 1), (2, 3), (3, 3), (4, 0), (4, 1), (4, 2), (4, 3))
dimension = 5
lab = laberinto(dimension, obstaculo)

# Imprimir el laberinto
for i in lab:
    print(''.join(i))

# Llamar a la función recorre_laberinto y mostrar el resultado
resultado = recorre_laberinto(lab)
print("Resultado:")
for movimiento in resultado:
    print(movimiento)

# No cerramos la ventana
input("Presione Enter para salir")
