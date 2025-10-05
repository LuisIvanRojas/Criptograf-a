Cifrado Playfair en Python

Método de cifrado por sustitución que encripta pares de letras (digramas) en lugar de letras individuales. Esto lo hace más seguro que los cifrados de sustitución simple como el César. Su funcionamiento se basa en una matriz de 5x5 generada a partir de una palabra clave.

---

Funcionamiento Principal

1.  Generar la Matriz: A partir de una clave proporcionada por el usuario, se crea una matriz de 5x5. La matriz se llena primero con las letras únicas de la clave (tratando la 'j' como 'i') y luego con el resto de las letras del alfabeto.
2.  Preparar el Texto: El mensaje a cifrar se procesa para:
    * Dividirlo en pares de letras.
    * Separar letras repetidas en un par (ej. "ll" se convierte en "lx l").
    * Añadir una 'x' al final si el mensaje tiene un número impar de letras.
3.  Cifrar y Descifrar: Para cada par de letras, se aplican tres reglas según su posición en la matriz:
    * Misma Fila: Se reemplazan por las letras a su derecha.
    * Misma Columna: Se reemplazan por las letras de abajo.
    * Rectángulo: Se reemplazan por las letras en las esquinas opuestas de su rectángulo.
    
    El proceso de descifrado simplemente invierte estas reglas (moviéndose a la izquierda o hacia arriba).

---

Uso del Programa

* Interactivo: Al ejecutarlo, el programa pide una clave para generar la matriz.
* Menú de Opciones: Luego, presenta un menú para elegir entre cifrar un mensaje, descifrar uno o salir.
* Requerimientos: No necesita ninguna biblioteca externa, solo una instalación estándar de Python.