#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    x_square = [[num**2 for num in row] for row in matrix]
    return x_square
