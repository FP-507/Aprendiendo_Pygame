import pygame
import constantes

class Personaje():
    def __init__(self, x, y):       
        self.shape = pygame.Rect(0,0, constantes.WIDTH_PLAYER, constantes.HEIGTH_PLAYER)
        self.shape.center = (x,y)
        self.idle = []
        self._charge_animations(self.idle,'Warrior', 'Idle', 8)
        #index de la imagen que se usa actualmente
        self.frame_index = 0
        #tiempo que ha pasado desde que inicio la aplicacion en milisegundos
        self.update_time = pygame.time.get_ticks()
        #animacion que se esta usando actualmente
        self.current_animation= self.idle
        #imagen que tiene el personaje 
        self.image = self.current_animation[self.frame_index]
        
        #defino las listas con las animaciones y las cargo 
        self.left_animation=[]
        self._charge_animations(self.left_animation,'Warrior', 'Run//left', 8)
        self.right_animation=[]
        self._charge_animations(self.right_animation,'Warrior', 'Run//right', 8)
        self.down_animation=[]
        self._charge_animations(self.down_animation,'Warrior', 'Run//down', 8)
        self.up_animation=[]
        self._charge_animations(self.up_animation,'Warrior', 'Run//up', 8)
        
        
    def movimiento(self, delta_x, delta_y): 
        self.shape.x += delta_x
        self.shape.y += delta_y 
        if delta_x> 0: 
            self.current_animation= self.right_animation
        elif delta_x<0:             
            self.current_animation = self.left_animation
        elif delta_y>0:
            self.current_animation= self.down_animation
        elif delta_y<0:
            self.current_animation = self.up_animation
        else:
            self.current_animation = self.idle
         
    def update_animations(self):
        cooldown_animation=100
        self.image= self.current_animation[self.frame_index]
        if pygame.time.get_ticks() - self.update_time >= cooldown_animation: 
            self.frame_index += 1
            self.update_time = pygame.time.get_ticks()
        if self.frame_index >= len(self.current_animation): 
            self.frame_index = 0
       
    def scale(self, image=None, scale= constantes.SCALE_PLAYER): 
        image= pygame.transform.scale(image, (image.get_width()*scale, image.get_height()*scale))
          
    #defino una funcion interna con el personaje para cargar las animaciones 
    def _charge_animations(self,animation:list,character, animacion, cantidad):
        for i in range(cantidad):
            frame = pygame.image.load(f'assets//image//{character}//{animacion}//tile{i}.png')
            self.scale(frame, scale=20)
            animation.append(frame)

    def draw(self, interfaz): 
        #mostramos la imagen del personaje
        interfaz.blit(self.image, self.shape)
   
        
   