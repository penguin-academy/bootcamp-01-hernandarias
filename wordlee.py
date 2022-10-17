
import os

def obtener_fila_verificada(palabra_a_encontrar, palabra_ingresada):
    # Crear una lista vacía para el resultado.
    # Si las letras existen en la palabra a encontrar y sus posiciones coinciden: Encerrarlas en [] y agregar al resultado.
    # Si las letras existen en la palabra a encontrar pero sus posiciones no coinciden: Encerrarlas en () y agregar al resultado.
    # Si no se cumple ninguna de las anteriores, agregar al resultado sin hacer modificaciones.
    # Retornar el resultado.
    cantidad_de_letras_de_la_palabra_a_encontrar = 5

    letras_verificadas = [] # Creamos una lista vacía para almacenar el resultado de una linea

    for posicion in range(cantidad_de_letras_de_la_palabra_a_encontrar): # Iteramos por cada letra de la palabra ingresada

        las_letras_son_iguales = palabra_a_encontrar[posicion] == palabra_ingresada[posicion]
        la_letra_existe_en_la_palabra = palabra_ingresada[posicion] in palabra_a_encontrar

        if las_letras_son_iguales:
            # guardar las letras que están en la palabra a encontrar y coinciden en la posición, dentro de brackets
            letras_verificadas.append(f"[{palabra_ingresada[posicion]}]")
        elif la_letra_existe_en_la_palabra:
            # guardar las letras que no coinciden pero que están en la palabra a encontrar, dentro de parentesis
            letras_verificadas.append(f"({palabra_ingresada[posicion]})")
        else:
            # Las que no coinciden, se guardan sin modificiaciones
            letras_verificadas.append(palabra_ingresada[posicion])

    return letras_verificadas


def imprimir_grilla(grilla):
    cantidad_de_filas = len(grilla)

    for fila in range(cantidad_de_filas):
        print(grilla[fila])

# Ejecución del programa

palabra_a_encontrar = "virus"
cantidad_de_letras = 5
intentos = 6

grilla = []

os.system("clear")
print("Bienvenido al wordle!!")

while intentos > 0:
    print(f"te quedan {intentos}")
    palabra_ingresada = input("Ingrese una palabra:")
    intentos = intentos - 1

    os.system("clear")
    if (len(palabra_ingresada) != cantidad_de_letras):
        print("La cantidad de letras es incorrecta")
        print(f"la cantidad de letras correctas es {cantidad_de_letras}")
        continue
    else:
        linea_verificada = obtener_fila_verificada(palabra_a_encontrar, palabra_ingresada)
        grilla.append(linea_verificada)

    imprimir_grilla(grilla)
    if palabra_ingresada == palabra_a_encontrar:
        print("Felicidades, ganaste!!!")
        break