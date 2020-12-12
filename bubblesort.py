import numpy
def bubbleSort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1] = arr[j+1],arr[j]
            
    print(arr)
l = int(input())
a = numpy.zeros(l,dtype='int')

for i in range(l):
    v = int(input())
    a[i] = v
    
print(a)
bubbleSort(a)

    
    



