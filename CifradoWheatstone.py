

def generar_matriz(clave):
    """Crea una matriz 5x5 a partir de una clave, omitiendo letras repetidas y la 'j'."""
    clave = clave.lower().replace("j", "i")
    alfabeto = "abcdefghiklmnopqrstuvwxyz"
    letras_usadas = []
    matriz = []

    # Incorporar las letras de la clave
    for letra in clave:
        if letra not in letras_usadas and letra in alfabeto:
            letras_usadas.append(letra)

    # Completar con las letras restantes del alfabeto
    for letra in alfabeto:
        if letra not in letras_usadas:
            letras_usadas.append(letra)

    # Construir la matriz 5x5
    for i in range(0, 25, 5):
        matriz.append(letras_usadas[i:i + 5])
    return matriz


def mostrar_matriz(matriz):
    """Muestra la matriz generada de forma organizada."""
    print("\n🔷 MATRIZ DE CIFRADO 🔷")
    for fila in matriz:
        print("  ".join(fila))
    print()


def buscar_posicion(letra, matriz):
    """Localiza la posición (fila, columna) de una letra en la matriz."""
    letra = 'i' if letra == 'j' else letra
    for f, fila in enumerate(matriz):
        if letra in fila:
            return f, fila.index(letra)
    return None, None


def preparar_mensaje(texto):
    """Transforma el mensaje en pares de letras (dígrafos)."""
    texto = texto.lower().replace(" ", "").replace("j", "i")
    pares = []
    i = 0

    while i < len(texto):
        a = texto[i]
        b = texto[i + 1] if i + 1 < len(texto) else 'x'
        if a == b:
            pares.append((a, 'x'))
            i += 1
        else:
            pares.append((a, b))
            i += 2

    if len(pares[-1]) == 1:
        pares[-1] = (pares[-1][0], 'x')

    return pares


def cifrar(pares, matriz):
    """Realiza el proceso de encriptado según las reglas del cifrado Wheatstone."""
    resultado = ""

    for a, b in pares:
        f1, c1 = buscar_posicion(a, matriz)
        f2, c2 = buscar_posicion(b, matriz)

        # Regla 1: misma fila → mover a la derecha
        if f1 == f2:
            resultado += matriz[f1][(c1 + 1) % 5] + matriz[f2][(c2 + 1) % 5]

        # Regla 2: misma columna → mover hacia abajo
        elif c1 == c2:
            resultado += matriz[(f1 + 1) % 5][c1] + matriz[(f2 + 1) % 5][c2]

        # Regla 3: letras en distinto renglón y columna → formar rectángulo
        else:
            resultado += matriz[f1][c2] + matriz[f2][c1]

    return resultado


def descifrar(pares, matriz):
    """Invierte las reglas para obtener el texto original."""
    resultado = ""

    for a, b in pares:
        f1, c1 = buscar_posicion(a, matriz)
        f2, c2 = buscar_posicion(b, matriz)

        # Regla 1: misma fila → mover a la izquierda
        if f1 == f2:
            resultado += matriz[f1][(c1 - 1) % 5] + matriz[f2][(c2 - 1) % 5]

        # Regla 2: misma columna → mover hacia arriba
        elif c1 == c2:
            resultado += matriz[(f1 - 1) % 5][c1] + matriz[(f2 - 1) % 5][c2]

        # Regla 3: letras en distinto renglón y columna → formar rectángulo
        else:
            resultado += matriz[f1][c2] + matriz[f2][c1]

    return resultado


# ==========================================
# BLOQUE PRINCIPAL DEL PROGRAMA
# ==========================================
if __name__ == "__main__":
    print("SISTEMA DE CIFRADO WHEATSTONE")

    while True:
        clave = input("\nIntroduce la palabra clave para generar la matriz: ").strip()
        matriz = generar_matriz(clave)
        mostrar_matriz(matriz)

        texto = input("Escribe el mensaje que deseas procesar: ").strip().lower()
        pares = preparar_mensaje(texto)

        print("\nElige una acción a realizar:")
        print("1. Encriptar texto")
        print("2. Desencriptar texto")
        opcion = input("→ ")

        if opcion == "1":
            resultado = cifrar(pares, matriz)
            print(f"\n Texto encriptado:\n{resultado}")
        elif opcion == "2":
            resultado = descifrar(pares, matriz)
            print(f"\n Texto desencriptado:\n{resultado}")
        else:
            print("\n Opción no reconocida. Intenta nuevamente.")

        continuar = input("\n¿Deseas ejecutar otra operación? (s/n): ").lower()
        if continuar == "n":
            print("\nPrograma finalizado. ¡Hasta pronto!")
            break
