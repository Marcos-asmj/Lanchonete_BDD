Feature: Verificando se o sistema consegue encontrar pacientes com promblemas de pressao

Scenario: Um cliente reconhecido apresentar problemas de pressao
    Given o ambiente seja preparado com sucesso
    When a foto /home/marcos/Área de Trabalho/Lanchonete_BDD-main/TrabIHM_BDD/faces/Kevin1.jpg de um visitante for capturada
    Then um(a) cliente deve ser reconhecido(a)
    And um problema de pressao deve ser encontrado
    When a foto /home/marcos/Área de Trabalho/Lanchonete_BDD-main/TrabIHM_BDD/faces/Pam1.jpg de um visitante for capturada
    Then um(a) cliente deve ser reconhecido(a)
    And um problema de pressao nao deve ser encontrado