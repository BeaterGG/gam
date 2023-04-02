import pygame
from sys import exit #para poder cerrar el juego

#inicializar pygame
pygame.init()

#crear ventana + resolucion
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width,screen_height))

#cambiarle el nombre a la ventana
pygame.display.set_caption('adrian keane')

#reloj
clock = pygame.time.Clock()

#estados del juego
game_active = True

#imagenes y rects
fondo = pygame.image.load('piso.png').convert_alpha()
pj_surf = pygame.image.load('pj.png').convert_alpha()
pj_surf = pygame.transform.rotozoom(pj_surf,0,2)
pj_rect = pj_surf.get_rect(centerx = screen_width/2, centery = screen_height/2)
sus_surf = pygame.image.load('sus2.png').convert_alpha()
sus_rect = sus_surf.get_rect(right = screen_width, centery = screen_height/2)
velocity = 5

#fuente
font1 = pygame.font.Font('minecraft.ttf',32)
texto1 = font1.render('Adrian no toques el sus', False, 'white')
texto1_rect = texto1.get_rect(centerx = screen_width/2, centery = 20)
texto2 = font1.render('QUE NO ADRIAN', False, 'white')
texto2_rect = texto2.get_rect(centerx = screen_width/2, centery = screen_height-screen_height/3)
texto3 = font1.render('NOOOOOOOO (ahora adrian es sus)', False, 'red')
texto3_rect = texto3.get_rect(centerx = screen_width/2, centery = screen_height/2)
texto4 = font1.render('*Agarrar al Adrian*', False, 'lightgrey')
texto4_rect = texto4.get_rect(centerx = screen_width/2, centery = screen_height/3)
font2 = pygame.font.Font('minecraft.ttf',16)
texto5 = font2.render('Presiona espacio para reiniciar', False, 'lightgrey')
texto5_rect = texto5.get_rect(centerx = screen_width/2, centery = screen_height-screen_height/3)
while True:
    #repeticion de frames para que el juego continue activo
    pygame.display.update()
    clock.tick(60) #fps
    
    #para cerrar el juego con la x
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    
    keys = pygame.key.get_pressed()
    if game_active:
        screen.fill(('black'))        
        #fondo repetitivo        
        for y in range(0,screen_height,16):
            for x in range(0,screen_width,16):
                screen.blit(fondo,(x,y))

        #blit = block transfer para pasar de una surface a la display surface
        screen.blit(texto1,texto1_rect)
        screen.blit(pj_surf,pj_rect)
        screen.blit(sus_surf,sus_rect)

        #movivmiento
        if keys[pygame.K_RIGHT]:
            pj_rect.centerx += velocity
        if keys[pygame.K_LEFT]:
            pj_rect.centerx -= velocity
        if keys[pygame.K_UP]:
            pj_rect.centery -= velocity
        if keys[pygame.K_DOWN]:
            pj_rect.centery += velocity
        #colisiones
        if sus_rect.colliderect(pj_rect):
            game_active = False
                
        
    else:
        screen.fill('black')
        screen.blit(texto3,texto3_rect)
        screen.blit(texto5,texto5_rect)
        if keys[pygame.K_SPACE]:
            game_active = True
            pj_rect = pj_surf.get_rect(centerx = screen_width/2, centery = screen_height/2)
