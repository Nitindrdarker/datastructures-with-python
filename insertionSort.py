import numpy

def insertionSort(arr):
    l = len(arr)
    for i in range(1, l):
        current = arr[i]
        j = i-1
        while(j>=0 and arr[j]>current):
            
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] =  current
    print(arr)

  
l = int(input())
a = numpy.zeros(l,dtype='int')

for i in range(l):
    v = int(input())
    a[i] = v
    
print(a)
insertionSort(a)