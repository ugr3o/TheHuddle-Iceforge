class Carta:
    # listas de clase con todos los palos y valores posibles de una baraja estándar
    PALOS = ["♠️", "♥️", "♦️", "♣️"]
    VALORES = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    def __init__(self, palo, valor):
        self.palo = palo
        self.valor = valor

    def obtener_puntos(self):
        # figuras valen 10, el As vale 11 (puede ajustarse en calcular_puntos), el resto su valor numérico
        if self.valor in ["J", "Q", "K"]:
            return 10
        elif self.valor == "A":
            return 11
        else:
            return int(self.valor)

    def __str__(self):
        # representación legible: valor + palo, ej: "A♠️"
        return f"{self.valor}{self.palo}"
