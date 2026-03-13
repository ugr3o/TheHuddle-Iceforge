from domain.participante import Participante
from ui.consola import Consola

class Jugador(Participante):

    def __init__(self, nombre, saldo):
        super().__init__(nombre)
        self.__saldo = saldo   # doble __ para encapsulamiento fuerte
        self.__apuesta = 0

    def realizar_apuesta(self, monto):
        if monto > self.__saldo:
            print("No tienes saldo suficiente")
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

    def jugar_turno(self, mazo):
        # el jugador elige acción en cada iteración hasta plantarse o pasarse
        while True:
            Consola.mostrar_mano(self)
            opcion = Consola.pedir_accion()
            if opcion == 1:
                self.agregar_carta(mazo.repartir())
                if self.calcular_puntos() > 21:
                    return "pasado"
            elif opcion == 2:
                return "plantarse"

    def __str__(self):
        return f"{self._nombre} | Saldo: {self.__saldo} | Puntos: {self.calcular_puntos()}"
