from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client.consultas_db

def inserir_dentista():
    nome = input("Nome: ")
    especialidade = input("Especialidade: ")
    telefone = input("Telefone: ")
    email = input("Email: ")
    cro = input("CRO: ")
    cidade = input("Cidade: ")
    estado = input("Estado: ")
    cep = input("CEP: ")
    anos_experiencia = int(input("Anos de Experiência: "))
    formacao = input("Formação: ")
    
    dentista = {
        "nome": nome,
        "especialidade": especialidade,
        "telefone": telefone,
        "email": email,
        "cro": cro,
        "cidade": cidade,
        "estado": estado,
        "cep": cep,
        "anos_experiencia": anos_experiencia,
        "formacao": formacao
    }

    db.dentistas.insert_one(dentista)
    print("\n Dentista inserido com sucesso!\n")


def visualizar_dentistas():
    print("\n Lista de Dentistas:")
    for dentista in db.dentistas.find():
        print(dentista)


def atualizar_dentista():
    cro = input("\nDigite o CRO do dentista a ser atualizado: ")
    
    print("\nCampos disponíveis para atualização:")
    print("1. Nome")
    print("2. Especialidade")
    print("3. Telefone")
    print("4. Email")
    print("5. Cidade")
    print("6. Estado")
    print("7. CEP")
    print("8. Anos de Experiência")
    print("9. Formação")
    
    campo = input("\nQual campo deseja atualizar? (Digite o número): ")
    novo_valor = input("Novo valor: ")

    campos_disponiveis = ["nome", "especialidade", "telefone", "email", "cidade", "estado", "cep", "anos_experiencia", "formacao"]
    
    if campo.isdigit() and 1 <= int(campo) <= len(campos_disponiveis):
        campo_selecionado = campos_disponiveis[int(campo) - 1]
        
        # Converte para inteiro se for o campo "anos_experiencia"
        if campo_selecionado == "anos_experiencia":
            novo_valor = int(novo_valor)

        db.dentistas.update_one({"cro": cro}, {"$set": {campo_selecionado: novo_valor}})
        print("\n Dentista atualizado com sucesso!")
    else:
        print("\n Campo inválido, tente novamente.")


def excluir_dentista():
    cro = input("\nDigite o CRO do dentista a ser excluído: ")
    confirmacao = input("Tem certeza que deseja excluir este dentista? (s/n): ").lower()
    
    if confirmacao == "s":
        db.dentistas.delete_one({"cro": cro})
        print("\n Dentista excluído com sucesso!")
    else:
        print("\n Exclusão cancelada.")


def menu():
    while True:
        print("\nMenu Dentistas:")
        print("1. Inserir Dentista")
        print("2. Visualizar Dentistas")
        print("3. Atualizar Dentista")
        print("4. Excluir Dentista")
        print("5. Sair")

        escolha = input("\nEscolha uma opção: ")

        if escolha == "1":
            inserir_dentista()
        elif escolha == "2":
            visualizar_dentistas()
        elif escolha == "3":
            atualizar_dentista()
        elif escolha == "4":
            excluir_dentista()
        elif escolha == "5":
            print("\n Encerrando...")
            break
        else:
            print("\n Opção inválida, tente novamente.")

menu()
