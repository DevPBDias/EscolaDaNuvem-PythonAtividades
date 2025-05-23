while True:
    try:

        valorUm = float(input("Digite o primeiro valor: ").replace(",", "."))
        valorDois = float(input("Digite o segundo valor: ").replace(",", "."))

        operacao = input("Digite a operação desejada (+, -, *, /): ")

        if operacao not in ["+", "-", "*", "/"]:
            print("Erro: Operação inválida. Por favor, escolha entre +, -, * ou /.")
            continue

        if operacao == "+":
            resultado = valorUm + valorDois
        elif operacao == "-":
            resultado = valorUm - valorDois
        elif operacao == "*":
            resultado = valorUm * valorDois
        elif operacao == "/":
            resultado = valorUm / valorDois

        print(
            f"O resultado da operação {valorUm} {operacao} {valorDois} é: {resultado:.2f}"
        )
        break

    except ValueError:
        print(f"Erro: Por favor, insira números válidos para o colocar na calculadora.")
    except ZeroDivisionError:
        print("Erro: Divisão por zero não é permitida.")
