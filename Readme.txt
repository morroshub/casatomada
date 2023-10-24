
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