City = input("Ingrese el nombre de la ciudad a estudiar: ")

Data_in = input("Ingrese la precipitación total anual (mm) y la temperatura media anual (°C) separados por coma (,): ")

# Separar datos
Valor = Data_in.split(",")

# Convertir a float y crear tupla
Data = (float(Valor[0]), float(Valor[1]))

# Calcular índice usando la tupla
Ind = Data[0] / (Data[1] + 10)

print("El índice de Aridez en el municipio de", City, "es de:", Ind)

if Ind <= 5:
    print("La categoría climática de", City, "es Desértico (Hiperárido)")
elif Ind <= 10:
    print("La categoría climática de", City, "es Semidesértico (Árido)")
elif Ind <= 20:
    print("La categoría climática de", City, "es Semiárido mediterráneo")
elif Ind <= 30:
    print("La categoría climática de", City, "es Subhúmedo")
elif Ind <= 60:
    print("La categoría climática de", City, "es Húmedo")
else:
    print("La categoría climática de", City, "es Perhúmedo")
