#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 12:25:45 2021

@author: sjcet
"""
import numpy as np
M1 = np.array([[3, 6], [14, 21]])
M2 = np.array([[9, 27], [11, 22]])
M3 = M1 + M2
print("\nMatrix addition")
print(M3)
M1 = np.array([[3, 6], [14, 21]])
M2 = np.array([[9, 27], [11, 22]])

M3 = M1 - M2
print("\nMatrix Substract")
print(M3)
M1 = np.array([[3, 6], [14, 21]])
M2 = np.array([[9, 27], [11, 22]])
M3 = M1 / M2
print("\nDivide the elements of the matrices")
print(M3)

M1 = np.array([[3, 6], [5, -10]])
M2 = np.array([[9, -18], [11, 22]])
M3 = M1 * M2
print("\nMultiply the individual elements of matrix")
print(M3)

M1 = np.array([[3, 6], [5, -10]])
M2 = np.array([[9, -18], [11, 22]])
M3 = M1.dot(M2)
print("\nmatrix multiplication")
print(M3)
M1 = np.array([[3, 6, 9], [5, -10, 15], [4,8,12]])
M2 = M1.transpose()
print("\nTranspose of the matrix")
print(M2)
M1 = np.array([[3, 6, 9], [5, -10, 15], [4,8,12]])
print("\nSum of diagonal elements of a matrix")
print(np.trace(M1))