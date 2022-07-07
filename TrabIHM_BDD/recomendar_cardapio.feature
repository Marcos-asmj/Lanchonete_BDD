Feature: Verificando se o sistema consegue recomendar itens do cardapio

Scenario: Um cliente que entrou deve receber recomendacoes do cardapio
    Given o ambiente seja preparado com sucesso
    When a foto C:/Users/Marcos/Documents/labs/TrabIHM/faces/Kevin1.jpg de um visitante for capturada
    Then um(a) cliente deve ser reconhecido(a)
    When o sistema recomenda itens do cardapio ao cliente
    Then 1 cliente recebe recomendacoes