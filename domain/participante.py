from abc import ABC, abstractmethod

# clase base abstracta: define el contrato que deben cumplir Jugador, Dealer y JugadorBot
class Participante(ABC):

    def __init__(self, nombre, saldo=0):
        self._nombre = nombre
        self._mano = []          # lista de cartas recibidas en la ronda actual
        self.__saldo = saldo     # privado: solo se accede por getters y métodos propios
        self.__apuesta = 0

    def agregar_carta(self, carta):
        self._mano.append(carta)

    def calcular_puntos(self):
        # suma los puntos de todas las cartas en mano
        total = 0
        ases = 0
        for carta in self._mano:
            total += carta.obtener_puntos()
            if carta.valor == "A":
                ases += 1
        # si se pasa de 21 y hay ases, se revalúan de 11 a 1 para evitar pasarse
        while total > 21 and ases > 0:
            total -= 10
            ases -= 1
        return total

    def limpiar_mano(self):
        # se vacía la mano al inicio de cada nueva ronda
        self._mano.clear()

    def obtener_nombre(self):
        return self._nombre

    def obtener_mano(self):
        # devuelve copia para que nadie pueda modificar la mano original desde afuera
        return list(self._mano)

    def realizar_apuesta(self, monto):
        if monto > self.__saldo:
            print("No tenés saldo suficiente")
        else:
            self.__apuesta = monto
            self.__saldo -= monto

    def ganar_apuesta(self):
        # al ganar se recupera la apuesta y se suma la ganancia (pago 1:1)
        self.__saldo += self.__apuesta * 2

    def empate(self):
        # en empate se devuelve la apuesta sin ganancia
        self.__saldo += self.__apuesta

    def obtener_apuesta(self):
        return self.__apuesta

    def obtener_saldo(self):
        return self.__saldo

    @abstractmethod
    def jugar_turno(self):
        # cada subclase define su propia lógica de turno
        pass

    def __str__(self):
        return f"{self._nombre}: {self.calcular_puntos()}"
