from behave import then
from lanchonete import *

@then("um problema de pressao deve ser encontrado")
def when_checar_pressao(context):
    assert context.pressao == 1

@then("um problema de pressao nao deve ser encontrado")
def when_checar_pressao(context):
    assert context.pressao == 0