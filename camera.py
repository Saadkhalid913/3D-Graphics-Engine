import numpy as np 
import typing 


class Camera():

    def __init__(self, render, position):

        self.h_fov = np.pi / 3 
        self.v_fov = self.h_fov * (render.height / render.width)
        self.position = np.array([*position, 1.0], dtype = "float64") # add 1 for homogeneous coordinates 

        # movement vectors 
        self.right = np.array([1,0,0,1])
        self.up = np.array([0,1,0,1])
        self.forward = np.array([0,0,1,1])

        self.near_plane = 0.1
        self.far_plane = 100 

    def TranslationMatrix(self):
        x, y , z , constant = self.position

        translation_matrix = np.array([ 
            [1,0,0,0],
            [0,1,0,0],
            [0,0,1,0],
            [-x, -y, -z, 1]
        ])

        return translation_matrix

    def RotationMatrix(self):

        rx,ry,rz,w = self.right
        fx,fy,fz,w = self.up
        ux,uy,uz,w = self.forward
            
        rotation_matrix = np.array([
            [rx,ry,rz, 0],
            [fx,fy,fz, 0],
            [ux,uy,uz, 0],
            [0,0,0,1],
        ])

        return rotation_matrix 

    
    def camera_space_projection_matrix(self):
        rotation_matrix = self.RotationMatrix()
        translation_matrix = self.TranslationMatrix()
        return np.matmul(translation_matrix, rotation_matrix)
