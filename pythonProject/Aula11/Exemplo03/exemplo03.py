# Lê o nome e telefone do usuário e grava em contatos.txt

with open('contatos.txt', 'w') as contatos_file:
    while True:
        nome = input("Digite o nome (ou deixe vazio para sair): ")
        if not nome:  # Para se o nome for vazio
            break
        telefone = input("Digite o telefone: ")
        contatos_file.write(f"{nome}, {telefone}\n")  # Grava no arquivo

# Lê e exibe os registros do arquivo contatos.txt
print("\nRegistros gravados em contatos.txt:")
with open('contatos.txt', 'r') as contatos_file:
    for linha in contatos_file:
        print(linha.strip())  # Exibe cada registro