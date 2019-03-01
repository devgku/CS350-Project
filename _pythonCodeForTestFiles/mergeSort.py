import time


#pick a file from the directory to work with
file = open("thousandInts.txt", "r")
if file.mode == 'r':
    contents = file.read()

#fills array object with file data
array = contents.split()
#can use this library function to confirm the sort, if desired
#a0 = sorted(map(int, array))
#print(a0)



def mergeSort(array):
    #print("Splitting ",array)
    if len(array)>1:
        mid = len(array)//2
        lefthalf = array[:mid]
        righthalf = array[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                array[k]=lefthalf[i]
                i = i + 1
            else:
                array[k]=righthalf[j]
                j = j + 1
            k=k+1

        while i < len(lefthalf):
            array[k]=lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            array[k]=righthalf[j]
            j = j + 1
            k = k + 1
    #print("Merging ",array)

start = time.time()
mergeSort(array)
end = time.time()
print("time elapsed: " + str(float(end - start)))

print("mergesort of list")
print(array)



