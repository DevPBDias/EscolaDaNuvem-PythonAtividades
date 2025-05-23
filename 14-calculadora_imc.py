try:
    peso = float(input("Digite seu peso em kg: "))
    altura = float(input("Digite sua altura em metros: "))

    calculo_imc = peso / (altura**2)

    mensagem_padrao = f"Seu IMC é: {calculo_imc:.2f}"

    if calculo_imc < 18.5:
        print(f"{mensagem_padrao}. Você está abaixo do peso.")
    elif 18.5 <= calculo_imc < 24.9:
        print(f"{mensagem_padrao}. Você está com o peso normal.")
    elif 25 <= calculo_imc < 29.9:
        print(f"{mensagem_padrao}. Você está com sobrepeso.")
    else:
        print(f"{mensagem_padrao}. Você está obeso.")

except ValueError:
    print("Erro: Por favor, insira valores numéricos válidos para peso e altura.")
