from domain.carta import Carta
from domain.mazo import Mazo
from domain.dealer import Dealer
from domain.jugador import Jugador
from domain.jugadorBot import Jugadorbot


class Game():

    def __init__(self):
        self.mazo = Mazo()
        self.dealer = Dealer("Dealer")
        self.jugadorbot = Jugadorbot("")
        

    def iniciar(self):
        nombre = input("Ingresa tu nombre: ")
        saldo = int(input("Ingrese su saldo: "))
        self.jugador = Jugador(nombre,saldo)
        self.jugadorbot = Jugadorbot()
        self.mazo.barajar()



        


        

# clase Game:

#     __init__:
#         - crear mazo
#         - crear dealer con nombre "Dealer"
#         - crear jugadorbot con nombre y saldo fijos
#         - jugador = None (todavía no sabemos el nombre)

#     iniciar():
#         - pedir nombre al usuario
#         - pedir saldo inicial al usuario
#         - crear jugador con esos datos
#         - barajar el mazo
#         - llamar a _jugar_ronda()
    
#     _jugar_ronda():
#         - limpiar manos de todos
#         - repartir 2 cartas a cada participante
#         - turno del jugador
#         - turno del bot
#         - turno del dealer
#         - llamar a _determinar_ganador()
#         - preguntar si quiere jugar otra ronda
#             - si → llamar a _jugar_ronda() de nuevo
#             - no → mostrar mensaje de fin

#     _repartir_iniciales():
#         - agregar 2 cartas al jugador
#         - agregar 2 cartas al dealer
#         - agregar 2 cartas al bot

#     _turno_jugador():
#         - mostrar mano del jugador
#         - mientras el jugador no se plante y no se pase de 21:
#             - llamar jugar_turno() del jugador
#             - si pide carta → repartir una carta
#             - si se planta → salir del loop

#     _determinar_ganador():
#         - obtener puntos del jugador, dealer y bot
#         - si jugador > 21 → perdió (se pasó)
#         - si dealer > 21 → ganó el jugador
#         - si jugador > dealer → ganó el jugador
#         - si jugador < dealer → perdió el jugador
#         - si jugador == dealer → empate
#         - actualizar saldos según resultado