try:
    idade = int(input("Digite a sua idade: "))

    if idade > 120:
        print("Segundo a ciência, não existe idade acima de 120 anos")

    if idade >= 60 and idade <= 120:
        print(f"Você é uma pessoa idosa com {idade} anos")
    elif idade >= 18 and idade < 60:
        print(f"Você é um adulto com {idade} anos")
    elif idade >= 13 and idade < 18:
        print(f"Você é um adolescente com {idade} anos")
    elif idade >= 0 and idade < 13:
        print(f"Você é uma criança com {idade} anos")
except ValueError:
    print("Valor inválido, insira um número inteiro e positivo")
