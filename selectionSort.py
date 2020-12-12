import numpy

def selectionSort(arr):
    l = len(arr)
    for i in range(l):
        count = i
        for j in range(i+1,l):
            if(arr[count]>arr[j]):
                count = j
        arr[i],arr[count]= arr[count],arr[i]

    print(arr)

                

l = int(input())
a = numpy.zeros(l,dtype='int')

for i in range(l):
    v = int(input())
    a[i] = v
    
print(a)
selectionSort(a)