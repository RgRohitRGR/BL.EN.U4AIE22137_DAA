import random
import time
import matplotlib.pyplot as plt
import numpy as np

st=time.time()
A=np.random.randint(10000,size=(1000))
times=[]
algo=[]

temp=0

#bubble sort
n=len(A)
swapped=True
while(swapped):
  swapped=False
  for j in range(0,n-1):
    if(A[j] > A[j+1]):
      temp=A[j]
      A[j]=A[j+1]
      A[j+1]=temp
      swapped=True
  n=n-1
et=time.time()
elapsedtime=et-st

algo.append('bubble')
times.append(elapsedtime)

A=np.random.randint(10000,size=(1000))
st=time.time()
smallest=0
n=len(A)

#selection sort
for j in range(0,n-1):
  smallest=j
  for i in range(j+1,n):
    if(A[i] < A[smallest]):
      smallest=i
  temp=A[j]
  A[j]=A[smallest]
  A[smallest]=temp

et=time.time()
elapsedtime=et-st
algo.append('selection')
times.append(elapsedtime)

#insertion sort
A=np.random.randint(10000,size=(1000))
st=time.time()
i=0
for j in range(1,n):
  key=A[j]
  i=j-1
  while(i>=0 and A[i] > key):
    A[i+1] = A[i]
    i=i-1
  A[i+1]=key
et=time.time()
elapsedtime=et-st
algo.append('insertion')
times.append(elapsedtime)

print(algo,times)
plt.bar(algo,times)
plt.show()
