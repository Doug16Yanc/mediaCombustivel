"Programa feito por meio de paradigma procedimental ou imperativo."

def main():

    totalDistancia = 0
    totalCombustivel = 0


    distancia = float(input("Digite, em quilômetros, a distância percorrida (0 para finalizar):"))

    while (distancia != 0):

        if (distancia != 0):

            litros = float(input("Digite, em litros, a quantidade consumida de combustível:"))

            razao = distancia/litros

            print(f"A razão de consumo foi de {razao:.2f}")

            totalDistancia += distancia
            totalCombustivel += litros

        distancia = float(input("Digite, em quilômetros, a distância percorrida (0 para finalizar):"))

    razaoTotal = totalDistancia/totalCombustivel

    print(f"A razão final de consumo é igual a {razaoTotal :.2f}.")


if __name__:
    main()