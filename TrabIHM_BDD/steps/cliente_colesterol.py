from behave import then
from lanchonete import *

@then("um problema de colesterol deve ser encontrado")
def when_checar_colesterol(context):
    assert context.colesterol == 1

@then("um problema de colesterol nao deve ser encontrado")
def when_checar_colesterol(context):
    assert context.colesterol == 0
