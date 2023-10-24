
#  * Inspirado en el cuento 'Casa tomada' de Julio Cortázar

#  * Te encuentras explorando una mansión abandonada llena de habitaciones.
#  * En cada habitación tendrás que resolver un acertijo para poder avanzar a la siguiente.
#  * Tu misión es encontrar la habitación con la llave para escapar.
#  *
#  * Se trata de implementar un juego interactivo de preguntas y respuestas (T/F) por terminal.
#  *
#  * - 🏰 Casa: La mansión se corresponde con una estructura cuadrada 4 x 4
#  *   Las habitaciones de puerta y llave no tienen enigma.
#  *   (16 habitaciones, siendo una de entrada y otra donde están la llave)
#  *   Esta podría ser una representación:
#  *   🚪⬜️⬜️⬜️
#  *   ⬜️👻⬜️⬜️
#  *   ⬜️⬜️⬜️👻
#  *   ⬜️⬜️🔑⬜️
#  * - ❓ Enigmas: Cada habitación propone un enigma aleatorio que deberás responder con T para verdadero y F para falso.
#  *   Si no lo aciertas no podrás desplazarte y pierdes vidas.
#  * - 🧭 Movimiento: Si resuelves el enigma se te preguntará a donde quieres desplazarte.
#  *   (Ejemplo: down/up/left/right. Sólo deben proporcionarse las opciones posibles)
#  * - 🔑 Salida: Sales de la casa si encuentras la habitación con la llave.
#  * - 👻 (Bonus) Fantasmas: Existe un 33% de que en una habitación aparezca un fantasma y tengas que responder dos preguntas para salir de dicha habitacion.
#  */

#Librerias/Imports
import random


# Definición de los caracteres para los elementos de la casa
CASILLA_VACIA = '⬜️'
PUERTA = '🚪'
FANTASMA = '👻'
LLAVE = '🔑'

# Definición de la estructura de la casa 4x4. 
# Creamos una tupla llamada MANSION_1 para dentro crear 4 tuplas que seran el contenido de los elementos dentro de la mansion.

MANSION_1 = [[CASILLA_VACIA,PUERTA,CASILLA_VACIA,CASILLA_VACIA],[CASILLA_VACIA,CASILLA_VACIA,CASILLA_VACIA,FANTASMA],[FANTASMA,FANTASMA,CASILLA_VACIA,CASILLA_VACIA],[LLAVE,FANTASMA,CASILLA_VACIA,CASILLA_VACIA]]
             
# Grafico Mansion 1 :

# En este ejemplo partimos de A2 debemos llegar a D1.

# Punto de partida
punto_partida = [0,1]

# ⬜️🚪⬜️⬜️ A 0,1,2,3 y
# ⬜️⬜️⬜️👻 
# 👻👻⬜️⬜️ 
# 🔑👻⬜️⬜️ 
 #3,2,1,0 X

# Pondremos un conteo de vidas para hacerlo más divertido 🥳 : 

vidas = 3
enigmas = 14

preguntas_true = {
    'p1': True,
    'p4': True,
    'p9': True,
    'p10': True,
    'p11': True,
    'p12': True
}

# True 
# p1 = '¿La casa en la historia es un lugar de seguridad para los personajes al principio?'
# p4 = '¿La historia se desarrolla en una casa antigua?'
# p9 = '¿La historia tiene un final ambiguo?'
# p10 = '¿El cuento "La Casa Tomada" fue escrito por Julio Cortázar?'
# p11 = '¿El cuento "La Casa Tomada" de Julio Cortázar es conocido por su estilo de escritura evocador?'
# p12 = '¿La historia explora temas de aislamiento y pérdida?'


preguntas_false = {
    'p2': False,
    'p3': False,
    'p5': False,
    'p6': False,
    'p7': False,
    'p8': False,
    'p13': False,
    'p14': False
}

# False
# p2 = '¿Los personajes principales sienten que la casa está siendo invadida?'
# p3 = '¿La casa está situada en una ciudad grande?'
# p5 = '¿Los personajes intentan luchar contra la invasión de la casa?'
# p6 = '¿El cuento utiliza elementos sobrenaturales para crear su atmósfera?'
# p7 = '¿La relación entre los personajes principales está clara en la narrativa?'
# p8 = '¿El cuento se enfoca principalmente en el diálogo entre los personajes?'
# p13 = '¿Los personajes principales son hermanos en el cuento?' 
# p14 = '¿La narración se vuelve cada vez más expansiva a medida que avanza la historia?'

