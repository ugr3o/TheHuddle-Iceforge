from domain.mazo import Mazo
from domain.dealer import Dealer
from domain.jugador import Jugador
from domain.jugadorBot import Jugadorbot
from ui.consola import Consola

class Game():

    def __init__(self):
        self.mazo = Mazo()
        self.dealer = Dealer("Dealer")
        self.jugadorbot = Jugadorbot("Juan", 10000)
        
    def iniciar(self):
        nombre = Consola.pedir_nombre()
        saldo = Consola.pedir_saldo()
        self.jugador = Jugador(nombre, saldo)
        self.mazo.barajar()
        self._jugar_ronda()
        
    def _jugar_ronda(self):
        if self.mazo.cartas_restantes() < 6:
            self.mazo = Mazo()
            self.mazo.barajar()

        self.jugador.limpiar_mano()
        self.jugadorbot.limpiar_mano()
        self.dealer.limpiar_mano()

        monto = Consola.pedir_apuesta()
        self.jugador.realizar_apuesta(monto)

        contador = 0
        while contador < 2:
            self.jugador.agregar_carta(self.mazo.repartir())
            self.jugadorbot.agregar_carta(self.mazo.repartir())
            self.dealer.agregar_carta(self.mazo.repartir())
            contador += 1
        
        Consola.mostrar_mano(self.dealer)
        resultado_jugador = self.jugador.jugar_turno(self.mazo)
        self.jugadorbot.jugar_turno(self.mazo)
        self.dealer.jugar_turno(self.mazo)
        self._determinar_ganador(resultado_jugador)

        opcion = Consola.pedir_continuar()
        if opcion == 1:
            self._jugar_ronda()
        elif opcion == 2:
            Consola.mostrar_fin()
            
    def _determinar_ganador(self, resultado_jugador):
        if resultado_jugador == "pasado":
            Consola.mostrar_resultado(f"{self.jugador.obtener_nombre()} perdió, se pasó de 21")
        else:
            self._evaluar_resultado(self.jugador)
        self._evaluar_resultado(self.jugadorbot)  # el bot siempre se evalúa independiente
            
    def _evaluar_resultado(self, jugador):
        if jugador.calcular_puntos() > 21:
            Consola.mostrar_resultado(f"{jugador.obtener_nombre()} perdió")

        elif self.dealer.calcular_puntos() > 21:
            Consola.mostrar_resultado(f"{self.dealer.obtener_nombre()} perdió")
            jugador.ganar_apuesta()
        
        elif jugador.calcular_puntos() > self.dealer.calcular_puntos():
            Consola.mostrar_resultado(f"{jugador.obtener_nombre()} ganó")
            jugador.ganar_apuesta()
        
        elif jugador.calcular_puntos() < self.dealer.calcular_puntos():
            Consola.mostrar_resultado(f"{jugador.obtener_nombre()} perdió")

        elif jugador.calcular_puntos() == self.dealer.calcular_puntos():
            Consola.mostrar_resultado(f"{jugador.obtener_nombre()} y {self.dealer.obtener_nombre()} empataron")
            jugador.empate()
        
#     _determinar_ganador():
#         - obtener puntos del jugador, dealer y bot
#         - si jugador > 21 → perdió (se pasó)
#         - si dealer > 21 → ganó el jugador
#         - si jugador > dealer → ganó el jugador
#         - si jugador < dealer → perdió el jugador
#         - si jugador == dealer → empate
#         - actualizar saldos según resultado




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

