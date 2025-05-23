while True:
    try:
        senha = input("Digite a senha ou digite 'sair' para encerrar programa: ")

        caracteres = len(senha)

        if senha.lower() == "sair":
            print("Saindo do programa.")
            break

        if caracteres < 8:
            print("A senha deve ter pelo menos 8 caracteres.")
            continue
        elif not any(char.isdigit() for char in senha):
            print("A senha deve conter pelo menos um número.")
            continue
        else:
            print("Senha válida!")
            break

    except ValueError:
        print("Entrada inválida. Tente novamente.")
        continue
