import numpy as np
import typing

np.set_printoptions(precision=12, suppress=True)

def TranslateMatrix(locX: float, locY: float, locZ: float):
    TranslationMatrix = np.array([
        [1, 0, 0, -locX],
        [0, 1, 0, -locY],
        [0, 0, 1, -locZ],
        [0, 0, 0, 1]
    ], dtype="float64")

    return TranslationMatrix


def RotateXMatrix(Rotation: float):
    RotationMatrix = np.array([
        [np.cos(Rotation), -np.sin(Rotation), 0, 0],
        [np.sin(Rotation), np.cos(Rotation), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1],
    ], dtype="float64")

    return RotationMatrix


def RotateYMatrix(Rotation: float):
    RotationMatrix = np.array([
        [np.cos(Rotation), 0, np.sin(Rotation), 0],
        [0, 1, 0, 0],
        [-np.sin(Rotation), 0, np.cos(Rotation), 0],
        [0, 0, 0, 1],
    ], dtype="float64")

    return RotationMatrix


def RotateZMatrix(Rotation: float):
    RotationMatrix = np.array([
        [1, 0, 0, 0],
        [0, np.cos(Rotation), -np.sin(Rotation), 0],
        [0, np.sin(Rotation), np.cos(Rotation), 0],
        [0, 0, 0, 1]
    ], dtype="float64")

    return RotationMatrix


def ScreenScaleMatrix(f: float, pX: float, pY: float, sX: float, sY: float, s: float):
    ScaleMatrix = np.array([
        [(f * 800) / (2 * sX), s, 0, 0],
        [0, (f * 800) / (2 * sY), 0, 0],
        [0, 0, -1, 0],
        [0, 0, 0, 1]
    ], dtype="float64")

    return ScaleMatrix


def PerspectiveMatrix(z: float):
    factor = 1 / (z) # add a small value to avoid zerodivisionerror

    return np.array([
        [factor, 0, 0, 0],
        [0, factor, 0, 0],
        [0, 0, factor, 0],
        [0, 0, 0, 1]
    ], dtype="float64")


def OffsetMatrix(offsetX, offsetY):
    offset_matrix = np.array([
        [ 1, 0, 0, offsetX ],
        [ 0, -1, 0, offsetY ],
        [ 0, 0, 1, 0 ],
        [ 0, 0, 0, 1 ]
    ], dtype="float64")
    return offset_matrix