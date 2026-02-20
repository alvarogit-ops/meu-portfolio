tasks = []
opcoes = [
    "1: Adicionar Tarefa",
    "2: Listar Tarefas",
    "3: Remover Tarefa",
    "4: Sair",
]


while True:
    for opcao in opcoes:
        print(opcao)

    try:
        opcao = int(input("Digite uma opção: "))
    except ValueError:
        print("Digite apenas números")
        continue

    if opcao == 1:
        nome_tarefa = input("Digite o nome da tarefa: ")
        tasks.append(nome_tarefa)
        print("Tarefa adicionada")


    elif opcao == 2:
        if not tasks:
            print("As suas opções")
        else:
            for i, tarefa  in enumerate(tasks):
                print(f"{i+1}.{tarefa}")

    elif opcao == 3:    
        if not tasks:
            print("Nenhuma tarefa ")
        else:
            try:
                numero_tarefa = int(input("Digite o número da tarefa "))
                tasks.pop(numero_tarefa - 1)
                print("Tarefa removida")

            except (ValueError, IndexError):
                print("Número inválido")
    

    elif opcao == 4:
        print("Saindo")
        break
    else:
        print("Opção inválida")



   


