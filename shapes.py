import numpy as np



cube_vertices = [
    np.array([0,0,0,1]),
    np.array([1,0,0,1]),
    np.array([0,1,0,1]),
    np.array([0,0,1,1]),

    np.array([0,1,1,1]),
    np.array([1,1,0,1]),
    np.array([1,0,1,1]),

    np.array([1,1,1,1])
]

cube_edges = [
    [0,1],
    [0,2],
    [0,3],

    [1,6],
    [1,5],

    [2,4],
    [2,5],

    [3,6],
    [3,4],

    [4,7],

    [5,7],

    [6,7],
]

