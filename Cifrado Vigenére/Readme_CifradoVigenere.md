
### Descripción del programa – Cifrado Vigenère en C

El **Cifrado Vigenère** es un método clásico de cifrado polialfabético, considerado una versión mejorada y más robusta que el **Cifrado César**.
Su principal característica radica en el uso de una **palabra clave** que introduce múltiples desplazamientos, lo cual dificulta los ataques de frecuencia típicos de los cifrados monoalfabéticos.

---

### Funcionamiento general

1. **Uso de la palabra clave**

   A diferencia del Cifrado César, que utiliza un desplazamiento fijo, el algoritmo de Vigenère emplea una **palabra clave** cuyos caracteres determinan los desplazamientos individuales de las letras del mensaje.
   Dicha clave se **repite cíclicamente** hasta igualar la longitud del texto a cifrar.

2. **Cifrado**

   Cada letra del mensaje se desplaza en el alfabeto un número de posiciones correspondiente al valor de la letra asociada en la clave repetida.
   Por ejemplo, si la clave es **"KEY"** y el mensaje es **"HELLO"**, la letra **‘H’** se cifra con el desplazamiento definido por **‘K’**, **‘E’** con **‘E’**, **‘L’** con **‘Y’**, y así sucesivamente de manera cíclica.

3. **Descifrado**

   El proceso de descifrado invierte la operación anterior:
   a cada carácter del texto cifrado se le **resta** el desplazamiento determinado por la letra correspondiente de la clave, recuperando así el mensaje original.

---

### Uso del programa

El programa presenta un **menú interactivo** que permite al usuario elegir entre las siguientes opciones:

* **Cifrar un mensaje**
* **Descifrar un mensaje**
* **Salir del programa**

Durante la ejecución, el usuario ingresa tanto el texto como la palabra clave, que deben cumplir las condiciones indicadas en las instrucciones del programa.

---

### Requerimientos y ejecución

* **Compilación:**
  El código está escrito en lenguaje **C** y requiere un compilador estándar como **GCC** para su compilación y ejecución en una terminal.
  Ejemplo de compilación y ejecución:

  ```bash
  gcc vigenere.c -o vigenere
  ./vigenere
  ```

* **Entrada de datos:**

  El programa está diseñado para procesar únicamente **letras minúsculas sin espacios**, es decir, analiza solo la primera palabra ingresada.

* **Compatibilidad multiplataforma:**

  Incluye la instrucción `system("cls")` para limpiar la pantalla en sistemas **Windows**.
  No obstante, se añade un comentario indicando que debe sustituirse por `system("clear")` en entornos **Linux/Unix**.

---

### Observaciones

* El Cifrado Vigenère fue considerado durante siglos como uno de los métodos más seguros de cifrado clásico.
* Su fortaleza radica en la variabilidad introducida por la palabra clave, aunque puede ser vulnerado mediante análisis estadístico si la clave es corta o reutilizada.
* Este programa constituye una implementación práctica que ilustra los principios fundamentales del cifrado polialfabético.

