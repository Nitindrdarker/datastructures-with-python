import numpy

def merge(a, left, leftcount, right, rightcount):
    i = 0
    j = 0
    k = 0
    while(i<leftcount and j<rightcount):
        if(left[i]<right[j]):
            a[k] = left[i]
            k += 1
            i += 1
        else:
            a[k] = right[j]
            k += 1
            j += 1
    while(i<leftcount):
        a[k] = left[i]
        k += 1
        i += 1
    while(j<rightcount):
        a[k] = right[j]
        k += 1
        j += 1

def mergeSort(a):
    l = len(a)
    mid = l//2
    if(l<2):
        return
    else:
        left = numpy.zeros(mid)
        right = numpy.zeros(l-mid) 
        for i in range(mid):
            left[i] = a[i] 
        for i in range(mid,l):
            right[i-mid] = a[i]
        mergeSort(left)
        mergeSort(right)
        merge(a,left,mid,right,l-mid)

l = int(input())
a = numpy.zeros(l,dtype='int')

for i in range(l):
    v = int(input())
    a[i] = v
    
print(a)
mergeSort(a)
print(a)