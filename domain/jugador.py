from domain.participante import Participante
from ui.consola import Consola

class Jugador(Participante):

    def __init__(self, nombre, saldo):
        super().__init__(nombre, saldo)  # pasa nombre y saldo al padre

    def jugar_turno(self, mazo):
        # el jugador elige acción en cada iteración hasta plantarse o pasarse
        while True:
            Consola.mostrar_mano(self)
            # si ya tiene 21 se planta automáticamente
            if self.calcular_puntos() == 21:
                print("¡21! Plantado automáticamente.")
                return "plantarse"
            opcion = Consola.pedir_accion()
            if opcion == 1:
                self.agregar_carta(mazo.repartir())
                if self.calcular_puntos() > 21:
                    Consola.mostrar_mano(self)  # muestra la mano con la carta que lo pasó
                    return "pasado"
            elif opcion == 2:
                return "plantarse"

    def __str__(self):
        return f"{self._nombre} | Saldo: {self.obtener_saldo()} | Puntos: {self.calcular_puntos()}"
