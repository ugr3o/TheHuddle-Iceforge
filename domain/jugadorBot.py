from domain.participante import Participante

class Jugadorbot(Participante):

    def __init__(self, nombre, saldo):
        super().__init__(nombre, saldo)  # pasa nombre y saldo al padre

    def jugar_turno(self, mazo):
        # el bot sigue pidiendo cartas mientras tenga menos de 17, igual que el dealer
        while self.calcular_puntos() < 17:
            self.agregar_carta(mazo.repartir())
        return "plantarse"

    def __str__(self):
        return f"{self._nombre} | Saldo: {self.obtener_saldo()} | Puntos: {self.calcular_puntos()}"
