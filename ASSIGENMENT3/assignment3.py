# -*- coding: utf-8 -*-
"""ASSIGNMENT3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ANRR_WHpL-QGkdVzfvOGBOxWxns4I0IX
"""

import numpy as np


def dir_vec(A,B):
  return B-A

def norm_vec(A,B):
  return np.matmul(omat, dir_vec(A,B))

#Generate line points
#def line_gen(A,B):
#  len =10
#  dim = A.shape[0]
#  x_AB = np.zeros((dim,len))
#  lam_1 = np.linspace(0,1,len)
#  for i in range(len):
#    temp1 = A + lam_1[i]*(B-A)
#    x_AB[:,i]= temp1.T
#  return x_AB

#Generate line intercepts
def line_icepts(n,c):
  e1 = np.array([1,0]) 
  e2 = np.array([0,1]) 
  A = c*e1/(n@e1)
  B = c*e2/(n@e2)
  return A,B

#Generate line points
def line_dir_pt(m,A,k1,k2):
  len =10
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(k1,k2,len)
  for i in range(len):
    temp1 = A + lam_1[i]*m
    x_AB[:,i]= temp1.T
  return x_AB
#Generate line points

def line_norm_eq(n,c,k):
  len =10
  dim = n.shape[0]
  m = omat@n
  m = m/np.linalg.norm(m)
#  x_AB = np.zeros((dim,2*len))
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(k[0],k[1],len)
#  print(lam_1)
#  lam_2 = np.linspace(0,k2,len)
  if c==0:
    for i in range(len):
      temp1 = lam_1[i]*m
      x_AB[:,i]= temp1.T
  else:
    A,B = line_icepts(n,c)
    for i in range(len):
      temp1 = A + lam_1[i]*m
      x_AB[:,i]= temp1.T
#    temp2 = B + lam_2[i]*m
#    x_AB[:,i+len]= temp2.T
  return x_AB

#def line_dir_pt(m,A, dim):
#  len = 10
#  dim = A.shape[0]
#  x_AB = np.zeros((dim,len))
#  lam_1 = np.linspace(0,10,len)
#  for i in range(len):
#    temp1 = A + lam_1[i]*m
#    x_AB[:,i]= temp1.T
#  return x_AB


