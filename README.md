A continuación el código final desarrollado en clase:
def Calculo():  # Función con la cual se ingresan los datos y se hace el calculo del índice de aridez
    City = input("Ingrese el nombre de la ciudad a estudiar: ")

    Data_in = input("Ingrese la precipitación total anual (mm) y la temperatura media anual (°C) separados por coma (,): ")

    Valor = Data_in.split(",")

    Data = (float(Valor[0]), float(Valor[1]))

    Ind = Data[0] / (Data[1] + 10)

    if Ind <= 5:
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

    return City, Ind, Categoria


def rango_semiarido_mediterraneo(): #Función que brinda los limites inferior y superior del rango semiarido
    li = 10
    ls = 20
    return li, ls


def interpretar_indice(Ind): #Función dependiente de los limites, para mostrar el mensaje interpretativo del rango
    li, ls = rango_semiarido_mediterraneo()

    print("Rango climático de referencia (Semiárido): entre", li, "y", ls)

    if li <= Ind <= ls:
        print("El municipio está DENTRO del rango Semiárido.")
    elif Ind < li:
        print("El municipio está POR DEBAJO del rango (más seco).")
    else:
        print("El municipio está POR ENCIMA del rango (más húmedo).")


def porcentajes_categorias(categorias): #Función que calcula la cantidad de municipios en según qué categoria
    n = len(categorias) #Se extrae la cantidad de datos
    contadores = {} #Contador que servirá para llevar registro de la cantidad de municipios en la categoria

    for categoria in categorias:
        if categoria in contadores:
            contadores[categoria] += 1
        else:
            contadores[categoria] = 1

    print("\nPorcentaje de municipios por categoría:")

    for categoria in contadores: #Se calcula el porcentaje dentro de cada categoria
        porcentaje = (contadores[categoria] * 100) / n
        print(categoria + ":", porcentaje, "%")


def main():
    n = int(input("Ingrese el número de municipios que quiere estudiar: "))

    Municipios = []
    categorias = []

    for i in range(n): #Para una cantidad n de municipios que se van a estudiar, se hará n veces la solicitud de datos
        print("\nMunicipio", i + 1)

        City, Ind, Categoria = Calculo() 

        Municipios.append((City, Ind, Categoria)) #Para llevar control, se guardan los resultados arrojados por la función Calculo
        categorias.append(Categoria)

        interpretar_indice(Ind) #Se utiliza la función del último requisito, donde será dependiente de los limites investigados

    porcentajes_categorias(categorias) #Función para el calculo de porcentajes

    print("\nResultados individuales:")
    for City, Ind, Categoria in Municipios:
        print("Municipio:", City, "→ Índice:", Ind, "| Categoría:", Categoria)


main()
