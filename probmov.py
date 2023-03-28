import pygame
from sys import exit #para poder cerrar el juego

#inicializar pygame
pygame.init() 

#crear ventana + resolucion
screen_width = 800
screen_height = 400
screen = pygame.display.set_mode((screen_width,screen_height)) 

#cambiarle el nombre a la ventana
pygame.display.set_caption('adrian keane')

#reloj
clock = pygame.time.Clock()

#imagenes
fondo = pygame.image.load('piso.png')
pj = pygame.image.load('pj.png')
sus = pygame.image.load('sus.png')

#fuente
font1 = pygame.font.Font('minecraft.ttf',32)
texto1 = font1.render('Adrian keane la tiene gorda', False, 'white')
font2 = pygame.font.Font('minecraft.ttf',16)
texto2 = font2.render('https://www.youtube.com/watch?v=AY9MnQ4x3zk 49:30', False, 'white')

pj_x_pos = screen_width/2-8
pj_y_pos = screen_height/2-8

while True:
    #para actualizar siempre la pantalla (y no se vean frames pasados)
    screen.fill(('black'))
    
    #para cerrar el juego con la x
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
            pygame.quit()
            exit()
            
    #fondo repetitivo        
    for y in range(0,screen_height,16):
        for x in range(0,screen_width,16):
            screen.blit(fondo,(x,y))

    #blit = block transfer para pasar de una surface a la display surface
    screen.blit(texto1,(0,0))
    screen.blit(texto2,(0,screen_height-32))
    
    #movimiento
    for event in pygame.event.get():
        if event.type == pygame.K_UP:
            pygame.quit()
            exit()
            
    screen.blit(sus,(screen_width-20,screen_height-20))
    screen.blit(sus,(screen_width-40,screen_height-40))
    screen.blit(pj,(pj_x_pos,screen_height/2-8))

    #repeticion de frames para que el juego continue activo
    pygame.display.update()
    clock.tick(60) #fps
