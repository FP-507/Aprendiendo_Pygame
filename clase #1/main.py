import pygame 
import constantes as cons
from personaje import Personaje


#creamos una instancia de Personaje 
player = Personaje(50,50)


#inicializamos pygame
pygame.init()

#definimos variables


#usamos las variables para con el metodo de pygame.display.set_mode usar esas variabels y crear una ventana
ventana= pygame.display.set_mode((cons.ANCHO_VENTANA, cons.ALTO_VENTANA))

#cambiamos el nombre del juego 
pygame.display.set_caption("Prueba de nombre")

#Creamos una funcion para manejar los eventos que ocurren en pantalla y mantener la ventana abierta
run = True 
while run: 
    
    #dibujamos al personaje en la pantalla
    player.draw(ventana)
    
    #usamos pygame.event.get() para obtener todos los eventos que sucedan, de esta forma el for recorre los eventos y sabe como responder a estos
    for event in pygame.event.get():
        
        #creamos un evento para cerrar la ventana
        if event.type == pygame.QUIT: 
            run = False
            
    #hacemos una update constante mientras la app este corriendo para poder mostrar objetos
    pygame.display.update()
        

            
            
pygame.quit()