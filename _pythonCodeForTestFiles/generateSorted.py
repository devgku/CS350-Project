import random
import time
import math

def makeArray(n,percentSorted):
    arraySorted = []
    arrayUnsorted = []
    sortedIndex = int(math.ceil(n * percentSorted))
    for i in range(0,sortedIndex):
        arraySorted.append(i)
    for j in range(sortedIndex,n):
            arrayUnsorted.append(random.randint(sortedIndex,n))
    return arraySorted + arrayUnsorted


percentSorted = 1
arraySorted10 = makeArray(10,percentSorted)
arraySorted50 = makeArray(50,percentSorted)
arraySorted100 = makeArray(100,percentSorted)
arraySorted1000 = makeArray(1000,percentSorted)
arraySorted10000 = makeArray(10000,percentSorted)
arraySorted100000 = makeArray(100000,percentSorted)
arraySorted200000 = makeArray(200000,percentSorted)
arraySorted400000 = makeArray(400000,percentSorted)
arraySorted600000 = makeArray(600000,percentSorted)
arraySorted800000 = makeArray(800000,percentSorted)
arraySorted1000000 = makeArray(1000000,percentSorted)

percentSorted = 0.9
arrayNearlySorted10 = makeArray(10,percentSorted)
arrayNearlyrted50 = makeArray(50,percentSorted)
arrayNearlySorted100 = makeArray(100,percentSorted)
arrayNearlySorted1000 = makeArray(1000,percentSorted)
arrayNearlySorted10000 = makeArray(10000,percentSorted)
arrayNearlySorted100000 = makeArray(100000,percentSorted)
arrayNearlySorted200000 = makeArray(200000,percentSorted)
arrayNearlySorted400000 = makeArray(400000,percentSorted)
arrayNearlySorted600000 = makeArray(600000,percentSorted)
arrayNearlySorted800000 = makeArray(800000,percentSorted)
arrayNearlySorted1000000 = makeArray(1000000,percentSorted)

percentSorted = 0.5
arrayHalfSorted10 = makeArray(10,percentSorted)
arrayHalfSorted50 = makeArray(50,percentSorted)
arrayHalfSorted100 = makeArray(100,percentSorted)
arrayHalfSorted1000 = makeArray(1000,percentSorted)
arrayHalfSorted10000 = makeArray(10000,percentSorted)
arrayHalfSorted100000 = makeArray(100000,percentSorted)
arrayHalfSorted200000 = makeArray(200000,percentSorted)
arrayHalfSorted400000 = makeArray(400000,percentSorted)
arrayHalfSorted600000 = makeArray(600000,percentSorted)
arrayHalfSorted800000 = makeArray(800000,percentSorted)
arrayHalfSorted1000000 = makeArray(1000000,percentSorted)

"""
#reverse sorted order data set.
#pick a file to work with
file = open("special.txt", "r")
if file.mode == 'r':
   contents = file.read()
file.close()

n = 0
def tenPctUnsorted(n, contents):  
    #lower bounds
    nLower = int(.25 * n)
    #upper bounds
    nUpper = int(.75 * n)
    # ***if you want to check what the bounds are for i, show next 2 lines 
    #print ("lower bound is " + str(nL))
    #print ("upper bound is " + str(nU))

    arr = list(map(int, contents.split()))
    arr.sort()   
    for i in range(n):   
        if (i > nLower) and (i < nUpper + 1):
            file.write("%d\n" % (random.randint(1,100)))
        else: 
            file.write("%d\n" % (arr[i]))

file = open("_fiftyPctUnsorted_special.txt", "w+")
tenPctUnsorted(50, contents)                
file.close()




# add name to file. Will generate n integers separated by \n 

#pick a file to work with
file = open("_a1_10Ints.txt", "r")
if file.mode == 'r':
   contents = file.read()
file.close()

#creates a file to 
file = open("_fiftyPctUnsorted_10Ints.txt", "w+")
tenPctUnsorted(10, contents)                
file.close()



file = open("_a1_100Ints.txt", "r")
if file.mode == 'r':
   contents = file.read()
file.close()


#pick a file to work with
file = open("_fiftyPctUnsorted_100Ints.txt", "w+")
tenPctUnsorted(100, contents)                
file.close()


file = open("_a1_1000Ints.txt", "r")
if file.mode == 'r':
   contents = file.read()
file.close()


file = open("_fiftyPctUnsorted_1000Ints.txt", "w+")
tenPctUnsorted(1000, contents)                
file.close()


#pick a file to work with
file = open("_a1_10000Ints.txt", "r")
if file.mode == 'r':
   contents = file.read()
file.close()

file = open("_fiftyPctUnsorted_10000Ints.txt", "w+")
tenPctUnsorted(10000, contents)                
file.close()


#pick a file to work with
file = open("_a1_100000Ints.txt", "r")
if file.mode == 'r':
   contents = file.read()
file.close()


file = open("_fiftyPctUnsorted_100000Ints.txt", "w+")
tenPctUnsorted(100000, contents)
file.close()

#pick a file to work with
file = open("_a1_200000Ints.txt", "r")
if file.mode == 'r':
    contents = file.read()
file.close()


file = open("_fiftyPctUnsorted_200000Ints.txt", "w+")
tenPctUnsorted(200000, contents)
file.close()

#pick a file to work with
file = open("_a1_400000Ints.txt", "r")
if file.mode == 'r':
    contents = file.read()
file.close()


file = open("_fiftyPctUnsorted_400000Ints.txt", "w+")
tenPctUnsorted(400000, contents)
file.close()

#pick a file to work with
file = open("_a1_600000Ints.txt", "r")
if file.mode == 'r':
    contents = file.read()
file.close()


file = open("_fiftyPctUnsorted_600000Ints.txt", "w+")
tenPctUnsorted(600000, contents)
file.close()

#pick a file to work with
file = open("_a1_800000Ints.txt", "r")
if file.mode == 'r':
    contents = file.read()
file.close()


file = open("_fiftyPctUnsorted_800000Ints.txt", "w+")
tenPctUnsorted(800000, contents)
file.close()

#pick a file to work with
file = open("_a1_1000000Ints.txt", "r")
if file.mode == 'r':
   contents = file.read()
file.close()


file = open("_fiftyPctUnsorted_1000000Ints.txt", "w+")
tenPctUnsorted(1000000, contents)
file.close()"""