dicc_preguntas = {
    'p1': '¿La casa en la historia es un lugar de seguridad para los personajes al principio?',
    'p2': '¿Los personajes principales sienten que la casa está siendo invadida?',
    'p3': '¿La casa está situada en una ciudad grande?',
    'p4': '¿La historia se desarrolla en una casa antigua?',
    'p5': '¿Los personajes intentan luchar contra la invasión de la casa?',
    'p6': '¿El cuento utiliza elementos sobrenaturales para crear su atmósfera?',
    'p7': '¿La relación entre los personajes principales está clara en la narrativa?',
    'p8': '¿El cuento se enfoca principalmente en el diálogo entre los personajes?',
    'p9': '¿La historia tiene un final ambiguo?',
    'p10': '¿El cuento "La Casa Tomada" fue escrito por Julio Cortázar?',
    'p11': '¿El cuento "La Casa Tomada" de Julio Cortázar es conocido por su estilo de escritura evocador?',
    'p12': '¿La historia explora temas de aislamiento y pérdida?',
    'p13': '¿Los personajes principales son hermanos en el cuento?',
    'p14': '¿La narración se vuelve cada vez más expansiva a medida que avanza la historia?'
}


# Inicialización de preguntas contestadas
preguntas_contestadas = set() # Usamos set para añadir las preguntas y que sean registros unicos.



# Definir las direcciones disponibles
direcciones = {
'up': (-1, 0),
'down': (1, 0),
'left': (0, 1),
'right': (0, -1)
 }

# Casillas importantes
LLAVE = [0,3]
PUERTA = [1,0]
punto_partida = [1,0] #Se debe entrar por la puerta para comenzar
x, y = 1, 0
casilla_actual = MANSION_1[y][x]


x, y = PUERTA
casilla_actual = MANSION_1[y][x]
print(f'x: {x}, y: {y}')
print(f'Estás en la casilla {casilla_actual}')



# Comenzar el juego
while True:
    # Casilla Ganadora
    if nueva_posicion == LLAVE:
        print('¡Ganaste! Has encontrado la llave y puedes salir de la mansión.')
        print('Fin del juego')
        break

    direcciones_disponibles = []

    # La estructura de bucle for siguiente se utiliza para recorrer los elementos del diccionario direcciones. El bucle se ejecutará para cada elemento en direcciones.items(). Cada elemento consta de una clave (que es una dirección) y un valor (que es una tupla de desplazamiento).
    # El método items() se utiliza para obtener una lista de elementos (clave, valor) del diccionario direcciones.

    # Lógica del movimiento
    for direccion, (dx, dy) in direcciones.items():
        nuevo_x = x + dx
        nuevo_y = y + dy

        if 0 <= nuevo_x < 4 and 0 <= nuevo_y < 4:
            direcciones_disponibles.append(direccion)

    print(f'Direcciones disponibles: {", ".join(direcciones_disponibles)}')
    direccion_elegida = input('Elige una dirección: ')
    print(f'direccion_elegida: {direccion_elegida}')

    if direccion_elegida in direcciones_disponibles:
        dx, dy = direcciones[direccion_elegida]
        nueva_x = x + dx
        nueva_y = y + dy

        nueva_posicion = MANSION_1[nueva_y][nueva_x]
        print(f'nueva_x: {nueva_x}, nueva_y: {nueva_y}')
        print(f'nueva_posicion: {nueva_posicion}')

        # Luego, puedes actualizar las coordenadas
        x = nueva_x
        y = nueva_y
        casilla_actual = nueva_posicion

        if casilla_actual == CASILLA_VACIA and enigmas > 0:
            pregunta = random.choice(list(dicc_preguntas.keys()))
            if pregunta not in preguntas_contestadas:
                print(f'Contesta la siguiente pregunta: {dicc_preguntas[pregunta]}')
                respuesta = input('Responde con "T" o "F": ')

                if respuesta.lower() == 't' and pregunta in preguntas_true:
                    print('Respuesta correcta. Elige a dónde avanzar.')
                elif respuesta.lower() == 'f' and pregunta in preguntas_false:
                    print('Respuesta correcta. Elige a dónde avanzar.')
                else:
                    print('Respuesta incorrecta. Pierdes una vida.')
                    vidas -= 1
                    print(f'Te quedan {vidas} vidas.')
                preguntas_contestadas.add(pregunta)

        elif casilla_actual == FANTASMA and enigmas > 0:
            print('¡Soy un fantasma! Debes responder dos preguntas.')
            for _ in range(2):
                pregunta = random.choice(list(dicc_preguntas.keys()))
                if pregunta not in preguntas_contestadas:
                    print(f'Contesta la siguiente pregunta: {dicc_preguntas[pregunta]}')
                    respuesta = input('Responde con "T" o "F": ')

                    if respuesta.lower() == 't' and pregunta in preguntas_true:
                        print('Respuesta correcta. Sigue con la siguiente pregunta.')
                    elif respuesta.lower() == 'f' and pregunta in preguntas_false:
                        print('Respuesta correcta. Ahora debes contestar la segunda pregunta.')
                    else:
                        print('Respuesta incorrecta. Pierdes una vida.')
                        vidas -= 1
                        print(f'Te quedan {vidas} vidas.')
                    preguntas_contestadas.add(pregunta)

    else:
        print('Dirección no válida. Inténtalo de nuevo.')
        if vidas <= 0:
            print('Todas tus vidas se han agotado. Has perdido el juego.')
            break
if vidas == 0:
    print('Has perdido todas tus vidas. Juego terminado.')
