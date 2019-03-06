# this code creates Hoare Partition written in Levitin's Book
# the partition will be used in quicksort later.

def hoarePartition(arr,l,r):
    # Partitions a subarray by Hoare' s algorithm, using the first element as a pivot
    # Input: Subarray of array arr[0 .. n-1],defined by its left and right
    # indices l and r (l < r)
    # Output: Partition of A[l..r], with the split position returned as this function's value
    pivot = arr[l]
    i,j = l-1, r+1
    while True:
        while True:
            j -= 1
            if arr[j] <= pivot:
                break
        while True:
            i += 1
            if arr[i] >= pivot:
                break
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            return j

def quickSort(arr, l, r):
    # Sorts a subarray by quicksort
    # Input: Subarray of array arr[0 .. n -1] defined by its left and right
    # indices l and r
    # Output: Subarray arr[l..r] sorted in nondecreasing order
    if l < r:
        s = hoarePartition(arr,l,r)
        #quickSort(arr,l,s-1)          # this code is same with the book but it does not work
        quickSort(arr,l,s)                # fixed code, can you explain what is different
        quickSort(arr,s+1,r)

    # Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr,0,n-1)
print ("Sorted array is:")
for i in range(n):
    print ("%d" %arr[i]),