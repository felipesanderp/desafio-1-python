def adicionar_contato(contatos, nome_contato, telefone, email):
    contato = {"nome": nome_contato, "telefone": telefone, "email": email, "favorito": False}
    contatos.append(contato)
    print(f"Contato {nome_contato} adiconado com sucesso!")

def ver_contatos(contatos):
    print("\n Lista de contatos:")
    for indice, contato in enumerate(contatos, start=1):
        favorito = " ☆ " if contato["favorito"] else " "

        nome_contato = contato["nome"]
        telefone = contato["telefone"]
        email = contato["email"]

        print(f"{indice}. [{favorito}] {nome_contato} | {telefone} | {email}")

def atualizar_contato(contatos, indice_contato, nome_novo_contato, novo_telefone_contato, novo_email_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
        contatos[indice_contato_ajustado]["nome"] = nome_novo_contato
        contatos[indice_contato_ajustado]["telefone"] = novo_telefone_contato
        contatos[indice_contato_ajustado]["email"] = novo_email_contato

        print(f"Contato {indice_contato} atualizado com sucesso!")
    else:
        print("Índice de tarefas inválido.")
    return

def favoritar_contato(contatos, indice_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
        contatos[indice_contato_ajustado]["favorito"] = True
        print(f"Contato {indice_contato} marcado como favorito")
    else:
        print("Indice do contato inválido.")
    return

def desmarcar_contato_favorito(contatos, indice_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
        contatos[indice_contato_ajustado]["favorito"] = False
        print(f"Contato {indice_contato} desmarcado como favorito")
    else:
        print("Indice de contato inválido")
    return

def listar_favoritos(contatos):
    for indice, contato in enumerate(contatos, start=1):
        if contato["favorito"]:
            favorito = " ☆ " if contato["favorito"] else " "

            nome_contato = contato["nome"]
            telefone = contato["telefone"]
            email = contato["email"]

            print(f"{indice}. [{favorito}] {nome_contato} | {telefone} | {email}")
           
    return

def apagar_contato(contatos, indice_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    contatos.remove(contatos[indice_contato_ajustado])
    print("Contato removido")
    return