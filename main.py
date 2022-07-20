import numpy as np 
import pygame
from camera import Camera
from projection import Projection 

class Renderer():
    width = 600
    height = 600
    h_height = height // 2
    h_width = width // 2



    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.FPS = 60
        self.clock = pygame.time.Clock()
        self.camera : Camera = Camera(self, (0,0,0))
        self.projection : Projection = Projection(self)
    

    def run(self):
        while True:
            [exit() for i in pygame.event.get() if i.type == pygame.QUIT]
            pygame.display.flip()
            self.clock.tick(self.FPS)

r = Renderer()
r.run()



