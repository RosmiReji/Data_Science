#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 10:07:49 2022

@author: sjcet
"""

import numpy as np
x=([[4,5],[6,7]])
y=([[4,3],[3,4]])
print(x)
print(y)
print("Subtraction")
print(np.subtract(x,y))
print("Sum of diagonal elements")
print(np.trace(x))
print(np.trace(y))

