import pygame
import os

# Inicializando o Pygame
pygame.init()

# Definindo o tamanho da janela padrão
WIDTH, HEIGHT = 1000, 700  # Tamanho inicial da janela
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)  # Janela redimensionável
pygame.display.set_caption("Ice Game.")

# Definindo a cor de fundo
BG_COLOR = (135,206,235)  # cor de fundo (um tom azul-goiabense)

# Caminho da imagem
image_file = "gelado.png"  # Coloque o nome correto da sua imagem aqui
if os.path.exists(image_file):
    img = pygame.image.load(image_file).convert_alpha()  # Carregar a imagem
    img_rect = img.get_rect(center=(WIDTH // 2, HEIGHT // 2))  # Inicialmente centraliza a imagem
else:
    print("Imagem não encontrada!")

SPEED = 1  

# Variáveis de controle de tamanho
is_maximized = False  # Flag para determinar se está no modo maximizado

# Função para centralizar a imagem
def center_image():
    global img_rect, WIDTH, HEIGHT
    img_rect.center = (WIDTH // 2, HEIGHT // 2)  # Centraliza a imagem com base no tamanho da tela

# Função para alternar para o modo maximizado
def toggle_maximized():
    global is_maximized, screen, WIDTH, HEIGHT, img_rect
    if is_maximized:
        # Voltar ao tamanho normal
        WIDTH, HEIGHT = 800, 600  # Redefine o tamanho para o padrão
        screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
        center_image()  # Centraliza a imagem
        is_maximized = False
    else:
        # Maximizar a janela
        WIDTH, HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h  # Pega a resolução máxima
        screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
        center_image()  # Centraliza a imagem
        is_maximized = True

# Loop principal do jogo
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Fechar a janela
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F11:  # Ativar/Desativar modo maximizado
                toggle_maximized()

    # Atualiza o tamanho da janela em tempo real
    WIDTH, HEIGHT = screen.get_size()  # Pega o tamanho atual da janela
    center_image()  # Centraliza a imagem



    #PEGA AS TECLAS PRESSIONADAS
    keys = pygame.key.get_pressed()

    #movimentação da imagem
    if keys[pygame.K_LEFT]:
        img_rect.x -= SPEED #move para a ESQUERDA
    if keys[pygame.K_RIGHT]:
        img_rect.x += SPEED #move para a DIREITA
    if keys[pygame.K_UP]:
        img_rect.y -= SPEED #move para a CIMA
    if keys[pygame.K_DOWN]:
        img_rect.y += SPEED #move para a BAIXO

    # Preencher o fundo
    screen.fill(BG_COLOR)

    # Desenhar a imagem na tela
    screen.blit(img, img_rect.topleft)

    # Atualizar a tela
    pygame.display.flip()

# Finalizar o Pygame
pygame.quit()