from behave import when, then
from lanchonete import *

@when("checar se o cliente tem problema de colesterol")
def when_checar_colesterol(context):
    context.total_clientes_colesterol = identificar_colesterol(context.clientes_reconhecidos)

@then("{numero_de_clientes_colesterol} cliente apresenta problema de colesterol")
def then_verificar_clientes_colesterol(context, numero_de_clientes_colesterol):
    assert context.total_clientes_colesterol == int(numero_de_clientes_colesterol)