import time
import random
import matplotlib.pyplot as plt
import numpy as np

n=[3,4,5,6,9]
timesIter=[]
timesRecur=[]

st=time.time()
sum=0
#iterative method
for k in n:
  for i in range(1,k+1):
    sum=sum+i
  et=time.time()
  elapsed=et-st
  timesIter.append(elapsed)


#recursive method
sum=0
def sumofn(n):
  if(n <= 1):
    return n
  return n+sumofn(n-1)

for k in n:
  st=time.time()
  sumofn(k)
  et=time.time()
  elapsed=et-st
  timesRecur.append(elapsed)

plt.bar(n,timesIter)
plt.show()
plt.bar(n,timesRecur)
plt.show()

A=np.random.randint(1000,size=(10000))
key=int(input("enter the number you want to search"))
times=[]
algo=['linear','binary']

st=time.time()#linear
for i in range(0,len(A)):
  if(i == key):
    print("element found")
    break
et=time.time()
elapsed=et-st
times.append(elapsed)

n=len(A)
l=A[0]
r=A[n-1]
mid=0
while(l <= r):  #binary
  mid= l + (r-1) // 2
  if (A[mid]== key):
    print("element found")
  elif mid < key:
    l = mid + 1
  else:
    r = mid - 1

def stringToInt(str):

    if (len(str) == 1):
        return ord(str[0]) - ord('0')

    y = stringToInt(str[1:])

    x = ord(str[0]) - ord('0')

    x = x * (10**(len(str) - 1)) + y
    return x
 
 
str = "1235"
print(stringToInt(str))

def reverse_string(s):
    if len(s) == 0:
        return s
    return reverse_string(s[1:]) + s[0]

def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] == s[-1]:
        return is_palindrome(s[1:-1])
    return False


string_input = input("Enter a string of digits: ")
print("Converted integer:", string_to_int(string_input))

string_input = input("Enter a string to reverse: ")
print("Reversed string:", reverse_string(string_input))

string_input = input("Enter a string to check for palindrome: ")
if is_palindrome(string_input):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
