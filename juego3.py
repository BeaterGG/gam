import random
import pygame

pygame.init()

# Configuración de la pantalla
screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))

# Colores
white = (255, 255, 255)
black = (0, 0, 0)

# Jugadores
player1 = pygame.Rect(50, 50, 10, 10)
player2 = pygame.Rect(500, 50, 10, 10)

# Velocidad de movimiento
speed = 1

# Texto en pantalla
font = pygame.font.Font(None, 36)

def display_winner(winner):
    if winner == 1:
        text = font.render("Adrian ha sido cazado por el sus", True, black)
    else:
        text = font.render("El sus ha sido cazado por Adrian", True, black)
    text_rect = text.get_rect(center=(screen_width/2, screen_height/2))
    screen.blit(text, text_rect)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movimiento de los jugadores
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player1.y -= speed
    if keys[pygame.K_s]:
        player1.y += speed
    if keys[pygame.K_a]:
        player1.x -= speed
    if keys[pygame.K_d]:
        player1.x += speed

    if keys[pygame.K_UP]:
        player2.y -= speed
    if keys[pygame.K_DOWN]:
        player2.y += speed
    if keys[pygame.K_LEFT]:
        player2.x -= speed
    if keys[pygame.K_RIGHT]:
        player2.x += speed

    # Colisión con los bordes de la pantalla
    if player1.x < 0:
        player1.x = 0
    if player1.y < 0:
        player1.y = 0
    if player1.x + player1.width > screen_width:
        player1.x = screen_width - player1.width
    if player1.y + player1.height > screen_height:
        player1.y = screen_height - player1.height

    if player2.x < 0:
        player2.x = 0
    if player2.y < 0:
        player2.y = 0
    if player2.x + player2.width > screen_width:
        player2.x = screen_width - player2.width
    if player2.y + player2.height > screen_height:
        player2.y = screen_height - player2.height

    # Colisión entre jugadores
    if player1.colliderect(player2):
        winner = random.choice([1, 2])
        display_winner(winner)
        pygame.display.flip()
        pygame.time.wait(3000)
        running = False

    # Dibujar en pantalla
    screen.fill(white)
    pygame.draw.circle(screen, black, (player1.centerx, player1.centery), player1.width//2)
    pygame.draw.circle(screen, black, (player2.centerx, player2.centery), player2.width//2)
    pygame.display.flip()

pygame.quit()