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
from quickSortOpenSource import quickSortOpenSource
recursion = 1000000
sys.setrecursionlimit(recursion)    #this function increase the recursion limit.

array1 = arraySetBinaryDigits        #change the variable to switch to different test
array2 = arraySetRevSorted           #comment out to use
array3 = arraySetRandom               #comment out to use
array4 = arraySetFiftyUnsorted          #comment out to use
array5 = arraySetTenUnSorted            #comment out to use
array6 = arraySorted

###testArray = copy.deepcopy(array2)
###testArrayCopy = copy.deepcopy(testArray)

arrayTest= [array1,array2 ,array3 ,array4,array5 ,array6]
#arrayTest= [array1,array3,array6]
arrayTestCopy = copy.deepcopy(arrayTest)

recursion = 1000000
sys.setrecursionlimit(recursion)

def comp(list1, list2):
    for val in list1:
        if val in list2:
            return True
    return False


"""
for i in range (0,len_each_array):
    print i,
    testArray[i].sort()
    print len(testArray[i]),
    quickSortHoare(testArrayCopy[i])
    print len(testArrayCopy[i])
"""

len_array_test = len(arrayTest)

for i in range(0,len_array_test):
    for j in range(0,5):
        print i,j, len(arrayTest[i][j]),
        arrayTest[i][j].sort()
        #arrayTestCopy[i][j] = quickSort(arrayTestCopy[i][j])
        #quickSortOpenSource(arrayTestCopy[i][j])
        #mergeSort(arrayTestCopy[i][j])
        heapSort(arrayTestCopy[i][j])
        if comp(arrayTestCopy[i][j],arrayTestCopy[i][j]) == True:
            print "PASS"
        else:
            print "FAIL"

