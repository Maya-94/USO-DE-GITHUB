# ordenar_fila_matriz.py
# Programa 2: ordenar una fila de una matriz 3x3 usando Bubble Sort

def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila)

def bubble_sort(lista):
    n = len(lista)
    for i in range(n-1):
        for j in range(n-1-i):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

def main():
    matriz = [
        [9, 2, 8],
        [4, 7, 6],
        [3, 5, 1],
    ]

    print("Matriz original:")
    imprimir_matriz(matriz)

    fila = int(input("¿Qué fila deseas ordenar? (1, 2 o 3): "))
    matriz[fila-1] = bubble_sort(matriz[fila-1])

    print("\nMatriz con la fila ordenada:")
    imprimir_matriz(matriz)

if __name__ == "__main__":
    main()
