array=[8,7,2,5,3,5]
target=10
n=len(array)

found=0
for i in range(0,n):
  for j in range(0,len(array)-1):
    if((array[i]+array[j]) == target and i!=j):
      print("pair found (",array[i],",",array[j],")")
      found += 1
    else:
      continue
if(found==0):
  print("no pair found")


arr=[1,7,4,2,8,6,3,9,5]

temp=0
for i in range(0,len(arr)):
  for j in range(0,len(arr)-1):
    if(arr[j]>arr[j+1]):
      temp=arr[j+1]
      arr[j+1]=arr[j]
      arr[j]=temp

print(arr)
print("product of 2 highest numbers are:", arr[len(arr)-1]*arr[len(arr)-2])



inputarray=[0,1,0,1,0,0,1,1,1,0]
outputarray=[]
for i in range(0,2):
  for j in range(0,len(inputarray)):
    if(inputarray[j]==inputarray[i]):


arr=[8,4,1,6]
k=10
n=len(arr)

for i in range(0,n):
  for j in range(0,len(arr)-1):
    if((arr[i]+arr[j]) == k and i!=j):
      print("pair found (",arr[i],",",arr[j],")")
    else:
      continue
      outputarray.append(inputarray[j])
print(outputarray)
