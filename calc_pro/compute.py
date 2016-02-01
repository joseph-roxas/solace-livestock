import numpy as np


def compute(A, B, C, D, E, F):
    diff = A-B-C-D-E-F
    return diff

if __name__ == '__main__':
    print(compute(100, 1, 1, 1, 1, 1))
