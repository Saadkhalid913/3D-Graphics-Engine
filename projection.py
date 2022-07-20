import numpy as np


class Projection():

    def __init__(self, render):
        near = render.camera.near_plane
        far = render.camera.far_plane 
        left = -np.tan(render.camera.h_fov / 2)
        right = -left 
        bottom = -np.tan(render.camera.v_fov / 2)
        top = -bottom

        self.projection_matrix = np.array([
            [2 / (right - left), 0,0,0],
            [0, 2 / (top - bottom), 0,0],
            [0,0,(far + near) / (far - near), 1],
            [0,0, -2 * near * far / (far - near), 0]
        ])


        half_width = render.h_width 
        half_height = render.h_height

        self.screen_projection_matrix = np.array([ 
            [half_width, 0,0,0],
            [0,-half_height,0,0],
            [0,0,1,0],
            [half_width, half_height, 0,1]
        ])
