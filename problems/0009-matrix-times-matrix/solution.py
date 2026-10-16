import numpy as np

def matrixmul(a: list[list[int | float]], b: list[list[int | float]]) -> list[list[int | float]] | int:
    a_arr = np.array(a)
    b_arr = np.array(b)
    
    try:
        c = a_arr @ b_arr
        return c.tolist()
    except ValueError:
        return -1