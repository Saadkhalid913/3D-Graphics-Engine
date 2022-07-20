import numpy as np
import pygame
from matrix_functions import *


np.set_printoptions(suppress=True, precision = 2)


class Object3D():
    def __init__(self, render, vertices, faces):
        self.vertices = np.array([np.array(vertex) for vertex in vertices], dtype = "float64")
        self.faces = np.array([np.array(face) for face in faces])
        self.renderer = render
        self.movement_flag = False
        self.draw_vertices = True 
        self.translate([0.0001, 0.0001, 0.0001])



    def draw(self):
        vertices = self.vertices
        vertices = np.matmul(vertices, self.renderer.camera.camera_space_projection_matrix())
        vertices = np.matmul(vertices, self.renderer.projection.projection_matrix)



        vertices /= vertices[:, -1].reshape(-1, 1)
        vertices[(vertices > 2) | (vertices < -2)] = 0

        vertices = np.matmul(vertices, self.renderer.projection.screen_projection_matrix)
        vertices = vertices[: , : -2]
        
        print(vertices)



        for face in self.faces:
            polygon = vertices[face]
            pygame.draw.polygon(self.renderer.screen, (255,255,255), polygon, 1)

    def translate(self, pos):
        self.vertices = np.matmul(self.vertices, translate(pos))



        

    
