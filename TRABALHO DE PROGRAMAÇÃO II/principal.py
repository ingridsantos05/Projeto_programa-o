import funções

def main():
    filmes = {}

    while True:
        funções.exibir_menu()
        
        opcao = input("\nEscolha uma opção: ").strip()
        
        if opcao == '1':
            filme = input("\nDigite o nome do filme que você quer adicionar: ").strip()
            funções.adicionar_filme(filmes, filme)
        
        elif opcao == '2':
            id_filme = input("\nDigite o Id do filme que você quer remover: ").strip()
            try:
                id_filme = int(id_filme)
                funções.remover_filme(filmes, id_filme)

            except ValueError:
                print("\nEntrada inválida. Digite um número inteiro para o ID.")
        
        elif opcao == '3':
            funções.listar_filmes(filmes)
        
        elif opcao == '4':
            funções.listar_filmes(filmes)
            try:
                id_filme = int(input("\nDigite o Id do filme que você quer editar: ").strip())
                novo_nome = input("Digite o nome de um novo filme: ").strip()
                funções.editar_filme(filmes, id_filme, novo_nome)

            except ValueError:
                print("\nEntrada inválida. Digite um número inteiro para o ID.")
        
        elif opcao == '5':
            print("\nSaindo...")
            break
        
        else:
            print("\nOpção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
