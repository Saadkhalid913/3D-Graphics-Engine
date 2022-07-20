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
        ang = 0.02
        while True:
            self.screen.fill((0,0,0))
            self.object.draw()
            self.camera.control()
            [exit() for i in pygame.event.get() if i.type == pygame.QUIT]
            pygame.display.flip()
            self.clock.tick(self.FPS)
            self.object.rotateY(ang)
            pygame.display.update()
            # exit()



def get_object_from_file(renderer, filename):
        vertex, faces = [], []
        with open(filename) as f:
            for line in f:
                if line.startswith('v '):
                    vertex.append([float(i) for i in line.split()[1:]] + [1])
                elif line.startswith('f'):
                    faces_ = line.split()[1:]
                    faces.append([int(face_.split('/')[0]) - 1 for face_ in faces_])
        return Object3D(renderer, vertex, faces)


if __name__ == '__main__':
    r = Renderer()

    figure = get_object_from_file(r, "trumpet.obj")

    figure.scale(0.01)

    r.object = figure
    r.run()

    



