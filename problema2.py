import string


def contar_palabras(texto):
    # Eliminar signos de puntuación y convertir a minúsculas
    texto = texto.translate(str.maketrans('', '', string.punctuation)).lower()

    # Dividir el texto en palabras
    palabras = texto.split()

    # Contar frecuencias usando un diccionario
    frecuencias = {}
    for palabra in palabras:
        if palabra in frecuencias:
            frecuencias[palabra] += 1
        else:
            frecuencias[palabra] = 1

    # Devolver las palabras ordenadas por su clave
    return dict(sorted(frecuencias.items()))


if __name__ == "__main__":
    # Solicitar entrada del usuario
    texto = input("Introduce una frase o párrafo: ")

    # Contar las palabras
    frecuencias = contar_palabras(texto)

    # Mostrar resultados
    print("\nFrecuencia de palabras:")
    for palabra, frecuencia in frecuencias.items():
        print(f"{palabra}: {frecuencia}")
