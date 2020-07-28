# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 10:39:41 2020

@author: Pysequi1
"""

import math
import matplotlib.pyplot as plt
from PIL import Image 
import cv2 
import numpy as np

def norma(vector):
    D=np.array([[2,-1,0,-1,0,0,0,0,0],
        [-1,3,-1,0,-1,0,0,0,0],
        [0,-1,2,0,0,-1,0,0,0],
        [-1,0,0,3,-1,0,-1,0,0],
        [0,-1,0,-1,4,-1,0,-1,0],
        [0,0,-1,0,-1,3,0,0,-1],
        [0,0,0,-1,0,0,2,-1,0],
        [0,0,0,0,-1,0,-1,3,-1],
        [0,0,0,0,0,-1,0,-1,2]])
    #Calculo de la norma
    xDxT=math.sqrt(np.dot(vector, np.dot(D, (vector.transpose()))))
    return xDxT

def DCT(u,v,Matriz):
    x=3
    y=3
    def Al(e,dim):
        if e==0:
            A = math.sqrt((1/dim))
        else:
            A = math.sqrt((2/dim))
        return A
    valor=0
    for i in range(0,x):
        for j in range(0,y):
            valor=valor+Matriz[i][j]*math.cos((2*i+1)*math.pi*u/(2*x))*math.cos((2*j+1)*v*math.pi/(2*y))
    return Al(u,x)*Al(v,y)*valor

B1=[[1,0,0],[0,0,0],[0,0,0]]
B2=[[0,0,0],[1,0,0],[0,0,0]]
B3=[[0,0,0],[0,0,0],[1,0,0]]
B4=[[0,1,0],[0,0,0],[0,0,0]]
B5=[[0,0,0],[0,1,0],[0,0,0]]
B6=[[0,0,0],[0,0,0],[0,1,0]]
B7=[[0,0,1],[0,0,0],[0,0,0]]
B8=[[0,0,0],[0,0,1],[0,0,0]]
B9=[[0,0,0],[0,0,0],[0,0,1]]
Base=[B1,B2,B3,B4,B5,B6,B7,B8,B9]
vector=[]
for k in range(0,9):
    h=[]
    for i in range(0,3):
        for j in range(0,3):
            h.append(DCT(i,j,Base[k]))
    vector.append((h))
vector=np.array(vector)
vector=np.transpose(vector)
t=[]
for k in range(0,9):
    t.append((1/norma(vector[k]))*vector[k])
t=np.array(t,dtype=np.float16)