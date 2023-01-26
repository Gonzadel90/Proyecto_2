"""
Proyecto Básico de Python (Juego)

Computadora Adivinadora: La computadora debe adivinar el número pensado por el usuario, el numero debe ser del 1 al 20.

"""


import random

# La computadora debe adivinar el número seleccionado por el jugador.
def adivina_el_número_computadora(x):

    print("============================")
    print("  ¡Bienvenido(a) al Juego!  ")
    print("============================")
    print(f"Selecciona un número entre 1 y {x} para que la computadora intente adivinarlo.")

    # Intervalo de valores válidos
    límite_inferior = 1
    límite_superior = x
    respuesta = ""

    while respuesta != "c":
        # Generar predicción
        if límite_inferior != límite_superior:
            predicción = random.randint(límite_inferior, límite_superior)
        else:
            predicción = límite_inferior  # podría ser límite_superior, en este caso es lo mismo.
        # Obtener respuesta del usuario
        respuesta = input(f"Mi predicción es {predicción}. Si es muy alta, ingresa (A). Si es muy baja, ingresa (B). Si es correcta ingresa (C) ").lower()
        
        if respuesta == "a":
            límite_superior = predicción - 1
        elif respuesta == "b":
            límite_inferior = predicción + 1

    print(f"¡Felicitaciones! La computadora adivinó tu número correctamente: {predicción}")


adivina_el_número_computadora(20)