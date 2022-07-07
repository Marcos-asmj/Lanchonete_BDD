import face_recognition
import secrets
import json

FOTOS = [
    "C:/Users/Marcos/Documents/labs/TrabIHM_BDD/faces/Jim1.jpg",
    "C:/Users/Marcos/Documents/labs/TrabIHM_BDD/faces/Jim2.jpg",

    "C:/Users/Marcos/Documents/labs/TrabIHM_BDD/faces/Kevin1.jpg",
    "C:/Users/Marcos/Documents/labs/TrabIHM_BDD/faces/Kevin2.jpg",

    "C:/Users/Marcos/Documents/labs/TrabIHM_BDD/faces/Michael1.jpg",
    "C:/Users/Marcos/Documents/labs/TrabIHM_BDD/faces/Michael2.jpg",

    "C:/Users/Marcos/Documents/labs/TrabIHM_BDD/faces/Pam1.jpg",
    "C:/Users/Marcos/Documents/labs/TrabIHM_BDD/faces/Pam2.jpg",

    "C:/Users/Marcos/Documents/labs/TrabIHM_BDD/faces/Ryan2.jpg",
    "C:/Users/Marcos/Documents/labs/TrabIHM_BDD/faces/Ryan2.jpg"
]

CONFIGURACAO = "C:/Users/Marcos/Documents/labs/TrabIHM_BDD/configuracao.json"

def preparar():
    global configuracao

    configuracao = None
    with open(CONFIGURACAO, "r") as arquivo_configuracao:
        configuracao = json.load(arquivo_configuracao)
        if configuracao:
            print("Configuracao carregada. ")

    return (configuracao != None), configuracao

def simular_entrada(foto):
    visitante = {
        "foto": foto,
        "cliente": None
    }

    return visitante

def reconhecer_cliente(visitante, configuracao):

    print("Iniciando reconhecimento de cliente...")
    foto_visitante = face_recognition.load_image_file(visitante["foto"])
    encoding_foto_visitante = face_recognition.face_encodings(foto_visitante)[0]

    reconhecido = False
    for cliente in configuracao["clientes"]:
        fotos_banco = cliente["fotos"]
        total_reconhecimentos = 0

        for foto in fotos_banco:
            foto_banco = face_recognition.load_image_file(foto)
            encoding_foto_banco = face_recognition.face_encodings(foto_banco)[0]

            foto_reconhecida = face_recognition.compare_faces([encoding_foto_visitante], encoding_foto_banco)[0]
            if foto_reconhecida:
                total_reconhecimentos += 1

        if total_reconhecimentos/len(fotos_banco) > 0.7:
            reconhecido = True

    return reconhecido, visitante

def imprimir_cliente(cliente):
    print("nome:", cliente["clientes"]["nome"])

    if cliente["clientes"]["pressao"] == 1:    
        print("cliente com problema de pressao")
    else:
        print("cliente sem problema de pressao")

    if cliente["clientes"]["colesterol"] == 1:    
        print("cliente com problema de colesterol")
    else:
        print("cliente sem problema de colesterol")

def reconhecer_visitante(clientes_reconhecidos):
    visitante = simular_entrada()
    reconhecido, paciente = reconhecer_cliente(visitante)
    if reconhecido:
        id_cliente = secrets.token_hex(nbytes=16).upper()
        clientes_reconhecidos[id_cliente] = paciente

        print("Cliente reconhecido: ")
        imprimir_cliente(paciente)

    else:
        print("Cliente não reconhecido.")

def identificar_colesterol(pacientes_reconhecidos):
    total_clientes_colesterol = 0

    if len(pacientes_reconhecidos):
        for id_atendimento, paciente in list(pacientes_reconhecidos.items()):
            if paciente["clientes"]["colesterol"] == 1:
                total_clientes_colesterol += 1
                
                pacientes_reconhecidos.pop(id_atendimento)

    return total_clientes_colesterol

def identificar_pressao(pacientes_reconhecidos):
    total_clientes_pressao = 0

    if len(pacientes_reconhecidos):
        for id_atendimento, paciente in list(pacientes_reconhecidos.items()):
            if paciente["clientes"]["pressao"] == 1:
                total_clientes_pressao += 1
                
                pacientes_reconhecidos.pop(id_atendimento)

    return total_clientes_pressao
 

def recomendar_cardapio(clientes_reconhecidos):
    clientes_que_receberam_recomendacao = 0

    if len(clientes_reconhecidos):
        for id_cliente, cliente in list(clientes_reconhecidos.items()):
            if cliente["clientes"]["pressao"] == 1:
                if cliente["clientes"]["colesterol"] == 1:
                    print("Pratos nao recomendados: X-Burguer, Batata-Frita, Refrigerante.")
                    print("Pratos recomendados: Suco natural, X-Salada.")
                    clientes_que_receberam_recomendacao += 1
                    clientes_reconhecidos.pop(id_cliente)
                else: 
                    print("Prato nao recomendado: Batata-Frita.")
                    print("Prato recomendado: X-Salada.")
                    clientes_que_receberam_recomendacao += 1
                    clientes_reconhecidos.pop(id_cliente)
            else:
                if cliente["clientes"]["colesterol"] == 1:
                    print("Pratos nao recomendados: X-Burguer, Refrigerante.")
                    print("Pratos recomendados: Suco natural, X-Salada.")
                    clientes_que_receberam_recomendacao += 1
                    clientes_reconhecidos.pop(id_cliente)
                else: 
                    print("Nenhuma sugestao")
                    print("Nenhuma sugestao")
                    clientes_que_receberam_recomendacao += 1
                    clientes_reconhecidos.pop(id_cliente)

    return clientes_que_receberam_recomendacao