#Generate line points
def line_gen(A,B):
  len =10
  x_AB = np.zeros((2,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB

  #Foot of the Altitude
def alt_foot(A,B,C):
  m = B-C
  n = np.matmul(omat,m) 
  N=np.vstack((m,n))
  p = np.zeros(2)
  p[0] = m@A 
  p[1] = n@B
  #Intersection
  P=np.linalg.inv(N.T)@p
  return P

#Intersection of two lines
def line_intersect(n1,c1,n2,c2):
  N=np.vstack((n1,n2))
  p = np.array([c1,c2]) 
  #Intersection
  P=np.linalg.inv(N)@p
#  P=np.linalg.inv(N.T)@p
  return P

#Radius and centre of the circumcircle
#of triangle ABC
def ccircle(A,B,C):
  p = np.zeros(2)
  n1 = dir_vec(B,A)
  p[0] = 0.5*(np.linalg.norm(A)**2-np.linalg.norm(B)**2)
  n2 = dir_vec(C,B)
  p[1] = 0.5*(np.linalg.norm(B)**2-np.linalg.norm(C)**2)
  #Intersection
  N=np.vstack((n1,n2))
  O=np.linalg.inv(N)@p
  r = np.linalg.norm(A -O)
  return O,r

#Radius and centre of the incircle
#of triangle ABC
def icentre(A,B,C,k1,k2):
  p = np.zeros(2)
  t = norm_vec(B,C)
  n1 = t/np.linalg.norm(t)
  t = norm_vec(C,A)
  n2 = t/np.linalg.norm(t)
  t = norm_vec(A,B)
  n3 = t/np.linalg.norm(t)
  p[0] = n1@B- k1*n2@C
  p[1] = n2@C- k2*n3@A
  N=np.vstack((n1-k1*n2,n2-k2*n3))
  I=np.matmul(np.linalg.inv(N),p)
  r = n1@(I-B)
  #Intersection
  return I,r

def mult_line(A_I,b_z,k,m):
 for i in range(m):
  if i == 0:
    x = line_norm_eq(A_I[i,:],b_z[i],k[i,:])
  elif i == 1:
    y = line_norm_eq(A_I[i,:],b_z[i],k[i,:])
    z = np.vstack((x[None], y[None]))
  else:
    x = line_norm_eq(A_I[i,:],b_z[i],k[i,:])
    z = np.vstack((z,x[None]))
 return z

dvec = np.array([-1,1]) 
#Orthogonal matrix
omat = np.array([[0,1],[-1,0]])
# -*- coding: utf-8 -*-
"""Assignment3.ipynb
Automatically generated by Colaboratory.
Original file is located at
https://colab.research.google.com/drive/1DAAmk3YM2oEi5vpgcG7cBX4yL46ZXrxG#scrollTo=rdVdvCd1gVFF  
"""

#Code by C.RAMYA TULASI
#May 27,2021
import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA



# -*- coding: utf-8 -*-
"""assignment3.ipynb
Automatically generated by Colaboratory.
Original file is located at
    https://colab.research.google.com/drive/1DAAmk3YM2oEi5vpgcG7cBX4yL46ZXrxG
"""

import numpy as np


def dir_vec(A,B):
  return B-A

def norm_vec(A,B):
  return np.matmul(omat, dir_vec(A,B))

#Generate line points
#def line_gen(A,B):
#  len =10
#  dim = A.shape[0]
#  x_AB = np.zeros((dim,len))
#  lam_1 = np.linspace(0,1,len)
#  for i in range(len):
#    temp1 = A + lam_1[i]*(B-A)
#    x_AB[:,i]= temp1.T
#  return x_AB

#Generate line intercepts
def line_icepts(n,c):
  e1 = np.array([1,0]) 
  e2 = np.array([0,1]) 
  A = c*e1/(n@e1)
  B = c*e2/(n@e2)
  return A,B

#Generate line points
def line_dir_pt(m,A,k1,k2):
  len =10
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(k1,k2,len)
  for i in range(len):
    temp1 = A + lam_1[i]*m
    x_AB[:,i]= temp1.T
  return x_AB
#Generate line points

def line_norm_eq(n,c,k):
  len =10
  dim = n.shape[0]
  m = omat@n
  m = m/np.linalg.norm(m)
#  x_AB = np.zeros((dim,2*len))
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(k[0],k[1],len)
#  print(lam_1)
#  lam_2 = np.linspace(0,k2,len)
  if c==0:
    for i in range(len):
      temp1 = lam_1[i]*m
      x_AB[:,i]= temp1.T
  else:
    A,B = line_icepts(n,c)
    for i in range(len):
      temp1 = A + lam_1[i]*m
      x_AB[:,i]= temp1.T
#    temp2 = B + lam_2[i]*m
#    x_AB[:,i+len]= temp2.T
  return x_AB

#def line_dir_pt(m,A, dim):
#  len = 10
#  dim = A.shape[0]
#  x_AB = np.zeros((dim,len))
#  lam_1 = np.linspace(0,10,len)
#  for i in range(len):
#    temp1 = A + lam_1[i]*m
#    x_AB[:,i]= temp1.T
#  return x_AB


#Generate line points
def line_gen(A,B):
  len =10
  x_AB = np.zeros((2,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB

#Foot of the Altitude
def alt_foot(A,B,C):
  m = B-C
  n = np.matmul(omat,m) 
  N=np.vstack((m,n))
  p = np.zeros(2)
  p[0] = m@A 
  p[1] = n@B
  #Intersection
  P=np.linalg.inv(N.T)@p
  return P

#Intersection of two lines
def line_intersect(n1,c1,n2,c2):
  N=np.vstack((n1,n2))
  p = np.array([c1,c2]) 
  #Intersection
  P=np.linalg.inv(N)@p
#  P=np.linalg.inv(N.T)@p
  return P

  #Radius and centre of the circumcircle
#of triangle ABC
def ccircle(A,B,C):
  p = np.zeros(2)
  n1 = dir_vec(B,A)
  p[0] = 0.5*(np.linalg.norm(A)**2-np.linalg.norm(B)**2)
  n2 = dir_vec(C,B)
  p[1] = 0.5*(np.linalg.norm(B)**2-np.linalg.norm(C)**2)
  #Intersection
  N=np.vstack((n1,n2))
  O=np.linalg.inv(N)@p
  r = np.linalg.norm(A -O)
  return O,r

#Radius and centre of the incircle
#of triangle ABC
def icentre(A,B,C,k1,k2):
  p = np.zeros(2)
  t = norm_vec(B,C)
  n1 = t/np.linalg.norm(t)
  t = norm_vec(C,A)
  n2 = t/np.linalg.norm(t)
  t = norm_vec(A,B)
  n3 = t/np.linalg.norm(t)
  p[0] = n1@B- k1*n2@C
  p[1] = n2@C- k2*n3@A
  N=np.vstack((n1-k1*n2,n2-k2*n3))
  I=np.matmul(np.linalg.inv(N),p)
  r = n1@(I-B)
  #Intersection
  return I,r

def mult_line(A_I,b_z,k,m):
 for i in range(m):
  if i == 0:
    x = line_norm_eq(A_I[i,:],b_z[i],k[i,:])
  elif i == 1:
    y = line_norm_eq(A_I[i,:],b_z[i],k[i,:])
    z = np.vstack((x[None], y[None]))
  else:
    x = line_norm_eq(A_I[i,:],b_z[i],k[i,:])
    z = np.vstack((z,x[None]))
 return z

dvec = np.array([-1,1]) 
#Orthogonal matrix
omat = np.array([[0,1],[-1,0]])
# -*- coding: utf-8 -*-
"""Assignment3.ipynb
Automatically generated by Colaboratory.
Original file is located at
https://colab.research.google.com/drive/1DAAmk3YM2oEi5vpgcG7cBX4yL46ZXrxG#scrollTo=rdVdvCd1gVFF  
"""

#Code by B.ANUSHA
#June 9,2021
import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA
import math as math
import sys                                          #for path to external scripts
sys.path.insert(0, '/storage/emulated/0/tlc/school/ncert/linman/codes/CoordGeo') 

#lambda 
a = np.array([-9/7,0])
m = np.array([0,1])
r = 3
s = np.sqrt(r**2 - (LA.norm(a))**2)/(LA.norm(m))**2
print(s)

#mu 
c = np.array([9/7,0])
m = np.array([0,1])
r = 3
t = np.sqrt(r**2 - (LA.norm(c))**2)/(LA.norm(m))**2
print(t)


#centre and radius of circles
O=np.array([0,0])
r=3



#Input parameters
O = np.array(([0,0]))
P = np.array(([-7,0]))
Q = np.array(([7,0]))
A = np.array(([-(9.0/7.0),3.0*(math.sqrt(40.0)/7.0)]))
B = np.array(([-(9.0/7.0),-3.0*(math.sqrt(40.0)/7.0)]))
C = np.array(([(9.0/7.0),3.0*(math.sqrt(40.0)/7.0)]))
D = np.array(([(9.0/7.0),-3.0*(math.sqrt(40.0)/7.0)]))

m = np.array(([1,(-3.0/math.sqrt(40.0))]))
n = np.array(([1,(3.0/math.sqrt(40.0))]))

k1 = 9
k2 = -9
##Generating all lines
x_PA = line_dir_pt(n,P,k1,k2)
x_PB = line_dir_pt(m,P,k1,k2)
x_QC = line_dir_pt(m,Q,k1,k2)
x_QD = line_dir_pt(n,Q,k1,k2)
x_OP = line_gen(O,P)
x_OQ = line_gen(O,Q)
x_OA = line_gen(O,A)
x_OB = line_gen(O,B)
x_OC = line_gen(O,C)
x_OD = line_gen(O,D)

#Plotting all lines
plt.plot(x_OP[0,:],x_OP[1,:])
plt.plot(x_OQ[0,:],x_OQ[1,:])
plt.plot(x_PA[0,:],x_PA[1,:],label='$PA$')
plt.plot(x_PB[0,:],x_PB[1,:],label='$PB$')
plt.plot(x_QC[0,:],x_QC[1,:],label='$QC$')
plt.plot(x_QD[0,:],x_QD[1,:],label='$QD$')
plt.plot(x_OA[0,:],x_OA[1,:])
plt.plot(x_OB[0,:],x_OB[1,:])
plt.plot(x_OC[0,:],x_OC[1,:])
plt.plot(x_OD[0,:],x_OD[1,:])


plt.plot(O[0], O[1], 'o')
plt.text(-0.9,-0.9,'O',weight = "bold")
plt.plot(P[0], P[1], 'o')
plt.text(-7,0.5,'P',weight = "bold")
plt.plot(Q[0], Q[1], 'o')
plt.text(7,0.5,'Q', weight = "bold")
plt.plot(A[0], A[1], 'o')
plt.text(A[0]*(1.1),A[1]*(1.1),'A', weight = "bold")
plt.plot(B[0], B[1], 'o')
plt.text(B[0]*(1.1),B[1]*(1.1),'B', weight = "bold")
plt.plot(C[0], C[1], 'o')
plt.text(C[0]*(1.1),C[1]*(1.1),'C', weight = "bold")
plt.plot(D[0], D[1], 'o')
plt.text(D[0]*(1.1),D[1]*(1.1),'D', weight = "bold")



#Plotting the circle of radius 3
c1 = 3
theta1 = np.linspace(0,2*np.pi,50)
x1 = c1*np.cos(theta1)
y1 = c1*np.sin(theta1)

plt.plot(x1,y1,label='$circle with (r=3)$')


plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis([-9, 9, -6, 6])
# plt.axis('equal')
plt.show()