import pygame 
import constantes
from personaje import Personaje

pygame.init()
ventana= pygame.display.set_mode((constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA))


player = Personaje(50,50)

pygame.display.set_caption("Prueba de juego")

mov_arriba = False
mov_abajo = False
mov_izquierda = False
mov_derecha = False

reloj= pygame.time.Clock()

run = True 
while run: 
 
    reloj.tick(constantes.FPS)

    ventana.fill(constantes.BGCOLOR)
    
    delta_x = 0
    delta_y= 0

    if mov_derecha: 
        delta_x= constantes.VELOCIDAD
    elif mov_izquierda: 
        delta_x= -constantes.VELOCIDAD
    elif mov_arriba: 
        delta_y= -constantes.VELOCIDAD
    elif mov_abajo: 
        delta_y= constantes.VELOCIDAD

        
    player.movimiento(delta_x, delta_y)
    player.update_animations()

    player.draw(ventana)

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT: 
            run = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a: 
                mov_izquierda=True
            elif event.key == pygame.K_d: 
                mov_derecha=True
            elif event.key == pygame.K_w: 
                mov_arriba=True
            elif event.key == pygame.K_s: 
                mov_abajo=True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a: 
                mov_izquierda=False
            elif event.key == pygame.K_d: 
                mov_derecha=False
            elif event.key == pygame.K_w: 
                mov_arriba=False
            elif event.key == pygame.K_s: 
                mov_abajo=False
                
            

    pygame.display.update()
                    
            
pygame.quit()