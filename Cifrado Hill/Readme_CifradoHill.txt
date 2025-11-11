Cifrado Hill en Python

Este script de Python implementa el Cifrado Hill, un método de cifrado que utiliza álgebra lineal (matrices) para codificar bloques de letras simultáneamente, lo que lo hace más robusto que los cifrados de sustitución simple.

---

El programa puede tanto cifrar como descifrar un mensaje. Su lógica principal es:

1.  Preparación del Mensaje: Convierte el texto a mayúsculas, elimina cualquier carácter que no sea una letra y añade un relleno (con la letra 'X') si es necesario para que la longitud del mensaje sea un múltiplo del tamaño de la matriz clave.
2.  Conversión a Vectores: Agrupa las letras en bloques (vectores) y las convierte a números (A=0, B=1, ..., Z=25).
3.  Proceso de Cifrado/Descifrado:
    *Para cifrar, multiplica cada vector del mensaje por la matriz clave.
    *Para descifrar, primero calcula la matriz inversa modular de la clave y luego la multiplica por los vectores del mensaje cifrado.
4.  Resultado: El resultado numérico de la multiplicación se convierte de nuevo a letras, revelando el texto cifrado o el original.

---

Requerimientos y Uso

*Dependencia: El programa depende de la biblioteca `numpy` para realizar todas las operaciones matriciales de forma eficiente.
*Ejecución: El propio script incluye ejemplos claros que muestran cómo definir una matriz clave y utilizar las funciones para cifrar y descifrar mensajes con claves de 2x2 y 3x3.