#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 20:08:52 2019

@author: steven
"""
import numpy as np
import matplotlib.pyplot as plt
def Imagen(A,Coeficientes):
    i=0
    PivoDistin=False
    MinDimMat=min(len(A[0]),len(A))
    while i < MinDimMat:
        if (A[i][i] ==1 or A[i][i] == -1) or PivoDistin: #pivote distinto 
            for fila in range(i+1,len(A)):
                if A[fila][i] != 0:
                    if Coeficientes == "Z":
                        escalar1=A[i][i]
                        escalar2=A[fila][i]
                        A[fila]=(escalar2)*A[i]-(escalar1)*A[fila]
                    else:
                        A[fila]=(A[i]+A[fila])%2
            i=i+1
        else:
            if i+1 <len(A):
                j=i+1
                MaxDimeMat=True
            else:
                MaxDimeMat=False
            ExiOtroVal=False
            while MaxDimeMat and abs(A[j][i]) != 1 :
                    if A[j][i] != 0:
                        ExiOtroVal=True
                    if j != len(A)-1:
                        MaxDimeMat=True
                        j=j+1
                    else:
                        MaxDimeMat=False
            if i+1 <len(A):
                if j==len(A)-1 and ExiOtroVal:
                    j=i+1
                    while  j !=len(A) -1 and A[j][i] == 0:
                        j=j+1
                    PivoDistin = True
                else:
                    PivoDistin = False
                if j != len(A)-1:
                    for l in range(len(A[j])):
                        b=A[j][l]
                        A[j][l]=A[i][l]
                        A[i][l]=b
                else:
                    i=1+i
            else:
                i=i+1
    if len(A[0])>len(A): 
        k=len(A)-1
        while A[k][k]==0:
            k=k-1
        i=len(A)-1
        Fila=k+1
        while i < len(A[0]) and Fila < len(A):
            if A[Fila][i] !=0:
                for fila in range(Fila+1,len(A)):
                    if A[fila][i] != 0:
                        if Coeficientes == "Z":
                            escalar1=A[fila][i]
                            escalar2=A[Fila][i]
                            A[fila]=escalar1*A[Fila]-escalar2*A[fila]
                        else:
                            A[fila]=(A[Fila]+A[fila])%2
                i=i+1
                Fila=Fila+1
            else:
                if Fila+1 < len(A):
                    j=Fila+1
                    val=0               
                else:
                    val=1 
                while  val!=1 and A[j][i] == 0:
                    if j != len(A)-1:
                        j=j+1
                        val=0
                    else:
                        val=1
                if val==0:
                    for l in range(len(A[j])):
                        b=A[j][l]
                        A[j][l]=A[Fila][l]
                        A[Fila][l]=b
                else:
                    i=i+1
                    Fila=Fila+1   
    for back in range(-(len(A)-1),1):
        j=0
        while A[(-back)][j]==0 and j < len(A[0])-1:
            j=j+1
        if A[(-back)][j] == 1 or A[(-back)][j] ==-1:
            for fila in range((back+1),1):
                if A[(-fila)][j] != 0:
                    if Coeficientes == "Z":
                        escalar1=A[(-fila)][j]
                        escalar2=A[(-back)][j]
                        A[(-fila)]=(escalar1)*A[(-back)]-(escalar2)*A[(-fila)]
                    else:
                        A[(-fila)]=(A[(-back)]+A[(-fila)])%2         
    return A
def ContarPivotes(Matfinal):
    NumPivo=0
    for i in range(0,len(Matfinal)):
        if i < len(Matfinal[0])-1 :
            j=i
        while Matfinal[i][j] == 0 and j < len(Matfinal[0])-1 :
            j=j+1
        if Matfinal[i][j] !=0:
            NumPivo=NumPivo+1
    return NumPivo
def CreMatrixZ(Complex,Simplex,coeficientes):
    Matrixp=np.zeros((len(Complex[Simplex-1]),len(Complex[Simplex])))
    for VarCom in range(0,len(Complex[Simplex])):
        lx =[]
        for CombiSimp in range(0,len(Complex[Simplex][VarCom])):
            Sigma = Complex[Simplex][VarCom][:]
            Sigma.pop(CombiSimp)
            lx.append(Sigma)
        for ki in range(0,len(lx)):
            t=0
            posirotacio=lx[ki][:] 
            interrupcion = True
            sigposi=1
            while lx[ki] != Complex[Simplex-1][t] and interrupcion == True:
                rotavec=1
                posirotacio=lx[ki][:] 
                while rotavec < len(lx[ki]) and Complex[Simplex-1][t]!=posirotacio:
                    posirotacio=posirotacio[-rotavec:] + posirotacio[:-rotavec]
                    rotavec=rotavec+1
                if Complex[Simplex-1][t]==posirotacio:
                    interrupcion = False
                    if coeficientes=="Z":
                        sigposi=-1
                    else:
                        sigposi=1
                else:
                    t=t+1
            if coeficientes=="Z":
                Matrixp[t][VarCom]=(-1)**ki * sigposi
            else:
                Matrixp[t][VarCom]=1
    return Matrixp     
def Calculo(Complejo,coeficientes):
    Imag=[]
    Kernel=[len(Complejo[0])]
    for Simp in range(1,DimCom+1):
        mat=ContarPivotes(Imagen(CreMatrixZ(Complejo,Simp,coeficientes),Coeficiente)) 
        Imag.append(mat)
        Kernel.append(len(Complejo[Simp])-mat)
    Imag.append(0)
    NumBetti=np.array(Kernel)-np.array(Imag)
    return NumBetti
#------------------INGRESO-----------------------------------
print("Bienvenido ")
QuierDefaul=str(input("Este programa ya tiene cargados los complejos del Toro y la botella de Klein quieres calcular alguno de estos (S / N)?:   "))
if QuierDefaul=="S" or QuierDefaul=="s" :
    Coeficiente='Z'
    CualComple=str(input("¿Cúal deseas calcular el Toro (T) o la botella de Klein(K)?: "))
    DimCom=3
    if CualComple=='T':
        img=plt.imread('BotKleTri.png')
        plt.imshow(img)
        plt.show()
        Complex=[[[0],[1], [2], [3], [4], [5], [6], [7], [8]],
              [[0,1],[0,6],[0,7],[1,2],[1,7],[1,8],[2,0],[2,6],[2,8],[3,0],[3,1],[3,4],[4,1],[4,2],[4,5],[5,0],[5,2],[5,3],[6,3],[6,4],[6,7],[7,4],[7,5],[7,8],[8,3],[8,5],[8,6]],
              [[0,1,3],[0,2,6],[0,3,5],[0,5,2],[0,6,7],[0,7,1],[1,2,4],[1,4,3],[1,7,8],[1,8,2],[2,5,4],[2,8,6],[3,4,6],[3,6,8],[3,8,5],[4,5,7],[4,7,6],[5,8,7]]]
        img=plt.imread('Tritoro.png')
        plt.imshow(img)
        plt.show()
        EspTop= 'a el Toro'
    else:
        Complex=[[[0],[1], [2], [3], [4], [5], [6], [7], [8]],
                  [[0,2],[0,6],[0,7],[1,0],[1,6],[1,8],[2,1],[2,7],[2,8],[3,0],[3,1],[3,4],[4,1],[4,2],[4,5],[5,0],[5,2],[5,3],[6,3],[6,4],[6,7],[7,4],[7,5],[7,8],[8,3],[8,5],[8,6]],
                  [[0,1,3],[0,1,6],[0,3,5],[0,5,2],[0,6,7],[0,7,2],[1,2,4],[1,2,8],[1,4,3],[1,8,6],[2,5,4],[2,7,8],[3,4,6],[3,6,8],[3,8,5],[4,5,7],[4,7,6],[5,8,7]]]
        img=plt.imread('BotKleTri.png')
        plt.imshow(img)
        plt.show()
        EspTop= 'a la botella de Klein'
    Calcula=Calculo(Complex,Coeficiente)
    print('El complejo simiplicial asosciado '+ EspTop+ ' es: \n')
    print(Complex)
    print('Los grupos de homología son:')
    for i in range(len(Calcula)):
        if Coeficiente=='Z':
            GrupHom='(+)Z'
            if Calcula[i] != 0:
                print('H_'+ str(i) +' = Z'+ str(GrupHom*(Calcula[i]-1)))
            else:
                print('H_'+ str(i) +' = {0}')
        else:
            GrupHom='(+)Z_2'
            if Calcula[i] != 0:
                print('H_'+ str(i) +' = Z_2'+ str(GrupHom*(Calcula[i]-1)))
            else:
                print('H_'+ str(i) +' = {0}')
    print('Los números de betti son:')
    for i in range(len(Calcula)):
        print('B_'+ str(i) +' = '+ str(Calcula[i]))
else:        
    Coeficiente=str(input("Indica con que coeficientes quieres trabajar: (Z / Z_2): "))
    try:
        Simular='S'
        while Simular=='S' or Simular=='s':
            DimCom=int(input("Ingresa la dimensión del complejo simplicial: "))
            Complejo=[]
            for i in range(0,DimCom+1):
                  cantidad=int(input("Ingresa la cantidad de " + str(i)+"-simplex:  "))
                  if i!=0:
                      print("Ingresa los "+str(i)+"-Simplex")
                  if i==0:
                      a=[]
                      for j in range(0,cantidad):
                          a.append([j])
                      Complejo.append(a)    
                  else:
                      c=[]
                      for j in range(0,cantidad):
                          b= list(map(int, input().split(",")))
                          c.append(b)
                          if len(b)>i+1 or len(b)<i+1:
                              raise ValueError("Dimensión del "+str(i)+"-simplex en la posicion "+str(j)+"No es valido" )
                      Complejo.append(c)
            Calcula=Calculo(Complejo,Coeficiente)
            print('Los grupos de homologia son:')
            for i in range(len(Calcula)):
                if Coeficiente=='Z':
                    GrupHom='(+)Z'
                    if Calcula[i] != 0:
                        print('H_'+ str(i) +' = Z'+ str(GrupHom*(Calcula[i]-1)))
                    else:
                        print('H_'+ str(i) +' = {0}')
                else:
                    GrupHom='(+)Z_2'
                    if Calcula[i] != 0:
                        print('H_'+ str(i) +' = Z_2'+ str(GrupHom*(Calcula[i]-1)))
                    else:
                        print('H_'+ str(i) +' = {0}')
            print('Los números de betti son:')
            for i in range(len(Calcula)):
                print('B_'+ str(i) +'='+ str(Calcula[i]))
            Simular=str(input("Deseas realizar otro calculo (S \ N)?:  "))   
    except ValueError as e:
        print (e)
# #----------------------------RESPUESTA----------------------------------



    
