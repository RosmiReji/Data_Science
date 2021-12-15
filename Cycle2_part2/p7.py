#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 12:27:04 2021

@author: sjcet
"""

# Singular-value decomposition
from numpy import array
from scipy.linalg import svd
from numpy import dot
from numpy import diag 
# define a matrix
A = array([[1, 2,1], [3, 4,2], [5, 6,4]])
print(A)
# SVD
U, s, VT = svd(A)
print(U)
print(s)
print(VT)
Sigma=diag(s)
B=U.dot(Sigma.dot(VT))
print(B)