def adicionar_contato(contatos, nome_contato, telefone, email):
    contato = {"nome": nome_contato, "telefone": telefone, "email": email, "favorito": False}
    contatos.append(contato)
    print("\nContato {nome_contato} adiconado com sucesso!")

def ver_contatos(contatos):
    print("\n Lista de contatos:")
    for indice, contato in enumerate(contatos, start=1):
        favorito = "★" if contato["favorito"] else " "
        nome_contato = contato["nome"]
        print(f"{indice}. [{favorito}] {nome_contato}")


contatos = []

while True:
    print("\n Menu do gerenciador de Lista de contatos:")
    print("1. Adiconar contato")
    print("2. Ver contatos")
    print("3. Atualizar contato")
    print("4. Marcar contato como favorito")
    print("5. Ver contatos favoritos")
    print("6. Deletar contato")
    print("7. Sair")

    escolha = input("Digite sua escolha: ")

    if escolha == "1":
        nome_contato = input("Digite o nome do contato que deseja adicionar:")
        telefone = input("Digite o telefone do contato:")
        email = input("Agora o e-mail:")

        adicionar_contato(contatos, nome_contato, telefone, email)
    
    elif escolha == "2":
        ver_contatos(contatos)
    
    elif escolha == "7":
        break

print("Programa finalizado!")