# Solicita la edad y dice si es mayor o menor de edad
try:
    edad = int(input("Introduce tu edad: "))
    if edad < 0:
        print("Edad no válida.")
    elif edad >= 18:
        print("Eres mayor de edad.")
    else:
        print("Eres menor de saedad_cambios.")
except ValueError:
    print("Entrada no válida: introduce un número entero ········23#######.")