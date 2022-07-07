Feature: Reconhecer cliente pela foto

Scenario: Um visitante chega a lanchonete e deve ser reconhecido por uma camera
    Given o ambiente seja preparado com sucesso
    When a foto /home/marcos/Área de Trabalho/Lanchonete_BDD-main/TrabIHM_BDD/faces/Jim1.jpg de um visitante for capturada
    Then um(a) cliente deve ser reconhecido(a)
    When a foto /home/marcos/Área de Trabalho/Lanchonete_BDD-main/TrabIHM_BDD/faces/Michael1.jpg de um visitante for capturada
    Then um(a) cliente deve ser reconhecido(a)

Scenario: Um visitante chega a lanchonete e nao deve ser reconhecido
    Given o ambiente seja preparado com sucesso
    When a foto /home/marcos/Área de Trabalho/Lanchonete_BDD-main/TrabIHM_BDD/faces/Ryan2.jpg de um visitante for capturada
    Then nenhum cliente deve ser reconhecido