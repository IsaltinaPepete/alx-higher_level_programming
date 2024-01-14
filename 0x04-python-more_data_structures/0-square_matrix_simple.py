#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in range(len(matrix)):
        aux = []
        for j in range(len(matrix[0])):
            aux.append(matrix[i][j]**2)
        new_matrix.append(aux)
    return new_matrix
