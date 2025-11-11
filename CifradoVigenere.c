#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// funciones
void cifrado();
void descifrado();

// función auxiliar para obtener el valor numérico de una letra
int valorLetra(char c) {
    return c - 'a';  // convierte 'a'=0, 'b'=1 ... 'z'=25
}

int main() {
    int opcion = 0;
    printf("Cifrado Vigenere \n");

    while (opcion != 3) {
        printf("\nQue desea hacer?\n");
        printf("1.) Cifrar\n");
        printf("2.) Descifrar\n");
        printf("3.) Salir\n");
        printf("Seleccione una opcion: \n");
        scanf("%d", &opcion);
        system("cls"); // en Linux/Unix usar system("clear");

        switch (opcion) {
            case 1:
                cifrado();
                break;
            case 2:
                descifrado();
                break;
            case 3:
                return 0;
            default:
                printf("Opcion invalida\n");
        }
    }
    return 0;
}

// ------------------------------------------
// función de cifrado Vigenere
void cifrado() {
    char mensaje[200], clave[200], cipher[200];
    printf("\nIngrese el mensaje en minusculas que desea cifrar (sin espacios): ");
    scanf("%s", mensaje);
    printf("\nIngrese la clave en minusculas: ");
    scanf("%s", clave);

    int lenMensaje = strlen(mensaje);
    int lenClave = strlen(clave);

    for (int i = 0; i < lenMensaje; i++) {
        char letra = mensaje[i];
        int valorClave = valorLetra(clave[i % lenClave]);
        letra = (letra - 'a' + valorClave + 26) % 26 + 'a';
        cipher[i] = letra;
    }
    cipher[lenMensaje] = '\0'; // final de cadena
    printf("\nMensaje cifrado: %s\n", cipher);
}

// -----------------------------------------
// funcion de descifrado Vigenere
void descifrado() {
    char mensaje[200], clave[200], original[200];
    printf("\nIngrese el mensaje en minusculas que desea descifrar (sin espacios): ");
    scanf("%s", mensaje);
    printf("\nIngrese la clave en minusculas: ");
    scanf("%s", clave);

    int lenMensaje = strlen(mensaje);
    int lenClave = strlen(clave);

    for (int i = 0; i < lenMensaje; i++) {
        char letra = mensaje[i];
        int valorClave = valorLetra(clave[i % lenClave]);
        letra = (letra - 'a' - valorClave + 26) % 26 + 'a';
        original[i] = letra;
    }
    original[lenMensaje] = '\0'; // final de cadena
    printf("\nMensaje original: %s\n", original);
}
