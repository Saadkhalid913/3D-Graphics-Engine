import math
import numpy as np 
import pygame
import time

from projection_utils import OffsetMatrix, PerspectiveMatrix, RotateYMatrix, ScreenScaleMatrix, TranslateMatrix 
from shapes import cube_edges, cube_vertices

width = 800
height = 800

screen = pygame.display.set_mode((width, height))

WHITE = (255, 255, 255)
BLACK = (0,0,0)

screen.fill(BLACK)

f = 0.1
sX = 0.06
sY = 0.048
offsetX = width / 2
offsetY = height / 2,
skew = 0
RotY = 0

offsetX = width / 2
offsetY = height / 2

def GetProjectionCoordinates(point: np.array):
    translation = TranslateMatrix(0,0,4)
    rotYMatrix = RotateYMatrix(RotY)

    scaleMatrix = ScreenScaleMatrix(f, width, height, sX, sY, skew)
    result = np.matmul(translation, point)
    result = np.matmul(rotYMatrix, result)
    result = np.matmul(scaleMatrix, result)

    z = result[2]
    perspectiveMatrix = PerspectiveMatrix(z)
    result = np.matmul(perspectiveMatrix, result)

    offset = OffsetMatrix(offsetX, offsetY)
    result = np.matmul(offset, result)

    return result 



def DrawLine(x1,y1,x2,y2):
    pygame.draw.line(screen, WHITE, (x1,y1), (x2,y2))






running = True
while running:
    screen.fill(BLACK)
    time.sleep(0.1)
    RotY += 0.1

    for edge in cube_edges:
        i1, i2 = edge

        v1, v2 = cube_vertices[i1], cube_vertices[i2],

        v1_prime = GetProjectionCoordinates(v1).astype("int64")
        v2_prime = GetProjectionCoordinates(v2).astype("int64")

        x1,y1,z1,const1 = v1_prime
        x2,y2,z2,const2 = v2_prime
        
        DrawLine(x1,y1,x2,y2)
        # pygame.draw.line(screen, WHITE, (x1,y1), (x2,y2))

  


    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    







  
