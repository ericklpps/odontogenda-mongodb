from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client.consultas_db

print("Conexão com o MongoDB estabelecida com sucesso!")

def inserir_paciente():
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    email = input("Email: ")
    cpf = input("CPF: ")
    cidade = input("Cidade: ")
    estado = input("Estado: ")
    cep = input("CEP: ")
    plano_saude = input("Plano de Saúde: ")
    data_nascimento = input("Data de Nascimento (YYYY-MM-DD): ")
    
    paciente = {
        "nome": nome,
        "telefone": telefone,
        "email": email,
        "cpf": cpf,
        "cidade": cidade,
        "estado": estado,
        "cep": cep,
        "plano_saude": plano_saude,
        "data_nascimento": data_nascimento
    }

    db.pacientes.insert_one(paciente)
    print("\n Paciente inserido com sucesso!\n")


def visualizar_pacientes():
    print("\n Lista de Pacientes:")
    for paciente in db.pacientes.find():
        print(paciente)


def atualizar_paciente():
    cpf = input("\nDigite o CPF do paciente a ser atualizado: ")
    
    print("\nCampos disponíveis para atualização:")
    print("1. Nome")
    print("2. Telefone")
    print("3. Email")
    print("4. Cidade")
    print("5. Estado")
    print("6. CEP")
    print("7. Plano de Saúde")
    print("8. Data de Nascimento")
    
    campo = input("\nQual campo deseja atualizar? (Digite o número): ")
    novo_valor = input("Novo valor: ")

    campos_disponiveis = ["nome", "telefone", "email", "cidade", "estado", "cep", "plano_saude", "data_nascimento"]
    
    if campo.isdigit() and 1 <= int(campo) <= len(campos_disponiveis):
        campo_selecionado = campos_disponiveis[int(campo) - 1]
        
        db.pacientes.update_one({"cpf": cpf}, {"$set": {campo_selecionado: novo_valor}})
        print("\n Paciente atualizado com sucesso!")
    else:
        print("\n Campo inválido, tente novamente.")


def excluir_paciente():
    cpf = input("\nDigite o CPF do paciente a ser excluído: ")
    confirmacao = input("Tem certeza que deseja excluir este paciente? (s/n): ").lower()
    
    if confirmacao == "s":
        db.pacientes.delete_one({"cpf": cpf})
        print("\n Paciente excluído com sucesso!")
    else:
        print("\n Exclusão cancelada.")


def menu():
    while True:
        print("\nMenu:")
        print("1. Inserir Paciente")
        print("2. Visualizar Pacientes")
        print("3. Atualizar Paciente")
        print("4. Excluir Paciente")
        print("5. Sair")

        escolha = input("\nEscolha uma opção: ")

        if escolha == "1":
            inserir_paciente()
        elif escolha == "2":
            visualizar_pacientes()
        elif escolha == "3":
            atualizar_paciente()
        elif escolha == "4":
            excluir_paciente()
        elif escolha == "5":
            print("\n Encerrando...")
            break
        else:
            print("\n Opção inválida, tente novamente.")

menu()