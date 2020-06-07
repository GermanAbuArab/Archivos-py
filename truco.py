import random

palo = ["Espada", "Basto", "Copa", "Oro"]
numeros = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
piezasNum = [2, 4, 5, 10, 11]


def truco():
    mazo = [(i, j) for i in numeros for j in palo]
    manos = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
    cartasDeLaRonda = random.sample(mazo, 13)
    for k in range(0, 3):
        for l in range(0, 4):
            manos[l][k] = cartasDeLaRonda[len(cartasDeLaRonda) - 1]
            cartasDeLaRonda.pop(-1)
    muestra = cartasDeLaRonda[-1]
    puntos(manos, muestra)


def puntos(manos, muestra):
    print(f"La muestra es {muestra}")
    piezas = [(i, muestra[1]) for i in piezasNum]
    for i in range(0, len(piezasNum)):
        if muestra[0] == piezasNum[i]:
            piezas[i] = (12, muestra[1])
    jugador = 1
    for j in manos:
        print(f"El jugador {jugador} tinen las cartas:{j}")
        if flor(j, piezas)[0]:
            print(f"{flor(j, piezas)[1]} puntos de FLOR")
        else: # si no tiene flor si o si tiene Envido
            print(f"{envido(j,piezas)} puntos de ENVIDO")
        jugador += 1



def flor(mano, piezas):
    cantMatas = 0
    for i in range(3):
        if mano[i] in piezas:
            cantMatas += 1
    if cantMatas > 1:
        puntaje = calcular(mano, piezas)
        if cantMatas == 3:
            puntaje -= 40
        else:
            puntaje -= 20
        return (True, puntaje)
    elif cantMatas == 0:  # aun puede ser 3 del mismo palo
        if (mano[0][1] == mano[1][1] and mano[2][1] == mano[1][1]):
            return (True, calcular(mano, piezas))
        else:
            return (False, 0)
    else:  # aun puede tener 2 del mismo palo
        if mano[0] in piezas:
            if mano[1][1] == mano[2][1]:
                return (True, calcular(mano, piezas))
            else:
                return (False, 0)
        elif mano[1] in piezas:
            if mano[2][1] == mano[0][1]:
                return (True, calcular(mano, piezas))
            else:
                return (False, 0)
        elif mano[2] in piezas:
            if mano[0][1] == mano[1][1]:
                return (True, calcular(mano, piezas))
            else:
                return (False, 0)
        else:
            return (False, 0)


def calcular(mano, piezas):
    puntaje = 0
    for carta in mano:
        if carta == piezas[0]:
            puntaje += 30
        elif carta == piezas[1]:
            puntaje += 29
        elif carta == piezas[2]:
            puntaje += 28
        elif carta == piezas[3]:
            puntaje += 27
        elif carta == piezas[4]:
            puntaje += 27
        else:
            if carta[0] < 10:
                puntaje += carta[0]
    return puntaje

def envido(mano, piezas):
    for i in mano:
        if i in piezas: # si tiene una pieza entonces no tiene ninguna repetida
            return calcular(mano,piezas)
        if mano[1][1] == mano[2][1] or mano[0][1] == mano[2][1] or mano[1][1] == mano[0][1]:
            return calcular(mano,piezas)+20
        else:
            return calcular(mano,piezas)



def main():
    truco()


if __name__ == '__main__':
    main()
