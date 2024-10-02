import funcoes

contatos = []

while True:
    print("\n Menu do gerenciador de Lista de contatos:")
    print("1. Adiconar contato")
    print("2. Ver contatos")
    print("3. Atualizar contato")
    print("4. Marcar contato como favorito")
    print("5. Desmarcar contato como favorito")
    print("6. Ver contatos favoritos")
    print("7. Deletar contato")
    print("8. Sair")

    escolha = input("Digite sua escolha: ")

    if escolha == "1":
        nome_contato = input("Digite o nome do contato que deseja adicionar: ")
        telefone = input("Digite o telefone do contato: ")
        email = input("Agora o e-mail: ")

        funcoes.adicionar_contato(contatos, nome_contato, telefone, email)
    
    elif escolha == "2":
        funcoes.ver_contatos(contatos)

    elif escolha == "3":
        funcoes.ver_contatos(contatos)
        indice_contato = input("Digite o número do contato que deseja atualizar: ")

        novo_nome = input("Digite o novo nome do contato: ")
        novo_telefone = input("Digite o novo nome da tarefa: ")
        novo_email = input("Digite o novo nome da tarefa: ")

        funcoes.atualizar_contato(contatos, indice_contato, novo_nome, novo_telefone, novo_email)

    elif escolha == "4":
        funcoes.ver_contatos(contatos)
        
        indice_contato = input("Digite o número do contato que deseja favoritar: ")
        
        funcoes.favoritar_contato(contatos, indice_contato)
    
    elif escolha == "5":
        funcoes.ver_contatos(contatos)
        indice_contato = input("Digite o número do contato que deseja retirar dos favoritos: ")
        funcoes.desmarcar_contato_favorito(contatos, indice_contato)
    
    elif escolha == "6":
        funcoes.listar_favoritos(contatos)

    elif escolha == "7":
        funcoes.ver_contatos(contatos)
        indice_contato = input("Digite o número do contato que deseja remover: ")
        funcoes.apagar_contato(contatos, indice_contato)

    elif escolha == "8":
        break

print("Programa finalizado!")