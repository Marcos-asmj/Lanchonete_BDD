import face_recognition
import secrets
import json

FOTOS = [
    "/home/marcos/Área de Trabalho/Lanchonete_BDD-main/TrabIHM_BDD/faces/Jim1.jpg",
    "/home/marcos/Área de Trabalho/Lanchonete_BDD-main/TrabIHM_BDD/faces/Jim2.jpg",

    "/home/marcos/Área de Trabalho/Lanchonete_BDD-main/TrabIHM_BDD/faces/Kevin1.jpg",
    "/home/marcos/Área de Trabalho/Lanchonete_BDD-main/TrabIHM_BDD/faces/Kevin2.jpg",

    "/home/marcos/Área de Trabalho/Lanchonete_BDD-main/TrabIHM_BDD/faces/Michael1.jpg",
    "/home/marcos/Área de Trabalho/Lanchonete_BDD-main/TrabIHM_BDD/faces/Michael2.jpg",

    "/home/marcos/Área de Trabalho/Lanchonete_BDD-main/TrabIHM_BDD/faces/Pam1.jpg",
    "/home/marcos/Área de Trabalho/Lanchonete_BDD-main/TrabIHM_BDD/faces/Pam2.jpg",

    "/home/marcos/Área de Trabalho/Lanchonete_BDD-main/TrabIHM_BDD/faces/Ryan2.jpg",
    "/home/marcos/Área de Trabalho/Lanchonete_BDD-main/TrabIHM_BDD/faces/Ryan2.jpg"
]

CONFIGURACAO = "/home/marcos/Área de Trabalho/Lanchonete_BDD-main/TrabIHM_BDD/configuracao.json"

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
    colesterol = 0
    pressao = 0
    cliente_colesterol = 0
    cliente_pressao = 0
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
            colesterol = cliente["colesterol"]
            pressao = cliente["pressao"]
            if colesterol == 1:
                cliente_colesterol += 1
            if pressao == 1:
                cliente_pressao += 1
                


    return reconhecido, visitante, colesterol, pressao, cliente_colesterol, cliente_pressao

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
    reconhecido, cliente = reconhecer_cliente(visitante. configuracao)
    if reconhecido:
        id_cliente = secrets.token_hex(nbytes=16).upper()
        clientes_reconhecidos[id_cliente] = cliente

        print("Cliente reconhecido: ")
        imprimir_cliente(cliente)

    else:
        print("Cliente não reconhecido.")

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
