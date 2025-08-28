# busqueda_matriz.py
# Programa 1: búsqueda en una matriz 3x3

def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila)

def buscar_valor(matriz, objetivo):
    for i, fila in enumerate(matriz):        # recorrer filas
        for j, valor in enumerate(fila):     # recorrer columnas
            if valor == objetivo:
                return i, j
    return None

def main():
    matriz = [
        [3, 5, 1],
        [9, 2, 8],
        [4, 7, 6],
    ]

    print("Matriz:")
    imprimir_matriz(matriz)

    numero = int(input("Ingresa un número a buscar: "))
    posicion = buscar_valor(matriz, numero)

    if posicion:
        print(f"✅ Encontrado en fila {posicion[0]+1}, columna {posicion[1]+1}")
    else:
        print("❌ No encontrado")

if __name__ == "__main__":
    main()
