from abc import ABC, abstractmethod

class Participante(ABC): # abc abstract base casses
    def __init__(self,nombre):
        self._nombre = nombre
        self._mano = []
    
    def agregar_carta(self, carta):
        self._mano.append(carta)

    def calcular_puntos(self): #calculamos los valores de las cartas
        total = 0
        ases = 0
        for carta in self._mano:
            total += carta.obtener_puntos()
            if carta.valor == "A":
                ases += 1
        while total > 21 and ases > 0:
            total -= 10
            ases -= 1
        return total
    
    def limpiar_mano(self):
        self._mano.clear()
    
    def obtener_nombre(self):
        return self._nombre
    
    @abstractmethod
    def jugar_turno(self):
        pass

    def __str__(self):
        return f"{self._nombre}{self.calcular_puntos()}"
