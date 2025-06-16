import pygame 
import constantes as cons
from personaje import Personaje



player = Personaje(50,50)

pygame.init()

ventana= pygame.display.set_mode((cons.ANCHO_VENTANA, cons.ALTO_VENTANA))

pygame.display.set_caption("Prueba de juego")

#variables de movimiento del jugador
mov_arriba = False
mov_abajo = False
mov_izquierda = False
mov_derecha = False

#controlar el frame rate para que no te muevas muy rapido
reloj= pygame.time.Clock()

run = True 
while run: 

    #definimos los fps que queremos que cargue 
    reloj.tick(cons.FPS)
    
    #damos un color de fondo a pygame
    ventana.fill(cons.BGCOLOR)
    
    #Calcular el movimiento del jugador
    
    #Las variables funcionan para saber que tanto tengo que cambiar mi posicion inicial en el siguiente frame
    delta_x = 0
    delta_y= 0
    
    #logica para el espacio que te vas a mover en el mapa usando las variables delta
    if mov_derecha: 
        delta_x= cons.VELOCIDAD
    elif mov_izquierda: 
        delta_x= -cons.VELOCIDAD
    elif mov_arriba: 
        delta_y= -cons.VELOCIDAD
    elif mov_abajo: 
        delta_y= cons.VELOCIDAD

        
    #llamamos al personaje para moverlo
    player.movimiento(delta_x, delta_y)

    player.draw(ventana)

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT: 
            run = False
        
        #buscamos los tipos de evento que impliquen presionar una tecla
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a: 
                mov_izquierda=True
            elif event.key == pygame.K_d: 
                mov_derecha=True
            elif event.key == pygame.K_w: 
                mov_arriba=True
            elif event.key == pygame.K_s: 
                mov_abajo=True

        #definimos el evento para cuando dejemos de presionar las teclas
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