def Calculo():
    City = input("Ingrese el nombre de la ciudad a estudiar: ")

    Data_in = input("Ingrese la precipitación total anual (mm) y la temperatura media anual (°C) separados por coma (,): ")

    Valor = Data_in.split(",") #Función que permite leer cada valor, separados por coma

    Data = (float(Valor[0]), float(Valor[1])) #Se asigna cada dato en una lista llamada Valor[]

    Ind = Data[0] / (Data[1] + 10) #Se calcula el Indice de Aridez

    if Ind <= 5: #Inicio de la comparación con los diferentes índices
        Categoria = "Desértico (Hiperárido)"
    elif Ind <= 10:
        Categoria = "Semidesértico (Árido)"
    elif Ind <= 20:
        Categoria = "Semiárido mediterráneo"
    elif Ind <= 30:
        Categoria = "Subhúmedo"
    elif Ind <= 60:
        Categoria = "Húmedo"
    else:
        Categoria = "Perhúmedo"

    return City, Ind, Categoria #Del bucle for, interesa quedarse con los resultados de estas variables


def Porcentajes(Des, SemiDes, Semiari, Sub, Hum, Per, n):
    Des = (Des * 100) / n
    SemiDes = (SemiDes * 100) / n
    Semiari = (Semiari * 100) / n
    Sub = (Sub * 100) / n
    Hum = (Hum * 100) / n
    Per = (Per * 100) / n

    return Des, SemiDes, Semiari, Sub, Hum, Per


def main():
    n = int(input("Ingrese el número de municipios que quiere estudiar: "))

    Municipios = []

    # Inicializar contadores
    Des = SemiDes = Semiari = Sub = Hum = Per = 0

    for i in range(n):
        print("A continuación, escriba la información del municipio", i + 1)

        Conjunto = Calculo()
        City, Ind, Categoria = Conjunto

        Municipios.append(Conjunto)

        if Categoria == "Desértico (Hiperárido)":
            Des += 1
        elif Categoria == "Semidesértico (Árido)":
            SemiDes += 1
        elif Categoria == "Semiárido mediterráneo":
            Semiari += 1
        elif Categoria == "Subhúmedo":
            Sub += 1
        elif Categoria == "Húmedo":
            Hum += 1
        else:
            Per += 1

    # Calcular porcentajes
    Des, SemiDes, Semiari, Sub, Hum, Per = Porcentajes(Des, SemiDes, Semiari, Sub, Hum, Per, n)

    print("\nPorcentaje de municipios por categoría:")
    print("Desértico (Hiperárido):", Des, "%")
    print("Semidesértico (Árido):", SemiDes, "%")
    print("Semiárido mediterráneo:", Semiari, "%")
    print("Subhúmedo:", Sub, "%")
    print("Húmedo:", Hum, "%")
    print("Perhúmedo:", Per, "%")

    for City, Ind, Categoria in Municipios:
        print("El municipio de", City, "→ Tiene un Índice de:", Ind, "pertenece a la Categoría:", Categoria)


main()