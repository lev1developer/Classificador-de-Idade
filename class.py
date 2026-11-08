def classificar_idade():


    idade = int(input("digite sua idade: "))

    if idade < 0:
        print("Idade inválida")
    elif idade <= 12:
        print("Você é uma criança.")
    elif idade >= 13 and idade <= 17:
        print("Você é um adolescente.")
    elif idade >= 18 and idade <= 59:
        print("Você é um adulto.")
    else:
        print("Você é um idoso.")

classificar_idade()
