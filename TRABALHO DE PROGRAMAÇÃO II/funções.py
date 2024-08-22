def adicionar_filme(lista, filme): # Adiciona um novo filme ao dicionário.

    novo_id = max(lista.keys(), default=0) + 1
    lista[novo_id] = filme
    print(f"\nFilme '{filme}' adicionado com o ID {novo_id}.")

def remover_filme(dicionario, id_filme):  #Remove um filme do dicionário com base no id fornecido.

    if id_filme in dicionario:
        filme = dicionario.pop(id_filme)
        print(f"\nFilme '{filme}' com ID {id_filme} removido com sucesso.")
    else:
        print(f"\nFilme com ID {id_filme} não encontrado.")

def listar_filmes(dicionario): # Exibe todos os filmes que o usuario adicionou no dicionário.


    if dicionario:
        print("\nLista de Filmes:")
        for id_filme, filme in dicionario.items():
            print(f"{id_filme}: {filme}")
    else:
        print("\nNenhum filme encontrado.")

def editar_filme(dicionario, id_filme, novo_nome): # Edita o nome do filme que ja e existente no dicionário.

    if id_filme in dicionario:
        dicionario[id_filme] = novo_nome
        print(f"\nFilme com ID {id_filme} atualizado para '{novo_nome}'.")
    else:
        print(f"\nFilme com ID {id_filme} não encontrado.")

def exibir_menu(): #Exibe o menu de opções para o usuário.
    print("\nGerenciador de Filmes")
    print("1. Adicionar filme")
    print("2. Remover filme")
    print("3. Listar filmes")
    print("4. Editar filme")
    print("5. Sair")
