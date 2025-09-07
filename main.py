import pygame

#inicializando o Pygame
pygame.init()

#Definindo o tamanho da janela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.dispalay.set_caption("Coca-Collastic Game.")

#loop principal do jogo
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #atualizar a tela
    pygame.display.flip()

#finalizar o Pygame
pygame.quit()
