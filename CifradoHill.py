import numpy as np
import math

# Función para encontrar el inverso modular de un número 'a' modulo 'm'
def modular_inverse(a, m):
    """
    Encuentra el inverso multiplicativo modular de 'a' bajo el módulo 'm'.
    El inverso 'x' es el número tal que (a * x) % m = 1.
    """
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None # El inverso no existe si gcd(a, m) != 1

def hill_cipher(message, key_matrix, mode='encrypt'):
    """
    Cifra o descifra un mensaje usando el cifrado de Hill.
    
    :param message: El mensaje de texto a procesar.
    :param key_matrix: La matriz clave (como un objeto numpy).
    :param mode: 'encrypt' para cifrar, 'decrypt' para descifrar.
    :return: El texto cifrado o descifrado.
    """
    # --- 1. Preparación del mensaje y la clave ---
    n = key_matrix.shape[0]
    
    # Limpiar el mensaje: convertir a mayúsculas y quitar caracteres no alfabéticos
    message = ''.join(filter(str.isalpha, message)).upper()
    
    # Si el modo es 'decrypt', necesitamos la matriz inversa
    if mode == 'decrypt':
        # Calcular el determinante de la matriz clave
        det = int(np.round(np.linalg.det(key_matrix))) % 26
        
        # Calcular el inverso modular del determinante
        det_inv = modular_inverse(det, 26)
        
        if det_inv is None:
            raise ValueError("La matriz clave no es invertible en módulo 26. No se puede descifrar.")
            
        # Calcular la matriz adjunta y luego la inversa modular
        adjugate_matrix = np.round(det * np.linalg.inv(key_matrix)).astype(int) % 26
        key_matrix = (det_inv * adjugate_matrix) % 26

    # --- 2. Relleno del mensaje ---
    # Si la longitud del mensaje no es múltiplo del tamaño de la matriz, añadir 'X'
    if len(message) % n != 0:
        padding_needed = n - (len(message) % n)
        message += 'X' * padding_needed
        
    # --- 3. Proceso de cifrado/descifrado ---
    processed_text = ""
    for i in range(0, len(message), n):
        # Tomar un bloque de texto del tamaño 'n'
        block = message[i:i+n]
        
        # Convertir el bloque de letras a un vector de números (A=0, B=1, ...)
        block_vector = np.array([ord(char) - ord('A') for char in block])
        
        # Multiplicar el vector por la matriz clave
        result_vector = np.dot(key_matrix, block_vector) % 26
        
        # Convertir el vector resultante de nuevo a letras
        processed_block = ''.join([chr(int(num) + ord('A')) for num in result_vector])
        processed_text += processed_block
        
    return processed_text

# --- Ejemplo de uso ---
if __name__ == "__main__":
    # Mensaje original
    plaintext = "ACT"
    
    # Clave como una matriz 3x3 de numpy.
    # Esta clave DEBE ser invertible en módulo 26.
    # El determinante no puede ser 0, 2, o 13.
    # GYBNQKURP -> [[6, 24, 1], [13, 16, 10], [20, 17, 15]]
    key = np.array([
        [6, 24, 1],
        [13, 16, 10],
        [20, 17, 15]
    ])

    print(f"Mensaje Original: {plaintext}")
    print(f"Matriz Clave:\n{key}\n")

    # --- Cifrado ---
    try:
        ciphertext = hill_cipher(plaintext, key, mode='encrypt')
        print(f"Texto Cifrado: {ciphertext}")

        # --- Descifrado ---
        decrypted_text = hill_cipher(ciphertext, key, mode='decrypt')
        # La función de descifrado eliminará las 'X' de relleno si se añadieron
        print(f"Texto Descifrado: {decrypted_text}")

    except ValueError as e:
        print(f"Error: {e}")

    print("\n--- Otro ejemplo con una matriz 2x2 ---")
    plaintext_2 = "HELP"
    key_2 = np.array([
        [3, 3],
        [2, 5]
    ])

    print(f"Mensaje Original: {plaintext_2}")
    print(f"Matriz Clave:\n{key_2}\n")

    try:
        ciphertext_2 = hill_cipher(plaintext_2, key_2, mode='encrypt')
        print(f"Texto Cifrado: {ciphertext_2}")

        decrypted_text_2 = hill_cipher(ciphertext_2, key_2, mode='decrypt')
        print(f"Texto Descifrado: {decrypted_text_2}")
    
    except ValueError as e:
        print(f"Error: {e}")