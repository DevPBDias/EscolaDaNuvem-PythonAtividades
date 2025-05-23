try:
    ano_bissexto = int(input("Digite um ano: "))

    if (ano_bissexto % 4 == 0 and ano_bissexto % 100 != 0) or (ano_bissexto % 400 == 0):
        print(f"{ano_bissexto} é um ano bissexto.")
    else:
        print(f"{ano_bissexto} não é um ano bissexto.")

except ValueError:
    print("Erro: Por favor, insira um número válido para o ano.")
