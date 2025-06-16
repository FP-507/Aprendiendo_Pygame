import pygame
import constantes

class Personaje():
    def __init__(self, x, y):
        
        #le damos forma a nuestro personaje con pygame.Rect, pygame. Rect nos crea un rectangulo
        self.shape = pygame.Rect(0,0, constantes.WIDTH_PLAYER, constantes.HEIGTH_PLAYER)
        
        #cuando cree la forma y reciba las coordenadas, se mueve automaticamente a las coordenadas dadas
        self.shape.center = (x,y)
    
    #creamos un metodo para mostrar el personaje en pantalla, en pygame esto se hace con el metodo draw
    def draw(self, interfaz): 
        pygame.draw.rect(interfaz, constantes.COLOR_PLAYER, self.shape)