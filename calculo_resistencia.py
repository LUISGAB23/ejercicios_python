# Ejemplo de diccionario para el código de colores
colores = {
    "negro": {"valor": 0, "multiplicador": 1, "tolerancia": 0.20},
    "marron": {"valor": 1, "multiplicador": 10, "tolerancia": 0.01},
    "rojo": {"valor": 2, "multiplicador": 100, "tolerancia": 0.02},
    "naranja": {"valor": 3, "multiplicador": 1000},
    "amarillo": {"valor": 4, "multiplicador": 10000},
    "verde": {"valor": 5, "multiplicador": 100000},
    "azul": {"valor": 6, "multiplicador": 1000000},
    "violeta": {"valor": 7, "multiplicador": 10000000},
    "gris": {"valor": 8, "multiplicador": 100000000},
    "blanco": {"valor": 9, "multiplicador": 1000000000},
    "dorado": {"multiplicador": 0.1, "tolerancia": 0.05},
    "plateado": {"multiplicador": 0.01, "tolerancia": 0.10}
}

def calcular_resistencia_por_colores():
    # Solicitar colores
    color1 = input("Color de la primera banda: ").lower()
    color2 = input("Color de la segunda banda: ").lower()
    color3 = input("Color de la tercera banda (multiplicador): ").lower()
    color4 = input("Color de la cuarta banda (tolerancia, o deja en blanco): ").lower() or "ninguno"

    # Validar los colores
    if color1 not in colores or color2 not in colores or color3 not in colores:
        print("Error: Uno de los colores no es válido.")
        return

    # Calcular valor
    valor_base = (colores[color1]["valor"] * 10) + colores[color2]["valor"]
    multiplicador = colores[color3]["multiplicador"]
    valor_resistencia = valor_base * multiplicador

    # Calcular tolerancia
    if color4 in colores and "tolerancia" in colores[color4]:
        tolerancia = colores[color4]["tolerancia"]
    else:
        tolerancia = 0.20 # Tolerancia por defecto si no hay cuarta banda

    print(f"\nLa resistencia es: {valor_resistencia}Ω ± {tolerancia*100}%")

# Llamar a la función
calcular_resistencia_por_colores()