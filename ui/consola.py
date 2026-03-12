class Consola:

    @staticmethod
    def pedir_nombre():
        return input("Ingresa tu nombre: ")

    @staticmethod
    def pedir_saldo():
        return int(input("Ingrese su saldo: "))

    @staticmethod
    def pedir_apuesta():
        return int(input("¿Cuánto querés apostar? "))

    @staticmethod
    def pedir_accion():
        return int(input("1- Pedir carta \n 2- Plantarse: "))

    @staticmethod
    def pedir_continuar():
        return int(input("Desea seguir jugando? \n 1- Si \n 2- No: "))

    @staticmethod
    def mostrar_resultado(mensaje):
        print(mensaje)

    @staticmethod
    def mostrar_fin():
        print("Fin del juego")
    
    @staticmethod
    def mostrar_mano(participante):
        cartas = " | ".join(str(carta) for carta in participante._mano)
        print(f"{participante.obtener_nombre()} → {cartas} | Puntos: {participante.calcular_puntos()}")