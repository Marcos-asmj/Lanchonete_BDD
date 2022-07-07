Feature: Verificando se o sistema consegue encontrar pacientes com promblemas de colesterol

Scenario: Um cliente reconhecido apresentar problemas de colesterol
    Given o ambiente seja preparado com sucesso
    When a foto /home/marcos/Área de Trabalho/Lanchonete_BDD-main/TrabIHM_BDD/faces/Kevin1.jpg de um visitante for capturada
    Then um(a) cliente deve ser reconhecido(a)
    And um problema de colesterol deve ser encontrado
    When a foto /home/marcos/Área de Trabalho/Lanchonete_BDD-main/TrabIHM_BDD/faces/Pam1.jpg de um visitante for capturada
    Then um(a) cliente deve ser reconhecido(a)
    And um problema de colesterol nao deve ser encontrado