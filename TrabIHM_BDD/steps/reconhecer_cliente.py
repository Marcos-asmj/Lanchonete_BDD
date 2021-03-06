from behave import given, when, then
from lanchonete import *

@given("o ambiente seja preparado com sucesso")
def given_ambiente_preparado(context):
    preparado, context.configuracao = preparar()
    
    assert preparado is True

@when("a foto {foto} de um visitante for capturada")
def when_foto_capturada(context, foto):
    visitante = simular_entrada(foto)
    context.reconhecido, context.cliente, context.colesterol, context.pressao, context.clientes_colesterol, context.clientes_pressao = reconhecer_cliente(visitante, context.configuracao)

    assert True

@then("um(a) cliente deve ser reconhecido(a)")
def then_cliente_reconhecido(context):
    assert context.reconhecido is True

@then("nenhum cliente deve ser reconhecido")
def then_cliente_nao_reconhecido(context):
    assert context.reconhecido is False