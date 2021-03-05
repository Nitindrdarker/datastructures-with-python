def heapify(arr, n, i):
    left = (i * 2) + 1
    right = (i * 2) + 2
    smallest = i
    if(left < n and arr[smallest] > arr[left]):
        smallest = left
    if(right < n and arr[smallest] > arr[right]):
        smallest = right
    if smallest != i:
        arr[smallest], arr[i] = arr[i], arr[smallest]
        heapify(arr, n, smallest)
    else:
        return
def heapsort(arr, n):
    heapify(arr, n, 0)
    for i in range(n-1, -1, -1):
        arr[i], arr[0] = arr[0], arr[i] 
        heapify(arr, i, 0)
def print_heap(arr):
    for i in arr:
        print(i)



arr = [1, 2, 3, 4, 5]
heapify(arr, len(arr), 0)

heapsort(arr, len(arr))

print_heap(arr)

        


