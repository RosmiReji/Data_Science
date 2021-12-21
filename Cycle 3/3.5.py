#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 12:17:43 2021

@author: sjcet
"""


import matplotlib.pyplot as plt
import numpy as np
xpoints = np.array(['walking','cycling','car','bus','train'])
ypoints = np.array([29,15,35,18,3])

plt.bar(xpoints,ypoints,color='green',width=0.1)
plt.title("Transport survey")
plt.xlabel("mode of transport")
plt.ylabel("frequency")

plt.show()