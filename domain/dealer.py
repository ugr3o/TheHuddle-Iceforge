from domain.participante import Participante

class Dealer(Participante):

    # funcion jugar turno, mientras los puntos de sus cartas no sea >= a 17 sigue sacando cartas
    def jugar_turno(self, mazo):
        while self.calcular_puntos() < 17:
            self.agregar_carta(mazo.repartir()) # se agrega una carta del maso y se reciben los puntos hasta que igual a 17
        
    def __str__(self):
        return f"{self._nombre}{self.calcular_puntos()}"