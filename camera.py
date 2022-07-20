import numpy as np 
import typing 
import pygame as pg 

from matrix_functions import * 

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

        self.moving_speed = 0.3
        self.rotation_speed = 0.015

    def TranslationMatrix(self):
        x, y , z , constant = self.position

        translation_matrix = np.array([ 
            [1,0,0,0],
            [0,1,0,0],
            [0,0,1,0],
            [-x, -y, -z, 1]
        ])

        return translation_matrix

    def control(self):
        key = pg.key.get_pressed()
        if key[pg.K_a]:
            self.position -= self.right * self.moving_speed
        if key[pg.K_d]:
            self.position += self.right * self.moving_speed
        if key[pg.K_w]:
            self.position += self.forward * self.moving_speed
        if key[pg.K_s]:
            self.position -= self.forward * self.moving_speed
        if key[pg.K_q]:
            self.position += self.up * self.moving_speed
        if key[pg.K_e]:
            self.position -= self.up * self.moving_speed

        if key[pg.K_LEFT]:
            self.camera_yaw(-self.rotation_speed)
        if key[pg.K_RIGHT]:
            self.camera_yaw(self.rotation_speed)
        if key[pg.K_UP]:
            self.camera_pitch(-self.rotation_speed)
        if key[pg.K_DOWN]:
            self.camera_pitch(self.rotation_speed)

    def camera_yaw(self, angle):
        rotate = rotate_y(angle)
        self.forward = self.forward @ rotate
        self.right = self.right @ rotate
        self.up = self.up @ rotate

    def camera_pitch(self, angle):
        rotate = rotate_x(angle)
        self.forward = self.forward @ rotate
        self.right = self.right @ rotate
        self.up = self.up @ rotate


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
