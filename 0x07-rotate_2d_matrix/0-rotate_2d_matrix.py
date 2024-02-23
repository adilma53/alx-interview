#!/usr/bin/python3
""" rotate_2d_matrix """

def rotate_2d_matrix(matrix):
    """ rotate_2d_matrix """
    matrix[:] = matrix[::-1]
    for i in range(len(matrix)):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
