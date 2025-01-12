def separar_numeros(lista):
    negativos = sorted([num for num in lista if num < 0])
    positivos = sorted([num for num in lista if num > 0])
    return negativos, positivos

if __name__ == "__main__":
    entrada = input("Introduce una lista de números enteros separados por comas: ")
    lista_numeros = list(map(int, entrada.split(",")))

    negativos, positivos = separar_numeros(lista_numeros)

    print(f"Números negativos ordenados: {negativos}")
    print(f"Números positivos ordenados: {positivos}")