alunos = []

def estatisticas():
    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
        return

    medias = [a[4] for a in alunos]
    maior = max(medias)
    menor = min(medias)
    geral = sum(medias) / len(medias)
    nome_maior = [a[0] for a in alunos if a[4] == maior][0]

    print(f"Quantidade de alunos: {len(alunos)}")
    for a in alunos:
        print(f"{a[0]} - Notas: {a[1]:.2f}, {a[2]:.2f}, {a[3]:.2f} - Média: {a[4]:.2f} - {a[5]}")
    print(f"Maior média: {maior:.2f}")
    print(f"Menor média: {menor:.2f}")
    print(f"Média geral: {geral:.2f}")
    print(f"Aluno com maior média: {nome_maior}")

while True:
    print("\n------SISTEMA DE CONTROLE DE NOTAS ------")
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Exibir estatísticas")
    print("4 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome: ")
        n1 = float(input("Nota 1: "))
        n2 = float(input("Nota 2: "))
        n3 = float(input("Nota 3: "))

        media = (n1 + n2 + n3) / 3

        if media >= 7:
            situacao = "Aprovado"
        elif media >= 5:
            situacao = "Recuperação"
        else:
            situacao = "Reprovado"

        alunos.append([nome, n1, n2, n3, media, situacao])
        print("Aluno cadastrado!")

    elif opcao == "2":
        if len(alunos) == 0:
            print("Nenhum aluno cadastrado.")
        else:
            for a in alunos:
                print(f"{a[0]} - Notas: {a[1]:.2f}, {a[2]:.2f}, {a[3]:.2f} - Média: {a[4]:.2f} - {a[5]}")

    elif opcao == "3":
        estatisticas()

    elif opcao == "4":
        estatisticas()
        print("Saindo...")
        break

    else:
        print("Opção inválida!")