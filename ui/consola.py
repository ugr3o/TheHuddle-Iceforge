class Consola:
    @staticmethod
    def pedir_nombre():
        return input("Ingresa tu nombre: ")

    @staticmethod
    def pedir_saldo():
        # se repite hasta recibir un número válido mayor a 0
        while True:
            try:
                saldo = int(input("Ingrese su saldo: "))
                if saldo > 0:
                    return saldo
                print("El saldo debe ser mayor a 0.")
            except ValueError:
                print("Ingrese un número válido.")

    @staticmethod
    def pedir_apuesta(saldo_disponible):
        # valida que la apuesta sea un número positivo y no supere el saldo
        while True:
            try:
                monto = int(input(f"¿Cuánto querés apostar? (Saldo: {saldo_disponible}): "))
                if monto <= 0:
                    print("La apuesta debe ser mayor a 0.")
                elif monto > saldo_disponible:
                    print(f"No tenés saldo suficiente. Máximo: {saldo_disponible}")
                else:
                    return monto
            except ValueError:
                print("Ingrese un número válido.")

    @staticmethod
    def pedir_accion():
        # valida que la opción sea 1 o 2
        while True:
            try:
                opcion = int(input("1- Pedir carta\n2- Plantarse: "))
                if opcion in [1, 2]:
                    return opcion
                print("Opción inválida. Ingresá 1 o 2.")
            except ValueError:
                print("Ingresá un número.")

    @staticmethod
    def pedir_continuar():
        # valida que la opción sea 1 o 2
        while True:
            try:
                opcion = int(input("¿Deseás seguir jugando?\n1- Sí\n2- No: "))
                if opcion in [1, 2]:
                    return opcion
                print("Opción inválida. Ingresá 1 o 2.")
            except ValueError:
                print("Ingresá un número.")

    @staticmethod
    def mostrar_resultado(mensaje):
        print(mensaje)

    @staticmethod
    def mostrar_fin():
        print("Fin del juego.")

    @staticmethod
    def mostrar_mano(participante):
        # muestra todas las cartas y el total de puntos del participante
        cartas = " | ".join(str(carta) for carta in participante._mano)
        print(f"{participante.obtener_nombre()} → {cartas} | Puntos: {participante.calcular_puntos()}")

    @staticmethod
    def mostrar_carta_visible_dealer(dealer):
        # al inicio solo se muestra la primera carta del dealer, la segunda queda oculta
        carta_visible = str(dealer._mano[0])
        print(f"{dealer.obtener_nombre()} → {carta_visible} | ?? (una carta oculta)")
