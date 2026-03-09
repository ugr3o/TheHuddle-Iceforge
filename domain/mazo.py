from domain.carta import Carta
import random

class Mazo:
    
    def __init__(self):
        self._cartas = [] # atributo privado
        self._generar_cartas()

    def _generar_cartas(self): # se indica que es una funcion privada(no se llama desde afuera)
        for palo in Carta.PALOS:
            for valor in Carta.VALORES:
                self._cartas.append(Carta(palo,valor)) #el producto de la iteracion entre el palo y el valor se juntan
    
    def barajar(self):
        random.shuffle(self._cartas)
    
    def repartir(self):
        return self._cartas.pop() #se obtiene el ultimo valor de la lista y al mismo tiempo se elimina

    def cartas_restantes(self):
        return len(self._cartas) # se retorna la cantidad de cartas restantes dentro del mazo