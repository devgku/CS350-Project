# This file measure the time of sorting experimental data using the different sorting algorithms

from generateBinary import arraySetBinaryDigits
from generateRandom import arraySetRandom
from generateReverseSorted import arraySetRevSorted
from generateSorted import arraySetFiftyUnsorted
from generateSorted import arraySetTenUnSorted
from generateSorted import arraySorted
import time
import sys
import copy

from heapSort import heapSort
from mergeSort import mergeSort
from hoarePartition import quickSortHoare
from lomutoPartition import quickSortLomuto
from quickSortOpenSource2 import quickSort

recursion = 1000000
sys.setrecursionlimit(recursion)    #this function increase the recursion limit.

array = arraySetBinaryDigits        #change the variable to switch to different test
#array = arraySetRevSorted           #comment out to use
#array = arraySetRandom               #comment out to use
#array = arraySetFiftyUnsorted          #comment out to use
#array = arraySetTenUnSorted            #comment out to use
#array = arraySorted

array1 = copy.deepcopy(array)
array2 = copy.deepcopy(array)
array3 = copy.deepcopy(array)
array4 = copy.deepcopy(array)
array5 = copy.deepcopy(array)
array6 = copy.deepcopy(array)
array7 = copy.deepcopy(array)
array8 = copy.deepcopy(array)
array9 = copy.deepcopy(array)

array_set = [array,array1,array2,array3,array4,array5,array6,array7,array8,array9]
array_set1 = copy.deepcopy(array_set)
array_set2 = copy.deepcopy(array_set)
array_set3 = copy.deepcopy(array_set)
sys.setrecursionlimit(1000000)

number_of_element = len(array_set)
number_of_array = len(array)        #set the range of the array
"""
print array[5]
array[5] = quickSort(array[5])
#quickSortLomuto(array[3])
#quickSortHoare(array[3])
#mergeSort(array[11])
#heapSort(array[3])
print ("Sorted array is:")
print (array[5])
#print sortedArray

"""
for j in range(0,number_of_element):
    for i in range (0, number_of_array):
        #now = datetime.datetime.now()           #print the time and date for the record
        #print now
        start = time.time()
        #sorted(array[i])
        #mergeSort(array[i])
        quickSortHoare(array_set[j][i])
        #quickSortLomuto(array_set[j][i])
        #quickSortOpenSource(array[i])
        #heapSort(array[i])
        #array[i] = quickSort(array[i])
        end = time.time()
        print (end-start)
    print "END"
print "----------------------------------"


for j in range(0,number_of_element):
    for i in range (0, number_of_array):
        #now = datetime.datetime.now()           #print the time and date for the record
        #print now
        start = time.time()
        #sorted(array[i])
        mergeSort(array_set1[j][i])
        #quickSortHoare(array_set[j][i])
        #quickSortLomuto(array[i])
        #quickSortOpenSource(array[i])
        #heapSort(array[i])
        #array[i] = quickSort(array[i])
        end = time.time()
        print (end-start)
    print "END"
print "----------------------------------"

for j in range(0,number_of_element):
    for i in range (0, number_of_array):
        #now = datetime.datetime.now()           #print the time and date for the record
        #print now
        start = time.time()
        #sorted(array[i])
        #mergeSort(array_set1[j][i])
        #quickSortHoare(array_set[j][i])
        #quickSortLomuto(array[i])
        #quickSortOpenSource(array[i])
        heapSort(array_set2[j][i])
        #array[i] = quickSort(array[i])
        end = time.time()
        print (end-start)
    print "END"
print "----------------------------------"

for j in range(0,number_of_element):
    for i in range (0, number_of_array):
        #now = datetime.datetime.now()           #print the time and date for the record
        #print now
        start = time.time()
        #sorted(array[i])
        #mergeSort(array_set1[j][i])
        #quickSortHoare(array_set[j][i])
        #quickSortLomuto(array[i])
        #quickSortOpenSource(array[i])
        #heapSort(array_set2[j][i])
        array_set3[j][i] = quickSort(array_set3[j][i])
        end = time.time()
        print len(array_set3[j][i])
        print (end-start)
    print "END"
print "----------------------------------"