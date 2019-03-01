import time

#pick a file to work with
file = open("tenThousandInts.txt", "r")
if file.mode == 'r':
    contents = file.read()

#fills array variable with file data
array = contents.split()
#can use this library function to confirm the sort, if desired
#a0 = sorted(map(int, array))
#print(a0)


# Implementation of heap Sort from CLRM book Ch.6   
# To heapSort subtree rooted at index i. 
# n is size of heap 

def maxHeapify(array, n, i): 
    largest = i # Initialize largest as root 
    l = (2*i) + 1     # left = 2*i + 1 
    r = (2 * i) + 2     # right = 2*i + 2 
  
    # See if left child of root exists and is 
    # greater than root 
    if l < n and array[i] < array[l]: 
        largest = l 
  
    # See if right child of root exists and is 
    # greater than root 
    if r < n and array[largest] < array[r]: 
        largest = r 
  
    # Change root, if needed 
    if largest != i: 
        array[i],array[largest] = array[largest],array[i] # swap 
  
        # Heapify the root. 
        maxHeapify(array, n, largest) 
  
# The main function to sort an array of given size 
def heapSort(arr): 
    n = len(arr) 
  
    # Build a maxheap. 
    for i in range(n, -1, -1): 
        maxHeapify(arr, n, i) 
  
    # One by one extract elements 
    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i] # swap 
        maxHeapify(arr, i, 0) 
  

# Driver code to test above 
start2 = time.time()
heapSort(array)
end2 = time.time()
print("time elapsed: " + str(float(end2 - start2)))

print("heapSort of list")
print(array)
