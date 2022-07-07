from behave import when, then
from lanchonete import *

@when("o sistema recomenda itens do cardapio ao cliente")
def when_checar_recomendacoes(context):
    context.clientes_que_receberam_recomendacao = recomendar_cardapio(context.cliente)

@then("{numero_de_clientes_recomendados} cliente receberam recomendacao")
def then_verificar_clientes_recomendados(context, numero_de_clientes_recomendados):
    assert context.clientes_que_receberam_recomendacao == int(numero_de_clientes_recomendados)