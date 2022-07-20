import numpy as np
import pygame
from main import Renderer
from matrix_functions import *

class Object3D():
    def __init__(self, render: Renderer, vertices, faces):
        self.verticies = np.array([np.array(vertex) for vertex in vertices])
        self.faces = np.array([np.array(face) for face in faces])
        self.renderer = render
        self.movement_flag = False
        self.draw_vertices = True 


    def project_to_screen(self):
        vertices = np.matmul(self.verticies, self.renderer.camera.camera_space_projection_matrix())
        vertices = np.matmul(vertices, self.renderer.projection.projection_matrix)

        vertices /= vertices[:, -1].reshape(-1, 1)
        vertices[(vertices > 2) | (vertices < -2)] = 0

        vertices = np.matmul(vertices, self.renderer.projection.screen_projection_matrix)
        vertices = vertices[: , : -2]

        for face in self.faces:
            polygon = vertices[face]
            pygame.draw.polygon(self.renderer.screen, (255,255,255), polygon, 1)





        

    


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
