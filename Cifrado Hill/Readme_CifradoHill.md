### Descripción del programa – Cifrado Hill en Python

Este programa implementa el **Cifrado Hill**, un método de encriptación poligráfica basado en **álgebra lineal**.
A diferencia de los cifrados de sustitución simple, el Cifrado Hill opera sobre bloques de letras, lo que incrementa significativamente la complejidad del análisis criptográfico y la seguridad del mensaje.

### Funcionamiento general

El programa permite **cifrar y descifrar** mensajes mediante el uso de matrices clave y operaciones modulares.
Su lógica principal se desarrolla en las siguientes etapas:

1. **Preparación del mensaje**:

   El texto ingresado se convierte a **mayúsculas** y se eliminan los caracteres no alfabéticos.
   Si la longitud del mensaje no es múltiplo del tamaño de la matriz clave, se añaden caracteres de **relleno ('X')** para completar el bloque.

2. **Conversión a vectores numéricos**:

   El texto se agrupa en bloques del tamaño de la matriz clave, convirtiendo cada letra en un número según su posición en el alfabeto (A=0, B=1, ..., Z=25).

3. **Proceso de cifrado y descifrado**:

   * **Cifrado:** cada bloque del mensaje se multiplica por la **matriz clave** y se aplica la operación módulo 26 al resultado.
   * **Descifrado:** se calcula la **matriz inversa modular** de la clave y se multiplica por los bloques del texto cifrado para recuperar el mensaje original.

4. **Conversión final**:

   Los resultados numéricos obtenidos se transforman nuevamente en letras, generando el texto cifrado o descifrado según el proceso aplicado.

### Requisitos y ejecución

* **Dependencia:** el programa requiere la biblioteca `numpy`, utilizada para realizar las operaciones matriciales de manera eficiente.
  Se puede instalar mediante el comando:

  ```bash
  pip install numpy
  ```

* **Ejecución:** el script incluye ejemplos que muestran cómo definir matrices clave de tamaño **2×2** y **3×3**, así como el uso de las funciones principales para **cifrar y descifrar** mensajes.

---

### Observaciones

* La **matriz clave** debe ser **invertible módulo 26**, condición necesaria para que el descifrado sea posible.
* El cifrado Hill ilustra la aplicación directa de los **conceptos matemáticos del álgebra lineal** en la criptografía, sirviendo como base para comprender técnicas más avanzadas de cifrado simétrico.

