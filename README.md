# 🃏 Blackjack — Python POO

Juego de Blackjack para consola desarrollado en Python aplicando los cuatro pilares de la Programación Orientada a Objetos: **Abstracción, Herencia, Polimorfismo y Encapsulamiento**.

---

## 📁 Estructura del proyecto

```
blackjack/
├── main.py               ← punto de entrada
├── domain/
│   ├── carta.py          ← entidad Carta
│   ├── mazo.py           ← generador y gestor de la baraja
│   ├── participante.py   ← clase base abstracta
│   ├── jugador.py        ← jugador humano
│   ├── jugadorBot.py     ← jugador automático
│   └── dealer.py         ← crupier
├── game/
│   └── game.py           ← motor del juego
└── ui/
    └── consola.py        ← interfaz de consola
```

El código está separado en **3 zonas lógicas**:
- `domain/` → entidades y reglas del juego
- `game/` → coordinación del flujo
- `ui/` → todo lo que se imprime y se lee por consola

---

## 🚀 Cómo ejecutar

```bash
python main.py
```

---

## 🎮 Cómo se juega

1. Ingresás tu nombre y saldo inicial
2. Apostás antes de cada ronda
3. Se reparten 2 cartas a cada participante
4. El dealer muestra solo una carta al inicio
5. Elegís pedir carta (1) o plantarte (2)
6. El bot y el dealer juegan automáticamente
7. Se comparan los puntos y se determina el ganador
8. Podés seguir jugando mientras tengas saldo

**Reglas:**
- Las figuras (J, Q, K) valen 10
- El As vale 11, pero se revalúa a 1 si superás 21
- El dealer pide carta mientras tenga menos de 17
- Si superás 21 perdés automáticamente

---

## 🧱 Diseño POO

### Abstracción
`Participante` es una clase abstracta que modela el concepto de "cualquier entidad que participa en el juego" sin entrar en los detalles de cada una. Define el contrato que todas las subclases deben cumplir.

```python
class Participante(ABC):
    @abstractmethod
    def jugar_turno(self):
        pass  # cada subclase define cómo juega
```

### Herencia
`Jugador`, `Jugadorbot` y `Dealer` heredan de `Participante` y reutilizan su lógica compartida sin reescribirla.

```
Participante (ABC)
├── Jugador
├── Jugadorbot
└── Dealer
```

Lógica heredada y reutilizada por las tres subclases:
- `calcular_puntos()` — suma la mano con lógica del As
- `agregar_carta()` — recibe una carta del mazo
- `limpiar_mano()` — vacía la mano al inicio de cada ronda
- `realizar_apuesta()` — descuenta la apuesta del saldo
- `ganar_apuesta()` — suma la ganancia al saldo
- `obtener_mano()` — devuelve copia de la mano

### Polimorfismo
El mismo método `jugar_turno()` tiene comportamiento distinto en cada clase:

| Clase | Comportamiento |
|---|---|
| `Jugador` | Le pregunta al usuario qué hacer |
| `Jugadorbot` | Pide carta automáticamente hasta llegar a 17 |
| `Dealer` | Pide carta mientras tenga menos de 17 |

### Encapsulamiento
Los atributos críticos están protegidos y solo se acceden mediante métodos:

```python
# en Participante
self.__saldo   = saldo   # privado — solo accesible por obtener_saldo()
self.__apuesta = 0       # privado — solo accesible por obtener_apuesta()
self._mano     = []      # protegido — accesible por obtener_mano() que devuelve copia
```

---

## 📋 Archivos explicados

### `carta.py`
Representa una carta de la baraja. Tiene atributos de clase (`PALOS`, `VALORES`) compartidos por todas las instancias, y atributos de instancia (`palo`, `valor`) propios de cada carta.

### `mazo.py`
Genera la baraja completa (52 cartas) combinando todos los palos con todos los valores. Usa `pop()` para repartir, lo que simula sacar del tope de la baraja.

### `participante.py`
Clase base abstracta. Define el estado y comportamiento común a todos los participantes. No se puede instanciar directamente. Contiene el `@abstractmethod jugar_turno()` que obliga a todas las subclases a implementar su propia lógica de turno.

### `jugador.py`
Jugador humano. Su `jugar_turno()` muestra la mano e interactúa con el usuario en cada iteración. Se planta automáticamente si llega a 21.

### `jugadorBot.py`
Jugador automático. Su `jugar_turno()` sigue la misma lógica que el dealer: pide carta mientras tenga menos de 17.

### `dealer.py`
Crupier. No apuesta. Su `jugar_turno()` sigue la regla estándar del Blackjack: pide carta mientras tenga menos de 17, se planta en 17 o más.

### `game.py`
Motor del juego. Coordina el flujo de cada ronda sin contener lógica de dominio ni imprimir directamente. Toda la UI pasa por `Consola`.

### `consola.py`
Toda la interfaz de consola. Solo imprime y lee inputs. No toma ninguna decisión de juego. Todos sus métodos son `@staticmethod` porque no necesitan estado propio.

---

## 👤 Autor
Hugo Franco
