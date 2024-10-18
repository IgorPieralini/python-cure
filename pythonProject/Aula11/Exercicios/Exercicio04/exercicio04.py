import json
import os


# Função para carregar os contatos do arquivo
def carregar_contatos():
    if os.path.exists('agenda.txt'):
        with open('agenda.txt', 'r') as file:
            return json.load(file)
    return {}


# Função para salvar os contatos no arquivo
def salvar_contatos(contatos):
    with open('agenda.txt', 'w') as file:
        json.dump(contatos, file)


# Função para adicionar um novo contato
def adicionar_contato(contatos):
    nome = input("Digite o nome: ")
    sobrenome = input("Digite o sobrenome: ")
    telefone = input("Digite o telefone: ")
    email = input("Digite o e-mail: ")
    contatos[nome] = {
        'sobrenome': sobrenome,
        'telefone': telefone,
        'email': email
    }
    salvar_contatos(contatos)
    print("Contato adicionado com sucesso!")


# Função para procurar um contato pelo nome
def procurar_contato(contatos):
    nome = input("Digite o nome para procurar: ")
    if nome in contatos:
        contato = contatos[nome]
        print(f"Nome: {nome} {contato['sobrenome']}, Telefone: {contato['telefone']}, E-mail: {contato['email']}")
    else:
        print("Contato não encontrado.")


# Função para atualizar um contato
def atualizar_contato(contatos):
    nome = input("Digite o nome do contato a ser atualizado: ")
    if nome in contatos:
        sobrenome = input("Digite o novo sobrenome (deixe em branco para manter): ")
        telefone = input("Digite o novo telefone (deixe em branco para manter): ")
        email = input("Digite o novo e-mail (deixe em branco para manter): ")

        if sobrenome:
            contatos[nome]['sobrenome'] = sobrenome
        if telefone:
            contatos[nome]['telefone'] = telefone
        if email:
            contatos[nome]['email'] = email

        salvar_contatos(contatos)
        print("Contato atualizado com sucesso!")
    else:
        print("Contato não encontrado.")


# Função para apagar um contato
def apagar_contato(contatos):
    nome = input("Digite o nome do contato a ser apagado: ")
    if nome in contatos:
        del contatos[nome]
        salvar_contatos(contatos)
        print("Contato apagado com sucesso!")
    else:
        print("Contato não encontrado.")


# Função principal para executar a agenda
def agenda():
    contatos = carregar_contatos()

    while True:
        print("\nMenu:")
        print("▶ 1 - Novo contato")
        print("▶ 2 - Procura (pelo nome)")
        print("▶ 3 - Atualiza contato")
        print("▶ 4 - Apaga contato")
        print("▶ 0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            adicionar_contato(contatos)
        elif opcao == '2':
            procurar_contato(contatos)
        elif opcao == '3':
            atualizar_contato(contatos)
        elif opcao == '4':
            apagar_contato(contatos)
        elif opcao == '0':
            print("Saindo da agenda.")
            break
        else:
            print("Opção inválida. Tente novamente.")


# Executa a agenda
agenda()