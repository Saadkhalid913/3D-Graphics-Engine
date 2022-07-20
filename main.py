import numpy as np 
import pygame
from camera import Camera
from projection import Projection 
from Object3D import Object3D

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

        self.object = None
    

    def run(self):
        while True:
            self.screen.fill((0,0,0))
            self.object.draw()
            [exit() for i in pygame.event.get() if i.type == pygame.QUIT]


            pygame.display.flip()
            self.clock.tick(self.FPS)
            exit()


if __name__ == '__main__':
    r = Renderer()

    cube_vertices = [
                [0,0,0,1],
                [0,0,1,1],
                [1,0,0,1],
                [1,0,1,1],
                
                [0,1,0,1],
                [0,1,1,1],
                [1,1,0,1],
                [1,1,1,1]
            ]

    cube_faces = [[0,1,2,3], [0,1,4,5], [0,2,4,6], [4,5,6,7], [1,3,5,7], [2,3,6,7]]

    cube = Object3D(r, cube_vertices, cube_faces)
    r.object = cube
    r.run()

    



