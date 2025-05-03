def adicionar_tarefa(lista_de_tarefas, tarefa):
    #Adiciona nova tarefa a uma lista pré-existente
    lista_de_tarefas.append(tarefa)
    print("Tarefa adicionada com sucesso!")
    return lista_de_tarefas

def listar_tarefas(lista_de_tarefas):
    #Exibe a lista de tarefas que foi adicionada e numera
    print("~" * 50)
    print(f"{' ' * 15}Lista de tarefas")
    print("-" * 50)
    n = 1
    for tarefa in lista_de_tarefas:
            print(f"{n} - {tarefa}")
            n = n + 1
    print("~" * 50)

def deletar_tarefa(lista_de_tarefas, tarefa):
    #Deleta uma tarefa que foi adicionada a partir do número dela
    lista_de_tarefas.pop((tarefa - 1))
    return lista_de_tarefas

def exibir_menu():
    #Exibe menu com as opções funcionais para o usuario
    print("Escolha uma opção: \n" \
    "1 - Inserir nova tarefa\n" \
    "2 - Listar tarefas \n" \
    "3 - Deletar tarefa\n"
    "4 - Sair")


#Inicialização de variáveis
lista_de_tarefas = []
continuar = True

#Cabeçalho do programa
print("Seja bem vindo(a/e) à sua lista de tarefas!")

#Loop principal
while continuar:
    exibir_menu()
    opcao = input("Insira o que deseja fazer: ")

    if opcao == "1":
        tarefa = input('Insira uma nova tarefa: ')
        lista_de_tarefas = adicionar_tarefa(lista_de_tarefas, tarefa)
    elif opcao == "2":
        listar_tarefas(lista_de_tarefas)
    elif opcao == "3":
        tarefa = input('Insira o número da tarefa que deseja deletar: ')
        if not tarefa.isnumeric(): 
            print("Número inválido! Tente novamente.")
        elif int(tarefa) > len(lista_de_tarefas):
            print("Número inválido! Tente novamente.")
        elif int(tarefa) <= 0:
            print("Número inválido! Tente novamente.")
        else:
            deletar_tarefa(lista_de_tarefas, int(tarefa))
    elif opcao == "4":
        continuar = False
    else:
        print("Opção inválida! Por favor, tente novamente.")
    print('\n')