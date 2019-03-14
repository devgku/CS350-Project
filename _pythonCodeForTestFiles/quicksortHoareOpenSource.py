from random import randint
def quicksort(array, low, high):
    if low < high:
        p = partition(array, low, high)
        quicksort(array, low, p)
        quicksort(array, p + 1, high)

def partition(array, low, high):
    pivot = array[low]
    i=low-1
    j=high+1
    while 1:
        i = i + 1
        while array[i] < pivot:
            i = i + 1
    j=j-1
    while array[j] > pivot:
        j=j-1

    if i >= j:
        return j
    array[i],array[j]=array[j],array[i]




array=[]
for p in range(10):
    array.append(randint(1,100))

quicksort(array,0,len(array)-1)
print array