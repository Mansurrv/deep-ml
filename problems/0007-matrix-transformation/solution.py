import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:
    A = np.array(A)
    T = np.array(T)
    S = np.array(S)

    det_T = np.linalg.det(T)
    det_S = np.linalg.det(S)
    if det_T != 0 and det_S != 0:
        inversed_t = np.linalg.inv(T)
        initial_res = inversed_t @ A
        res = initial_res @ S
        return res
    else:
        return -1

