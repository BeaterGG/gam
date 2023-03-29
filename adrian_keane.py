import pygame
from sys import exit #para poder cerrar el juego

#inicializar pygame
pygame.init() 

#crear ventana + resolucion
screen_width = 1000
screen_height = 600
screen = pygame.display.set_mode((screen_width,screen_height))

#cambiarle el nombre a la ventana
pygame.display.set_caption('adrian keane')

#reloj
clock = pygame.time.Clock()

#imagenes y rects
fondo = pygame.image.load('piso.png').convert_alpha()
pj_surf = pygame.image.load('pj.png').convert_alpha()
pj_rect = pj_surf.get_rect(centerx = screen_width/2, centery = screen_height/2)
sus_surf = pygame.image.load('sus.png').convert_alpha()
sus_rect = sus_surf.get_rect(right = screen_width, centery = screen_height/2)

#fuente
font = pygame.font.Font('minecraft.ttf',32)
texto1 = font.render('Adrian no toques el sus', False, 'white')
texto1_rect = texto1.get_rect(centerx = screen_width/2, centery = 20)
texto2 = font.render('QUE NO ADRIAN', False, 'white')
texto2_rect = texto2.get_rect(centerx = screen_width/2, centery = screen_height-screen_height/3)
texto3 = font.render('NOOOOOOOO (ahora adrian es sus)', False, 'red')
texto3_rect = texto3.get_rect(centerx = screen_width/2, centery = screen_height/2)
texto4 = font.render('Agarra al Adrian', False, 'lightgrey')
texto4_rect = texto4.get_rect(centerx = screen_width/2, centery = screen_height/3)

while True:
    #repeticion de frames para que el juego continue activo
    pygame.display.update()
    clock.tick(60) #fps
    #para actualizar siempre la pantalla (y no se vean frames pasados)
    screen.fill(('black'))
    
    #para cerrar el juego con la x
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
    #fondo repetitivo        
    for y in range(0,screen_height,16):
        for x in range(0,screen_width,16):
            screen.blit(fondo,(x,y))

    #movimiento
    #pj_rect.centerx += 1

    #blit = block transfer para pasar de una surface a la display surface
    screen.blit(texto1,texto1_rect)

    #colisiones
    mouse_pos = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()
    
    x=1

    if pj_rect.collidepoint(mouse_pos):
        pygame.draw.rect(screen,'black',texto4_rect)
        pygame.draw.rect(screen,'white',texto4_rect,1,6)
        screen.blit(texto4,texto4_rect)

    if mouse_click == (True, False, False):
        x -= 1
        screen.blit(pj_surf,(mouse_pos))
        screen.blit(texto2,texto2_rect)
        if sus_rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen,'black',texto3_rect)
            pygame.draw.rect(screen,'white',texto3_rect,1,6)
            screen.blit(texto3,texto3_rect)
        
    if x==1: screen.blit(pj_surf,pj_rect)

    screen.blit(sus_surf,sus_rect)
    
    
    
    
    
    