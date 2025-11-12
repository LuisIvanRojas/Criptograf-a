#Algoritmo de Euclides Extendido
#Roja Mares Luis Ivan
#Lee Obando Ileana Veronica

def euclides_extendido(a, b):
    """
    Implementa el algoritmo extendido de Euclides.
    Calcula el máximo común divisor (MCD) de dos números enteros a y b,
    junto con los coeficientes (x, y) que cumplen la identidad de Bézout:

        a*x + b*y = MCD(a, b)

    Retorna una tupla con (mcd, x, y).
    """
    # Caso base
    if a == 0:
        return b, 0, 1

    # Paso recursivo
    mcd, x1, y1 = euclides_extendido(b % a, a)

    # Actualización de coeficientes
    x = y1 - (b // a) * x1
    y = x1

    return mcd, x, y


# PROGRAMA PRINCIPAL
if __name__ == "__main__":
    print("ALGORITMO DE EUCLIDES EXTENDIDO")

    while True:
        try:
            num1 = int(input("\nIngrese el primer número (a): "))
            num2 = int(input("Ingrese el segundo número (b): "))

            if num1 < 0 or num2 < 0:
                print("Los números deben ser enteros positivos.")
                continue

            mcd, x, y = euclides_extendido(num1, num2)

            print("\n📊 RESULTADOS:")
            print(f"MCD({num1}, {num2}) = {mcd}")
            print(f"Coeficientes: x = {x}, y = {y}")
            print(f"Comprobación: {num1}({x}) + {num2}({y}) = {num1*x + num2*y}")

        except ValueError:
            print("Entrada inválida. Debe ingresar solo números enteros.")

        opcion = input("\n¿Desea realizar otro cálculo? (s/n): ").lower().strip()
        if opcion != "s":
            print("\nPrograma finalizado. ")
            break
