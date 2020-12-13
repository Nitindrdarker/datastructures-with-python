import numpy


def binarySearch(a,start,end,number):
    
    try:
    
        mid = (start+end)//2
        if(a[mid] == number):
            return number
        elif(a[mid]>number):
            return binarySearch(a,0,mid-1,number)
        elif(a[mid]<number):
            return binarySearch(a,mid+1,end,number)
        

    except: 
        print('not found')
        return -1


a = numpy.array([1,2,3,4,5,6])


number = int(input())

if  (binarySearch(a,0,5,number)>0):
    print('found')



    