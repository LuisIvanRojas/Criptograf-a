### Descripción del programa – Cifrado Vernam (One-Time Pad) en Python

El **Cifrado Vernam**, también conocido como **One-Time Pad (OTP)**, es un método de cifrado simétrico considerado **teóricamente inquebrantable**, siempre que se cumplan ciertas condiciones:
la **clave** debe ser **totalmente aleatoria**, **tan larga como el mensaje** y **utilizada una sola vez**.

Este algoritmo se basa en una operación lógica simple pero poderosa, que garantiza una simetría perfecta entre el proceso de cifrado y descifrado.

---

### Funcionamiento general

1. **Operación XOR (O-exclusivo)**
   
   El núcleo del algoritmo es la operación **XOR** (o-exclusivo) aplicada a nivel de bits.
   Durante el cifrado, se toma el valor numérico (ASCII) de cada carácter del mensaje y se combina con el valor correspondiente de la clave mediante esta operación lógica.

2. **Simetría perfecta**
   
   Una propiedad esencial del operador XOR es su reversibilidad:
   aplicar nuevamente la misma operación con la **misma clave** sobre el texto cifrado produce el **mensaje original**.
   Por ello, las funciones de **cifrado y descifrado** en el programa son idénticas.

3. **Requisitos de la clave**
   
   El programa enfatiza la regla fundamental del Cifrado Vernam:
   la clave debe tener **exactamente la misma longitud** que el mensaje.
   Si esta condición no se cumple, el cifrado deja de ser seguro.

---

### Uso del programa

* **Modo interactivo:**

  El script solicita al usuario que introduzca un **mensaje** y una **clave** del mismo tamaño.
  Posteriormente, muestra el resultado cifrado, que usualmente se presenta como una secuencia de **caracteres no legibles o no imprimibles**, debido a la naturaleza binaria de la operación XOR.
  Luego, realiza automáticamente el proceso de **descifrado** para demostrar la recuperación exacta del texto original.

* **Requerimientos:**

  El programa no depende de librerías externas y puede ejecutarse en cualquier instalación estándar de **Python 3.x**.

---

### Observaciones

* El Cifrado Vernam representa uno de los fundamentos teóricos más importantes de la criptografía moderna.
* Su invulnerabilidad depende estrictamente del cumplimiento de las condiciones de uso único y aleatoriedad total de la clave.
* En la práctica, la dificultad de generar y distribuir claves verdaderamente aleatorias limita su aplicación a contextos muy específicos, como comunicaciones de alta seguridad.

---

