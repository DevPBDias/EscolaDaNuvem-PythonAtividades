notas = []

while True:
    try:
        nota_da_prova = float(
            input("Digite a nota da prova (ou 'fim' para encerrar): ").replace(",", ".")
        )
        if nota_da_prova < 0 or nota_da_prova > 10:
            print("Nota inválida. Por favor, insira uma nota entre 0 e 10.")
            continue
        notas.append(nota_da_prova)
    except ValueError:
        entrada = input(
            "Deseja encerrar? Digite 'fim' para encerrar ou 'sim' para continuar: "
        ).lower()
        if entrada == "fim":
            break
        elif entrada != "sim":
            print("Opção inválida. Continuando o registro de notas.")
        continue

media_turma = sum(notas) / len(notas)
if notas:
    print(f"Notas registradas: {notas}")
    print(f"Quantidade de notas registradas: {len(notas)}")
    print(f"Média da turma: {media_turma:.2f}")
else:
    print("Nenhuma nota foi registrada.")
