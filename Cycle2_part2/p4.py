#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 11:05:19 2021

@author: sjcet
"""

import numpy as np
m1 = np.array([[1,4],[2,5]])
m2 = np.array([[1,4],[2,5]])
m3 = np.dot(m1,m2) 
print("multiplication of two matrix")
print(m3)
m4=np.array([[5,6],[1,4]])
m5=np.dot(m3,m4)
print("multiplication of two matrix with third one")
print(m5)