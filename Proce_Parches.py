# -*- coding: utf-8 -*-
"""
Created on Wed May 20 20:43:16 2020

@author: Pysequi1
"""
#Librerias necesarias
import math
import matplotlib.pyplot as plt
from PIL import Image 
import cv2 
import numpy as np

#Cargamos la imagen
img = cv2.imread("imag.jpg", cv2.IMREAD_GRAYSCALE)
# Las coordenadas del parche que nos interesa
x=145
y=80
Parche=img[x:x+3,y:y+3]
#sacamos su dimención
Fila, Columna = Parche.shape
#Creaos una martiz de ceros con las dimensiones del parche
ParcheLog = np.zeros( (Fila, Columna))

for i in range(0,Fila):
    for j in range(0,Columna):
        #sacamos logaritmo a cada componente del parche (pixel)
        ParcheLog[i, j] = math.log(1+Parche[i,j])
#Restamos la media del parche a cada componente del parche
ParcheLogMed=ParcheLog-ParcheLog.mean() 
#Matriz de contraste
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
xDxT=math.sqrt(np.dot(ParcheLogMed.flatten(), np.dot(D, (ParcheLogMed.flatten().transpose()))))
ParcheNormalizado=ParcheLogMed*(1/xDxT)
#Grafica del los parches

plt.subplot(1, 2, 1)
plt.imshow(Parche, cmap='gray')
plt.subplot(1, 2, 2)
plt.imshow(ParcheNormalizado, cmap='gray')
plt.show()