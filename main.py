from db import get_connection

def adicionar_cliente(nome, email, CPF):
    connection = get_connection()
    cursor = connection.cursor()

    query = "INSERT INTO clientes (nome, email, CPF) VALUES (%s, %s, %s)"
    cursor.execute(query, (nome, email, CPF))
    connection.commit()

    cursor.close()
    connection.close()

def menu():
    print("1. Adicionar cliente.")
    print("2. Listar clientes.")
    print("3. Atualizar cliente.")
    print("4. Deletar cliente.")
    
    opcao =input("Escolha uma opção: ")

    if opcao == "1":
        main()
    elif opcao == "2":
        listar_clientes()
    elif opcao == "3":
        atualizar()
    elif opcao == "4":
        apagar()
    else:
        print("Opção inválida.")

def listar_clientes():
    connection = get_connection()
    cursor = connection.cursor()

    query = "SELECT id, nome, email, CPF FROM clientes"
    cursor.execute(query)
    clientes = cursor.fetchall()

    for cliente in clientes:
        print(f"ID: {cliente[0]}, Nome: {cliente[1]}, Email: {cliente[2]}, CPF: {cliente[3]}")

    cursor.close()
    connection.close()

def atualizar_cliente(nome, email, CPF):
    connection = get_connection()
    cursor = connection.cursor()

    query = "UPDATE clientes SET email = %s, CPF = %s WHERE nome = %s" 
    cursor.execute(query, (email, CPF, nome))
    connection.commit()
    cursor.close()
    connection.close()

def atualizar():
    nome = input("Digite o nome do cliente a ser atualizado: ")
    email = input("Digite o novo email do cliente: ")
    CPF = input("Digite o novo CPF do cliente: ")
    atualizar_cliente(nome, email, CPF)
    print("Cliente atualizado com sucesso!")

def deletar_cliente(nome):
    connection = get_connection()
    cursor = connection.cursor()

    query = "DELETE FROM clientes WHERE nome = %s"
    cursor.execute(query, (nome,))
    connection.commit()

    cursor.close()
    connection.close()

def apagar():
    nome = input("Digite o nome do cliente a ser deletado: ")
    deletar_cliente(nome)
    print("Cliente deletado com sucesso!")

def main():
    nome = input("Digite o nome do cliente: ")
    email = input("Digite o email do cliente: ")
    CPF = input("Digite o CPF do cliente: ")
    adicionar_cliente(nome, email, CPF)
    print("Cliente adicionado com sucesso!")


if __name__ == "__main__":
    menu()