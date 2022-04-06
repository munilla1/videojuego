import matplotlib.pyplot as plt

import mapa_de_videojuego as m

import random

lista_de_coordenadas = [
    [0, 0],
    [0, 0.5],
    [0.2, -0.6],
    [0.28, 0.9],
    [0.5, 1.4],
    [0.52, -0.4],
]

factor_desvio = 0.3


def mapa_random(lista_de_coordenadas):
    lista_de_coordenadas_random = []
    for desviacion_estandar in lista_de_coordenadas:
        desviacion_tiro = desvia_el_tiro(desviacion_estandar)
        lista_de_coordenadas_random.append(desviacion_tiro)

    return lista_de_coordenadas_random


def maximo_abs(lista_de_coordenadas):
    maximo_total = 0
    for pareja_de_coordenadas in lista_de_coordenadas:
        maxim = abs(max(pareja_de_coordenadas))
        minim = abs(min(pareja_de_coordenadas))
        maximo_temporal = max(maxim, minim)
        if maximo_temporal > maximo_total:
            maximo_total = maximo_temporal

    return maximo_total


def definir_area_de_dibujo(lista_de_coordenadas):
    max_coord = maximo_abs(lista_de_coordenadas) + 1
    print(f"busca_máximo_coordenadas: [{max_coord}]")

    plt.xlim(-1 * max_coord, max_coord)
    plt.ylim(-1 * max_coord, max_coord)


def disparos_aleatorios(lista_de_coordenadas, color="b", pause=False):
    for pareja_de_coordenadas in lista_de_coordenadas:
        plt.plot(
            pareja_de_coordenadas[0], pareja_de_coordenadas[1], color=color, marker='o')
        plt.plot(0, 0, 'y+')
        if(pause):
            plt.pause(0.50)


def desvia_el_tiro(vieja_pareja):

    hipotenusa = ((vieja_pareja[0] ** 2 + vieja_pareja[1]**2) ** (1/2))
    desviacion_max = factor_desvio * hipotenusa

    x = vieja_pareja[0]
    y = vieja_pareja[1]

    aleat_x = random.uniform(-1, 1)
    aleat_y = random.uniform(-1, 1)

    new_x = x + (aleat_x * desviacion_max)
    new_y = y + (aleat_y * desviacion_max)

    nueva_pareja = [new_x, new_y]

    return nueva_pareja


def dispara(lista_de_coordenadas, color='b'):
    lista_de_coordenadas_random = mapa_random(lista_de_coordenadas)
    definir_area_de_dibujo(lista_de_coordenadas_random)
    disparos_aleatorios(lista_de_coordenadas, 'r')
    disparos_aleatorios(lista_de_coordenadas_random, color, True)
    plt.show()


if __name__ == '__main__':
    dispara(lista_de_coordenadas)
    