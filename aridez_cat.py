City = str(input("Ingrese el nombre de la ciudad a estudiar: "))
Prec = int(input("Ingrese la precipitación total anual (en mm): "))
Temp = float(input("Ingrese la temperatura media anual (en °C): "))
Ind = Prec / ( Temp + 10)
print ("El índice de Aridez en el municipio de", City, "es de:", Ind)

if Ind < 5:
    print ("La categoría climática de", City, "es Desértico (Hiperárido)")
elif (5 < Ind < 10):
    print ("La categoría climática de", City, "es Semidesértico (Árido)")
elif (10 < Ind < 20):
    print ("La categoría climática de", City, "es Semiárido mediterráneo")
elif (20 < Ind < 30):
    print ("La categoría climática de", City, "es Subhúmedo")
elif (30 < Ind < 60):    
    print ("La categoría climática de", City, "es Húmedo")
else:
    print ("La categoría climática de", City, "es Perhúmedo")