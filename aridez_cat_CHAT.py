# aridez_cat.py
def calcular_indice_de_martonne(precipitacion, temperatura):
    """
    Calcula el índice de aridez de De Martonne.
    Parámetros:
    - precipitacion: precipitación anual en mm
    - temperatura: temperatura media anual en °C
    Retorna:
    - Índice de aridez (float)
    """
    return precipitacion / (temperatura + 10)

def clasificar_clima(indice):
    """
    Clasifica el clima a partir del índice de aridez de De Martonne.
    """
    if indice <= 5:
        return "Desértico (árido extremo)"
    elif indice <= 10:
        return "Semidesierto / Árido"
    elif indice <= 20:
        return "Semiárido"
    elif indice <= 30:
        return "Subhúmedo"
    else:
        return "Húmedo / Perhúmedo"

def main():
    print("Clasificación climática según el Índice de De Martonne")
    # Solicitar datos al usuario
    try:
        precip = float(input("Ingrese la precipitación anual (mm): "))
        temp = float(input("Ingrese la temperatura media anual (°C): "))
    except ValueError:
        print("Entrada inválida. Use solo números.")
        return

    # Calcular índice
    indice = calcular_indice_de_martonne(precip, temp)

    # Mostrar resultado
    categoria = clasificar_clima(indice)
    print(f"\nÍndice de De Martonne: {indice:.2f}")
    print(f"Categoría climática: {categoria}")

if __name__ == "__main__":
    main()
