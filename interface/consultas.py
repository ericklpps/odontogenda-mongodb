from pymongo import MongoClient
from bson import ObjectId

client = MongoClient("mongodb://localhost:27017/")
db = client.consultas_db

def parse_id(id_str):
    try:
        return ObjectId(id_str)
    except:
        return int(id_str)

def inserir_consulta():
    paciente_id = input("ID do Paciente: ")
    dentista_id = input("ID do Dentista: ")
    data = input("Data da Consulta (YYYY-MM-DD): ")
    procedimento = input("Procedimento: ")
    valor = float(input("Valor (R$): "))
    status = input("Status (confirmada/pendente/cancelada): ")
    metodo_pagamento = input("Método de Pagamento: ")
    hora = input("Hora (HH:MM): ")
    observacoes = input("Observações: ")
    
    consulta = {
        "paciente_id": parse_id(paciente_id),
        "dentista_id": parse_id(dentista_id),
        "data": data,
        "procedimento": procedimento,
        "valor": valor,
        "status": status,
        "metodo_pagamento": metodo_pagamento,
        "hora": hora,
        "observacoes": observacoes
    }

    db.consultas.insert_one(consulta)
    print("\n Consulta inserida com sucesso!\n")


def visualizar_consultas():
    print("\n Lista de Consultas:")
    for consulta in db.consultas.find():
        print(consulta)


def atualizar_consulta():
    consulta_id = input("\nDigite o ID da consulta a ser atualizada (ObjectId ou inteiro): ")
    
    print("\nCampos disponíveis para atualização:")
    print("1. Paciente ID")
    print("2. Dentista ID")
    print("3. Data")
    print("4. Procedimento")
    print("5. Valor")
    print("6. Status")
    print("7. Método de Pagamento")
    print("8. Hora")
    print("9. Observações")
    
    campo = input("\nQual campo deseja atualizar? (Digite o número): ")
    novo_valor = input("Novo valor: ")

    campos_disponiveis = ["paciente_id", "dentista_id", "data", "procedimento", "valor", "status", "metodo_pagamento", "hora", "observacoes"]
    
    if campo.isdigit() and 1 <= int(campo) <= len(campos_disponiveis):
        campo_selecionado = campos_disponiveis[int(campo) - 1]
        
        if campo_selecionado in ["paciente_id", "dentista_id"]:
            novo_valor = parse_id(novo_valor)
        elif campo_selecionado == "valor":
            novo_valor = float(novo_valor)

        db.consultas.update_one({"_id": parse_id(consulta_id)}, {"$set": {campo_selecionado: novo_valor}})
        print("\n Consulta atualizada com sucesso!")
    else:
        print("\n Campo inválido, tente novamente.")


def excluir_consulta():
    consulta_id = input("\nDigite o ID da consulta a ser excluída (Somente números): ")
    confirmacao = input("Tem certeza que deseja excluir esta consulta? (s/n): ").lower()
    
    if confirmacao == "s":
        db.consultas.delete_one({"_id": parse_id(consulta_id)})
        print("\n Consulta excluída com sucesso!")
    else:
        print("\n Exclusão cancelada.")


def menu():
    while True:
        print("\nMenu Consultas:")
        print("1. Inserir Consulta")
        print("2. Visualizar Consultas")
        print("3. Atualizar Consulta")
        print("4. Excluir Consulta")
        print("5. Sair")

        escolha = input("\nEscolha uma opção: ")

        if escolha == "1":
            inserir_consulta()
        elif escolha == "2":
            visualizar_consultas()
        elif escolha == "3":
            atualizar_consulta()
        elif escolha == "4":
            excluir_consulta()
        elif escolha == "5":
            print("\n Encerrando...")
            break
        else:
            print("\n Opção inválida, tente novamente.")

menu()
