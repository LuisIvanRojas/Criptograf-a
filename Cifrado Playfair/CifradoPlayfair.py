def generar_matriz(clave):
    clave = clave.lower().replace("j", "i")
    alfabeto = "abcdefghiklmnopqrstuvwxyz"  # j se une con i

    # eliminar duplicados
    nueva_clave = ""
    for c in clave:
        if c not in nueva_clave and c in alfabeto:
            nueva_clave += c
    for c in alfabeto:
        if c not in nueva_clave:
            nueva_clave += c

    # matriz 5x5
    matriz = [list(nueva_clave[i:i+5]) for i in range(0, 25, 5)]
    return matriz


def buscar(matriz, letra):
    if letra == "j":
        letra = "i"
    for i in range(5):
        for j in range(5):
            if matriz[i][j] == letra:
                return i, j
    return None


def preparar_texto(texto):
    texto = texto.lower().replace(" ", "").replace("j", "i")
    pares = []
    i = 0
    while i < len(texto):
        a = texto[i]
        b = ""
        if i+1 < len(texto):
            b = texto[i+1]
        else:
            b = "x"

        if a == b:  # no se permiten pares iguales
            pares.append(a + "x")
            i += 1
        else:
            pares.append(a + b)
            i += 2
    return pares


def cifrar(texto, matriz):
    pares = preparar_texto(texto)
    resultado = ""
    for par in pares:
        a, b = par[0], par[1]
        fila1, col1 = buscar(matriz, a)
        fila2, col2 = buscar(matriz, b)

        if fila1 == fila2:  # misma fila
            resultado += matriz[fila1][(col1+1)%5]
            resultado += matriz[fila2][(col2+1)%5]
        elif col1 == col2:  # misma columna
            resultado += matriz[(fila1+1)%5][col1]
            resultado += matriz[(fila2+1)%5][col2]
        else:  # rectángulo
            resultado += matriz[fila1][col2]
            resultado += matriz[fila2][col1]
    return resultado


def descifrar(texto, matriz):
    pares = preparar_texto(texto)
    resultado = ""
    for par in pares:
        a, b = par[0], par[1]
        fila1, col1 = buscar(matriz, a)
        fila2, col2 = buscar(matriz, b)

        if fila1 == fila2:  # misma fila
            resultado += matriz[fila1][(col1-1)%5]
            resultado += matriz[fila2][(col2-1)%5]
        elif col1 == col2:  # misma columna
            resultado += matriz[(fila1-1)%5][col1]
            resultado += matriz[(fila2-1)%5][col2]
        else:  # rectángulo
            resultado += matriz[fila1][col2]
            resultado += matriz[fila2][col1]
    return resultado


# --------------------------
# Programa principal
# --------------------------
if __name__ == "__main__":
    print("Cifrado Playfair")
    clave = input("Ingrese la clave: ")
    matriz = generar_matriz(clave)

    print("\nMatriz generada:")
    for fila in matriz:
        print(fila)

    opcion = 0
    while opcion != 3:
        print("\nQue desea hacer?")
        print("1. Cifrar")
        print("2. Descifrar")
        print("3. Salir")
        opcion = int(input("Opcion: "))

        if opcion == 1:
            mensaje = input("Ingrese el mensaje: ")
            cif = cifrar(mensaje, matriz)
            print("Mensaje cifrado:", cif)
        elif opcion == 2:
            mensaje = input("Ingrese el mensaje cifrado: ")
            desc = descifrar(mensaje, matriz)
            print("Mensaje descifrado:", desc)
