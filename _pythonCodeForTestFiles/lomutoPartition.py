#This code creates Lomuto Partition written in Levitin's book.


def lomutoPartition(arr,l,r):
    # Partitions subarray by Lomuto algorithm using first element as pivot
    # Input: An subarray arr[l..r] of arr[0..n-1], defined by its left and right
    #  indices l and r (l <= r)
    # Output: Partition of arr[l..r] and the new position of the pivot
    pivot = arr[l]	 # pivot is the first element
    s = l
    for i in range(l + 1, r):
        if arr[i] < pivot:
            s = s+1
            #print s, i
            #print arr[s],arr[i]
            arr[s],arr[i] = arr[i],arr[s]       #swap arr[s],arr[i]
            #print arr[s],arr[i]

    arr[l],arr[r] = arr[r],arr[l]               #swap arr[l],arr[r]
    return s


def quickSortLomutoWrapper(arr, l, r):
    # Sorts a subarray by quicksort
    # Input: Subarray of array arr[0 .. n -1] defined by its left and right
    # indices l and r
    # Output: Subarray arr[l..r] sorted in nondecreasing order
    if l < r:
        s = lomutoPartition(arr,l,r)
        # quickSort(arr,l,s-1)          # this code is same with the book but it does not work
        quickSortLomutoWrapper(arr,l,s)                # fixed code, can you explain what is different
        quickSortLomutoWrapper(arr,s+1,r)


def quickSortLomuto(arr):
    n = len(arr)
    quickSortLomutoWrapper(arr,0,n-1)