Cifrado Vernam (One-Time Pad) en Python

También conocido como One-Time Pad (OTP). Se considera el único método de cifrado teóricamente inquebrantable, siempre y cuando la clave sea verdaderamente aleatoria, tan larga como el mensaje y se utilice una sola vez.

---


El programa se basa en una operación matemática:

1.  Operación XOR: El núcleo del cifrado es la operación XOR (o-exclusivo) a nivel de bits. Para cifrar, se aplica esta operación entre el valor numérico (ASCII) de cada caracter del mensaje y su caracter correspondiente en la clave.
2.  Simetría Perfecta: Una propiedad fundamental del XOR es que es reversible. Si aplicas la misma operación XOR con la misma clave al texto cifrado, obtienes el mensaje original. Por esta razón, las funciones para cifrar y descifrar en el código son idénticas.
3.  Requisito Clave: El programa refuerza la regla más importante del Cifrado Vernam: la clave debe tener exactamente la misma longitud que el mensaje.

---

Uso del Programa

* Interactivo: El script solicita al usuario que ingrese un mensaje y una clave.
* Salida: Muestra el mensaje cifrado, que a menudo resulta en una cadena de caracteres extraños o no imprimibles (debido a la naturaleza del XOR). Inmediatamente después, lo descifra para demostrar que el proceso es correcto.
* Requerimiento*: No necesita ninguna biblioteca externa, funciona con una instalación estándar de Python.