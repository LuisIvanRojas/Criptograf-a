### Descripción del programa – Cifrado César

Este programa implementa el Algoritmo de Cifrado César, uno de los métodos de criptografía por sustitución más antiguos y sencillos.
El principio de funcionamiento consiste en reemplazar cada letra del mensaje original por otra letra que se encuentra un número fijo de posiciones más adelante en el alfabeto, determinado por una **llave numérica**.

Al ejecutar el programa, se presenta un "menú interactivo" que permite al usuario seleccionar una de las siguientes opciones:

1. Cifrar:

El programa solicita al usuario ingresar un mensaje (en letras minúsculas) y una clave numérica.
   A continuación, cada letra del mensaje se desplaza hacia adelante en el alfabeto tantas posiciones como indique la clave, generando y mostrando el texto cifrado.

2. Descifrar
   El usuario introduce un mensaje previamente cifrado y la misma clave numérica utilizada para cifrarlo.
   El programa aplica el desplazamiento inverso, restituyendo el texto original.

3. Salir
   Finaliza la ejecución del programa.


### Consideraciones importantes

* El programa está diseñado para **procesar únicamente letras minúsculas del alfabeto inglés** (`a`–`z`).
  No admite mayúsculas, números ni caracteres especiales.

* Debido al uso de la función `scanf("%s", ...)`, solo se procesa una palabra a la vez.
  En caso de ingresar una frase con espacios, únicamente se tomará en cuenta la primera palabra.

* El comando `system("cls")` se utiliza para limpiar la consola en sistemas **Windows**.
  En entornos **Linux** o **macOS**, este comando puede sustituirse por `system("clear")`.


