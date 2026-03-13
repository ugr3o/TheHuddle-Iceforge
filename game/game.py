from domain.mazo import Mazo
from domain.dealer import Dealer
from domain.jugador import Jugador
from domain.jugadorBot import Jugadorbot
from ui.consola import Consola

class Game():

    def __init__(self):
        # se inicializan los objetos del juego
        self.mazo = Mazo()
        self.dealer = Dealer("Dealer")
        self.jugadorbot = Jugadorbot("Juan", 10000)

    def iniciar(self):
        # se piden los datos del jugador y se arranca la primera ronda
        nombre = Consola.pedir_nombre()
        saldo = Consola.pedir_saldo()
        self.jugador = Jugador(nombre, saldo)
        self.mazo.barajar()

        # loop principal: se repite mientras el jugador quiera seguir
        continuar = True
        while continuar:
            self._jugar_ronda()
            opcion = Consola.pedir_continuar()
            if opcion == 2:
                continuar = False

        Consola.mostrar_fin()

    def _jugar_ronda(self):
        # si quedan pocas cartas se reinicia el mazo
        if self.mazo.cartas_restantes() < 6:
            self.mazo = Mazo()
            self.mazo.barajar()

        # se limpian las manos de todos los participantes para la nueva ronda
        self.jugador.limpiar_mano()
        self.jugadorbot.limpiar_mano()
        self.dealer.limpiar_mano()

        # el jugador realiza su apuesta antes de recibir cartas
        monto = Consola.pedir_apuesta(self.jugador.obtener_saldo())
        self.jugador.realizar_apuesta(monto)

        # el bot apuesta una cantidad fija automáticamente
        self.jugadorbot.realizar_apuesta(400)

        # se reparten 2 cartas a cada participante
        for _ in range(2):
            self.jugador.agregar_carta(self.mazo.repartir())
            self.jugadorbot.agregar_carta(self.mazo.repartir())
            self.dealer.agregar_carta(self.mazo.repartir())

        # al inicio solo se muestra la carta visible del dealer (regla del blackjack)
        Consola.mostrar_carta_visible_dealer(self.dealer)

        # turno del jugador humano
        resultado_jugador = self.jugador.jugar_turno(self.mazo)

        # turno del bot (su lógica es interna, no necesita input)
        self.jugadorbot.jugar_turno(self.mazo)

        # el dealer solo juega si el jugador no se pasó
        if resultado_jugador != "pasado":
            self.dealer.jugar_turno(self.mazo)

        # se revela la mano completa del dealer al final de la ronda
        print("\n--- Resultado de la ronda ---")
        Consola.mostrar_mano(self.dealer)

        # se determina el ganador de la ronda
        self._determinar_ganador(resultado_jugador)

        # se muestra el saldo actualizado del jugador humano
        print(f"Saldo actual de {self.jugador.obtener_nombre()}: {self.jugador.obtener_saldo()}")

    def _determinar_ganador(self, resultado_jugador):
        # si el jugador se pasó de 21 pierde automáticamente
        if resultado_jugador == "pasado":
            Consola.mostrar_resultado(f"{self.jugador.obtener_nombre()} perdió (se pasó de 21)")
        else:
            # si no se pasó se evalúa contra el dealer normalmente
            self._evaluar_resultado(self.jugador)

        # el bot siempre se evalúa, independientemente del resultado del jugador humano
        Consola.mostrar_mano(self.jugadorbot)
        self._evaluar_resultado(self.jugadorbot)

    def _evaluar_resultado(self, jugador):
        puntos_jugador = jugador.calcular_puntos()
        puntos_dealer = self.dealer.calcular_puntos()

        # si el jugador se pasó de 21 pierde
        if puntos_jugador > 21:
            Consola.mostrar_resultado(f"{jugador.obtener_nombre()} perdió (se pasó de 21)")

        # si el dealer se pasó de 21 el jugador gana
        elif puntos_dealer > 21:
            Consola.mostrar_resultado(f"{jugador.obtener_nombre()} ganó (el dealer se pasó)")
            jugador.ganar_apuesta()

        # si el jugador tiene más puntos que el dealer gana
        elif puntos_jugador > puntos_dealer:
            Consola.mostrar_resultado(f"{jugador.obtener_nombre()} ganó ({puntos_jugador} vs {puntos_dealer})")
            jugador.ganar_apuesta()

        # si el jugador tiene menos puntos que el dealer pierde
        elif puntos_jugador < puntos_dealer:
            Consola.mostrar_resultado(f"{jugador.obtener_nombre()} perdió ({puntos_jugador} vs {puntos_dealer})")

        # empate: se devuelve la apuesta
        else:
            Consola.mostrar_resultado(f"{jugador.obtener_nombre()} y {self.dealer.obtener_nombre()} empataron ({puntos_jugador})")
            jugador.empate()
