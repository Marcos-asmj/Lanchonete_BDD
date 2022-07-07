Feature: Verificando se o sistema consegue encontrar pacientes com promblemas de colesterol

Scenario: Um cliente reconhecido apresentar problemas de colesterol
    Given o ambiente seja preparado com sucesso
    When a foto C:/Users/Marcos/Documents/labs/TrabIHM_BDD/faces/Kevin1.jpg de um visitante for capturada
    Then um(a) cliente deve ser reconhecido(a)
    When checar se o cliente tem problema de colesterol
    Then 1 cliente apresenta problema de colesterol
    When a foto C:/Users/Marcos/Documents/labs/TrabIHM/faces/Pam1.jpg de um visitante for capturada
    Then um(a) cliente deve ser reconhecido(a)
    When checar se o cliente tem problema de colesterol
    Then 0 cliente apresenta problema de colesterol