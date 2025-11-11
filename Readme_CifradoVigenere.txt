Cifrado Vigenère en C

Es considerado una versión mejorada y mucho más segura que el cifrado César, ya que utiliza una palabra clave en lugar de un único número para realizar los desplazamientos de las letras.

---

El programa opera a través de un menú interactivo que permite al usuario cifrar, descifrar o salir.

1.  Uso de la Palabra Clave: A diferencia de un desplazamiento fijo, el Vigenère utiliza una palabra clave que se repite cíclicamente hasta alcanzar la misma longitud que el mensaje.
2.  Cifrado: Cada letra del mensaje se desplaza un número de posiciones determinado por la letra correspondiente en la clave repetida. Por ejemplo, si la clave es "KEY" y el mensaje "HELLO", la 'H' se desplaza según la 'K', la 'E' según la 'E', la 'L' según la 'Y', la siguiente 'L' de nuevo según la 'K', y así sucesivamente.
3.  Descifrado: El proceso es el inverso: a cada letra del mensaje cifrado se le resta el valor de la letra correspondiente de la clave para obtener el texto original.

---

Uso y Requerimientos

* Compilación: Necesita un compilador de C (como GCC) para ser compilado y ejecutado en una terminal.
* Entrada de Datos: El programa está diseñado para procesar únicamente letras minúsculas y sin espacios (solo procesa la primera palabra de la entrada).
* Multiplataforma: Utiliza `system("cls")` que es para Windows, pero el código incluye un comentario indicando que se debe usar `system("clear")` en Linux/Unix.