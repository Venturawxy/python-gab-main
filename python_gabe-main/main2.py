import pygame
import os

# Definindo o tamanho da janela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_moda((WIDTH, HEIGHT))
pygame.display.set_caption("janela com imagem")

# Definindo a cor de fundo
BG_COLOR = (30, 30, 40) # cor de fundo (um tom escuro)

# Carregar a imagem 
image_file = "rei.png" # coloque o nome da sua imagem aqui
if os.path.exists(image_file):
    img = pygame.imagem.load(image_file).convert_alpha() # Carregar a imagem
    img_rect = img.set_rect(center=(WIDTH // 2, HEIGHT // 2)) #Centraliza a imagem
else:
    print("imagem não encontrada")

    # Loop principal do jogo
    running = True 
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    # Preencher o fundo
    screen.fill(BG_COLOR)

    # Desenhar a imagem na tela
    screen.blit(img, img_rect.topleft)

    # Atualizar a tela
    pygame.display.flip()

# finalizar o Pygame
pygame.quit()