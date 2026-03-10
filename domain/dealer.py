from domain.participante import Participante

class Dealer(Participante):
    
    # funcion jugar turno, mientras los puntos de sus cartas no sea >= a 17 sigue sacando cartas

    def jugar_turno(self):
        while self.calcular_puntos() <= 17:
            return self.agregar_carta
        
    def __str__(self):
        return f"{self._nombre}{self.calcular_puntos()}"
            