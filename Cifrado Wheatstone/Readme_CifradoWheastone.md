
### Descripción del programa – Cifrado de Wheatstone (Playfair) en Python


El **Cifrado Wheatstone**, también conocido como **Cifrado Playfair**, es un método de cifrado clásico de sustitución por dígrafos (pares de letras).  
Fue inventado en 1854 por **Charles Wheatstone**, aunque se le atribuye popularmente a **Lord Playfair** por haber promovido su uso.

Este cifrado utiliza una **matriz de 5x5** construida a partir de una palabra clave.  
El texto a cifrar se divide en pares de letras, y cada par se sustituye según reglas basadas en las posiciones dentro de la matriz.

---

## Funcionamiento del algoritmo

1. **Generación de la matriz**  
   - Se toma una palabra clave.  
   - Se eliminan letras repetidas.  
   - Se completa con el resto del alfabeto (fusionando I/J en una sola celda).  

2. **Preparación del texto**  
   - Se eliminan espacios.  
   - Se reemplaza la letra **J** por **I**.  
   - Si hay dos letras iguales seguidas, se inserta una **X** entre ellas.  
   - Si el texto tiene un número impar de letras, se añade una **X** al final.  

3. **Reglas de cifrado**  
   Para cada par de letras:
   - Si están **en la misma fila**, se sustituye cada una por la que está **a su derecha**.  
   - Si están **en la misma columna**, se sustituye cada una por la que está **debajo**.  
   - Si forman un **rectángulo**, se sustituyen cruzando sus columnas.

4. **Reglas de descifrado**  
   Se aplican las mismas reglas pero en sentido inverso (izquierda o arriba en lugar de derecha o abajo).

---

## Ejemplo de uso

**Clave:** `criptografia`  
**Mensaje original:** `defensa nacional`

**Matriz generada:**

```

c r i p t
o g a f b
d e n s l
m q u v w
x y z h k

```

**Resultado cifrado:**  
```

eeufpqbsciucpb

````

---

## Ejecución del programa

### Requisitos previos
- Python 3.8 o superior

## Detalles técnicos

* El algoritmo trabaja con letras minúsculas.
* Las letras **I/J** se consideran equivalentes.
* Las letras repetidas en pares se dividen con una **X** para mantener la estructura del cifrado.
* Los resultados son deterministas: mismo texto + misma clave → mismo cifrado.

