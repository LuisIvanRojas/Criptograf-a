### Descripción del programa – Cifrado Playfair en Python

Este programa implementa el **Cifrado Playfair**, un método de sustitución que cifra **pares de letras (digramas)** en lugar de caracteres individuales.
Gracias a este enfoque, el cifrado resulta más resistente al análisis de frecuencia que los cifrados monoalfabéticos simples, como el Cifrado César.
El sistema se basa en una **matriz de 5×5** generada a partir de una **palabra clave** proporcionada por el usuario.

---

### Funcionamiento general

1. **Generación de la matriz clave**

   A partir de la palabra clave ingresada por el usuario, se construye una **matriz de 5×5** que contiene las letras del alfabeto en orden.

   * Las letras repetidas dentro de la clave se eliminan.
   * Las letras **‘I’** y **‘J’** se tratan como equivalentes para ajustar el alfabeto a 25 caracteres.
   * Después de colocar las letras únicas de la clave, se completan las celdas restantes con las letras faltantes del alfabeto.

2. **Preparación del texto**

   Antes del cifrado, el mensaje se procesa de la siguiente manera:

   * Se convierte a **minúsculas o mayúsculas uniformemente**.
   * Se eliminan caracteres no alfabéticos.
   * Se divide el texto en **pares de letras**.
   * Si un par contiene letras repetidas (por ejemplo, “LL”), se inserta una **‘X’** entre ellas.
   * Si el mensaje tiene un número impar de letras, se añade una **‘X’** al final como relleno.

3. **Proceso de cifrado y descifrado**

   El algoritmo aplica tres reglas fundamentales según la posición de cada par de letras dentro de la matriz:

   * **Misma fila:** cada letra se sustituye por la que está inmediatamente a su derecha (volviendo al inicio si es necesario).
   * **Misma columna:** cada letra se sustituye por la que está inmediatamente debajo.
   * **Rectángulo:** si las letras forman las esquinas de un rectángulo, cada una se reemplaza por la letra ubicada en la misma fila pero en la columna de la otra letra.

   El **descifrado** aplica las mismas reglas de forma inversa (movimientos hacia la izquierda o hacia arriba).

---

### Uso del programa

* **Modo interactivo:**
  Al iniciar la ejecución, el programa solicita al usuario una **clave** para generar la matriz de cifrado.
  Luego presenta un **menú de opciones** que permite elegir entre:

  1. Cifrar un mensaje.
  2. Descifrar un mensaje.
  3. Salir del programa.

* **Requerimientos:**
  El programa no requiere librerías externas.
  Puede ejecutarse con una instalación estándar de **Python 3.x**.

---

### Observaciones

* El cifrado Playfair es un claro ejemplo del avance de la criptografía clásica hacia técnicas **poligráficas**, al operar con pares de caracteres en lugar de sustituciones individuales.
* Aunque históricamente fue considerado seguro, actualmente su uso es principalmente **educativo**, pues los métodos modernos han superado ampliamente sus capacidades de protección.

---



