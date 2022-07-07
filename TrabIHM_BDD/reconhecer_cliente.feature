Feature: Reconhecer cliente pela foto

Scenario: Um cliente chega a hospital e deve ser reconhecido por uma camera
    Given o ambiente seja preparado com sucesso
    When a foto C:/Users/Marcos/Documents/labs/TrabIHM_BDD/faces/Jim1.jpg de um visitante for capturada
    Then um(a) cliente deve ser reconhecido(a)
    When a foto C:/Users/Marcos/Documents/labs/TrabIHM_BDD/faces/Michael1.jpg de um visitante for capturada
    Then um(a) cliente deve ser reconhecido(a)

Scenario: Uma pessoa que nao e paciente chega ao hospital e nao deve ser reconhecida
    Given o ambiente seja preparado com sucesso
    When a foto C:/Users/Marcos/Documents/labs/TrabIHM_BDD/faces/Ryan2.jpg de um visitante for capturada
    Then nenhum cliente deve ser reconhecido