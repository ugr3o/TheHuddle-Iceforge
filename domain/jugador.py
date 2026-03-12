from domain.participante import Participante
from ui.consola import Consola
class Jugador(Participante):

    def __init__(self,nombre,saldo):
        super().__init__(nombre)
        self.__saldo = saldo # doble __ para que sea mas dificil de acceder o modificar privado
        self.__apuesta = 0
    
    def realizar_apuesta(self,monto):
        if monto > self.__saldo:
            print("No tienes saldo suficiente")
        else:
            self.__apuesta = monto
            self.__saldo -= monto 

    def ganar_apuesta(self):
        self.__saldo += self.__apuesta * 2

    def empate(self):
        self.__saldo += self.__apuesta
    
    def obtener_apuesta(self):
        return self.__apuesta
    
    def obtener_saldo(self):
        return self.__saldo
    
    def jugar_turno(self, mazo):
        while True:
            Consola.mostrar_mano(self)
            opcion = Consola.pedir_accion()
            if opcion == 1:
                self.agregar_carta(mazo.repartir())
                if self.calcular_puntos() > 21:
                    Consola.mostrar_resultado(f"{self._nombre} se pasó de 21!")
                    return "pasado"
            elif opcion == 2:
                return "plantarse"
            else:
                Consola.mostrar_resultado("Opción inválida")

    def __str__(self):
        return f"{self._nombre}{self.__saldo}{self.calcular_puntos()}"