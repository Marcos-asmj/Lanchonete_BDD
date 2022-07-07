from behave import when, then
from lanchonete import *

@when("checar se o cliente tem problema de pressao")
def when_checar_pressao(context):
    context.total_clientes_pressao = identificar_pressao(context.clientes_reconhecidos)

@then("{numero_de_clientes_pressao} cliente apresenta problema de pressao")
def then_verificar_clientes_pressao(context, numero_de_clientes_pressao):
    assert context.total_clientes_pressao == int(numero_de_clientes_pressao)