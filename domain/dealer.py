from domain.participante import Participante

class Dealer(Participante):

    def __init__(self, nombre):
        super().__init__(nombre)  # saldo=0 por defecto, el dealer no apuesta

    def jugar_turno(self, mazo):
        # el dealer sigue sacando cartas hasta llegar a 17 o más (regla estándar)
        while self.calcular_puntos() < 17:
            self.agregar_carta(mazo.repartir())

    def __str__(self):
        return f"{self._nombre}: {self.calcular_puntos()}"