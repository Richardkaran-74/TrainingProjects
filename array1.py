from array import *

arr=array('i',[20,27,74,47])

for i in  range(len(arr)):
    for j in range(i+1,len(arr)):
        if (arr[i]<arr[j]):
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
print(arr)