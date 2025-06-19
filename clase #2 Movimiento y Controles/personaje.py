import pygame
import constantes

class Personaje():
    def __init__(self, x, y):
        self.shape = pygame.Rect(0,0, constantes.WIDTH_PLAYER, constantes.HEIGTH_PLAYER)
        self.shape.center = (x,y)
    
    #creamos un metodo para mostrar el personaje en pantalla, en pygame esto se hace con el metodo draw
    def draw(self, interfaz): 
        pygame.draw.rect(interfaz, constantes.COLOR_PLAYER, self.shape)
        
    def movimiento(self, delta_x, delta_y): 
        self.shape.x += delta_x
        self.shape.y += delta_y 