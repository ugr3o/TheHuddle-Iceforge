class Carta:
    PALOS = ["♠️", "♥️", "♦️", "♣️"] #palos posibles para cada valor
    VALORES = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"] # valores de las cartas como str
    def __init__(self,palo,valor): # se utiliza el __init__ por convencion y el self para indicar que le pertenece
        self.palo = palo
        self.valor = valor

    def obtener_puntos(self):
        if self.valor in ["J","Q","K"]: # estos valores son 10
            return 10
        elif self.valor == "A": #
            return 11
        else:
            return int(self.valor)

    
    def __str__(self):
        return f"{self.valor}{self.palo}"
