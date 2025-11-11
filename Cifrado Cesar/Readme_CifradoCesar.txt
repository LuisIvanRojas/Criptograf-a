Este programa es una implementación del Cifrado César, un método de criptografía simple basado en la sustitución. En este cifrado, cada letra del texto original es reemplazada por otra letra que se encuentra un número fijo de posiciones más adelante en el alfabeto.


Al ejecutar el programa, se despliega un menú interactivo que permite al usuario elegir entre tres opciones:

1.  Cifrar: El programa solicita al usuario que ingrese un mensaje (solo en minúsculas) y una "llave" numérica. Luego, cada letra del mensaje se desplaza hacia adelante en el alfabeto tantas posiciones como indique la llave, mostrando el mensaje cifrado.
2.  Descifrar: El usuario introduce un mensaje cifrado y la misma llave numérica que usó para cifrar. El programa revierte el proceso, desplazando las letras hacia atrás para revelar el mensaje original.
3.  Salir: Termina la ejecución del programa.


Importante

  * El programa solo está diseñado para aceptar letras minúsculas del alfabeto inglés. No procesará mayúsculas, números ni símbolos.
  * Debido al uso de `scanf("%s", ...)`, el programa solo leerá una sola palabra (hasta el primer espacio). Si introduces una frase, solo se procesará la primera palabra.
  * El comando `system("cls")` es específico para limpiar la consola en Windows. En sistemas como Linux o macOS, el comando equivalente sería `system("clear")`.