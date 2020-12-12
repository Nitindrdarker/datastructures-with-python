import numpy

def pivot(a,start,end):
    p = a[end]
    
    pindex = start
    for i in range(start,end):
        if(p>=a[i]):
            a[pindex],a[i] = a[i],a[pindex]
            pindex += 1
    a[pindex],a[end] = a[end],a[pindex]
        
    return pindex





def quickSort(a,start,end):
    if(start<end):
        p = pivot(a,start,end)
        quickSort(a,start,p-1)
        quickSort(a,p+1,end)
    

l = int(input())
a = numpy.zeros(l,dtype='int')

for i in range(l):
    v = int(input())
    a[i] = v
    
print(a)
quickSort(a,0,4)
print(a)