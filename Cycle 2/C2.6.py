#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 12:06:16 2021

@author: sjcet
"""
import numpy as np
x=np.array([[2,4,6,1],[6,8,20,1],[1,2,1,1],[1,1,1,1]])
print(x)
print("display all elements excluding the first row")
print(x[1:])
print("Display all elements excluding the last column")
print(x[:,:3])
print("Display the elements of 2nd and  3rd column")
print(x[:,1:3])
print("Display the elements of 1st and and 2nd column in 2nd and 3rd column")
print("Display 2nd and 3rd element of  1st row")
print(x[0,1])
print(x[0,2])

