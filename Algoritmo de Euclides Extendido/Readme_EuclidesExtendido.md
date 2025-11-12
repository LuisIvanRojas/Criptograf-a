### Descripción del programa – Algoritmo de Euclides Extendido en Python

Este programa implementa el **Algoritmo de Euclides Extendido**, una mejora del algoritmo clásico de Euclides utilizado para calcular el **máximo común divisor (MCD)** de dos números enteros.
Además, permite encontrar los **coeficientes de Bézout** `x` e `y` que cumplen la relación:

[
a \cdot x + b \cdot y = MCD(a, b)
]

---

## Funcionamiento del Programa

1. **Entrada de Datos**

   El usuario ingresa dos números enteros `a` y `b`.
   El programa valida que sean números positivos.

2. **Cálculo Recursivo**

   Se aplica el **Algoritmo de Euclides Extendido**:

   * Si `a = 0`, entonces el MCD es `b`, y los coeficientes son `(x=0, y=1)`.
   * En caso contrario, el algoritmo se llama recursivamente con los valores `(b % a, a)` y ajusta los coeficientes obtenidos.

3. **Resultados Mostrados**

   El programa imprime:

   * El **MCD** de los dos números.
   * Los **coeficientes de Bézout** `x` e `y`.
   * Una verificación de la igualdad ( a·x + b·y = MCD(a, b) ).

4. **Interactividad**

   Al finalizar, el usuario puede optar por realizar otro cálculo o salir del programa.

---

## Uso del Programa

* **Ejecución:**
  Abre una terminal y ejecuta el script con Python:

  ```bash
  python euclides_extendido.py
  ```

* **Ejemplo de uso:**

  ```
  --- Cálculo del MCD y coeficientes de Bézout ---
  Ingrese el primer número (a): 56
  Ingrese el segundo número (b): 98

  El máximo común divisor de 56 y 98 es: 14
  Los coeficientes x e y son: x = -1, y = 1
  Verificación de la identidad de Bézout: 56*(-1) + 98*(1) = 42
  ```

---

## Conceptos Clave

* **Máximo Común Divisor (MCD):**
  Es el número más grande que divide exactamente a `a` y `b`.

* **Identidad de Bézout:**
  Expresión que muestra cómo el MCD puede escribirse como una combinación lineal de `a` y `b`.

* **Usos en Criptografía:**
  El algoritmo es esencial en métodos como **RSA**, ya que se utiliza para calcular **inversos modulares**, paso clave en el proceso de generación de claves.

---

## 💡 Requisitos

* Python 3.7 o superior
* No necesita bibliotecas externas

