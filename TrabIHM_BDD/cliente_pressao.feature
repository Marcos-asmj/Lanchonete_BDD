Feature: Verificando se o sistema consegue encontrar pacientes com promblemas de pressao

Scenario: Um cliente reconhecido apresentar problemas de pressao
    Given o ambiente seja preparado com sucesso
    When a foto C:/Users/Marcos/Documents/labs/TrabIHM_BDD/faces/Kevin1.jpg de um visitante for capturada
    Then um(a) cliente deve ser reconhecido(a)
    When checar se o cliente tem problema de pressao
    Then 1 cliente apresenta problema de pressao
    When a foto C:/Users/Marcos/Documents/labs/TrabIHM/faces/Pam1.jpg de um visitante for capturada
    Then um(a) cliente deve ser reconhecido(a)
    When checar se o cliente tem problema de pressao
    Then 0 cliente apresenta problema de pressao