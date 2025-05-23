while True:
    try:
        numero = int(input("Digite um número inteiro ou 'fim' para encerrar): "))

        if numero < 0:
            print("Número inválido. Por favor, insira um número inteiro positivo.")
            continue

        if numero % 2 == 0:
            print(f"{numero} é par.")
            break
        else:
            print(f"{numero} é ímpar.")
            break

    except ValueError:
        saida_usuario = input(
            "Valor inválido. Digite 'fim' para encerrar ou 'sim' para continuar: "
        ).lower()

        if saida_usuario == "fim":
            print("Saindo do programa.")
            break
        else:
            print("Continuando a verificação de par ou ímpar.")
            continue
