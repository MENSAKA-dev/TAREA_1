def main():
    # Solicitar al usuario los dos conjuntos de números
    print("Introduce los elementos del primer conjunto, separados por comas:")
    conjunto1 = set(map(int, input().split(',')))

    print("Introduce los elementos del segundo conjunto, separados por comas:")
    conjunto2 = set(map(int, input().split(',')))

    # Calcular la intersección, unión y diferencia simétrica
    interseccion = conjunto1 & conjunto2
    union = conjunto1 | conjunto2
    diferencia_simetrica = conjunto1 ^ conjunto2

    # Mostrar los resultados
    print("\nResultados:")
    print(f"Intersección (elementos comunes): {interseccion}")
    print(f"Unión (todos los elementos sin duplicados): {union}")
    print(f"Diferencia simétrica (elementos en uno u otro, pero no en ambos): {diferencia_simetrica}")


if __name__ == "__main__":
    main()
