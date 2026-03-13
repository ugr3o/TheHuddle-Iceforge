from domain.carta import Carta
import random

class Mazo:

    def __init__(self):
        self._cartas = []  # lista privada que contiene los 52 objetos Carta
        self._generar_cartas()

    def _generar_cartas(self):
        # combinación de todos los palos con todos los valores = 52 cartas
        for palo in Carta.PALOS:
            for valor in Carta.VALORES:
                self._cartas.append(Carta(palo, valor))

    def barajar(self):
        # mezcla aleatoriamente las cartas in-place
        random.shuffle(self._cartas)

    def repartir(self):
        # devuelve y elimina la última carta de la lista (simula sacar del tope)
        return self._cartas.pop()

    def cartas_restantes(self):
        return len(self._cartas)
