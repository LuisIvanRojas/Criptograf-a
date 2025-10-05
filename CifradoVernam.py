def vernam_cifrar(mensaje, clave):
    if len(mensaje) != len(clave):
        raise ValueError("La clave debe tener la misma longitud que el mensaje")
    
    cifrado = []
    for m, k in zip(mensaje, clave):
        cifrado.append(chr(ord(m) ^ ord(k)))  # XOR
    return "".join(cifrado)


def vernam_descifrar(cifrado, clave):
    if len(cifrado) != len(clave):
        raise ValueError("La clave debe tener la misma longitud que el mensaje")
    
    original = []
    for c, k in zip(cifrado, clave):
        original.append(chr(ord(c) ^ ord(k)))  # XOR
    return "".join(original)


# --------------------------
# Programa principal
# --------------------------
if __name__ == "__main__":
    print("Cifrado Vernam (One-Time Pad)")
    mensaje = input("Ingrese el mensaje: ")
    clave = input("Ingrese la clave (misma longitud que el mensaje): ")

    cifrado = vernam_cifrar(mensaje, clave)
    print("Mensaje cifrado (texto raro):", cifrado)

    descifrado = vernam_descifrar(cifrado, clave)
    print("Mensaje descifrado:", descifrado)
