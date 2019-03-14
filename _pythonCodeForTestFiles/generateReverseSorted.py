import random
import time

def makeArray(n):
    array = []
    for i in range(n,0,-1):
        array.append(i)
    return array


arrayReversed10 = makeArray(10)
arrayReversed50 = makeArray(50)
arrayReversed100 = makeArray(100)
arrayReversed1000 = makeArray(1000)
arrayReversed10000 = makeArray(10000)
arrayReversed100000 = makeArray(100000)
arrayReversed200000 = makeArray(200000)
arrayReversed400000 = makeArray(400000)
arrayReversed600000 = makeArray(600000)
arrayReversed800000 = makeArray(800000)
arrayReversed1000000 = makeArray(1000000)

arraySetRevSorted = [arrayReversed10,arrayReversed50,arrayReversed100,arrayReversed1000,arrayReversed10000,arrayReversed100000, arrayReversed200000, arrayReversed400000, arrayReversed600000, arrayReversed800000, arrayReversed1000000]

"""
#reverse sorted order data set.

contents = []
#pick a file to work with
file = open("special.txt", "r")
if file.mode == 'r':
   contents = file.read()
file.close()

n = 0
def revNums(n, contents):  
    arr = list(map(int, contents.split()))
    arr.sort(reverse = True)   
    for i in range(n):      
       file.write("%d\n" % (arr[i]))


file = open("__rev_special.txt", "w+")
revNums(50, contents)                
file.close()



# add name to file. Will generate n integers separated by \n 

#pick a file to work with
file = open("_a1_10Ints.txt", "r")
if file.mode == 'r':
   contents = file.read()
file.close()

#creates a file to 
file = open("__10_revReversed_Ints.txt", "w+")
revNums(10, contents)                
file.close()



file = open("_a1_100Ints.txt", "r")
if file.mode == 'r':
   contents = file.read()
file.close()


#pick a file to work with
file = open("__100_revReversed_Ints.txt", "w+")
revNums(100, contents)                
file.close()


file = open("_a1_1000Ints.txt", "r")
if file.mode == 'r':
   contents = file.read()
file.close()


file = open("__1000_revReversed_Ints.txt", "w+")
revNums(1000, contents)                
file.close()


#pick a file to work with
file = open("_a1_10000Ints.txt", "r")
if file.mode == 'r':
   contents = file.read()
file.close()

file = open("__10000_revReversed_Ints.txt", "w+")
revNums(10000, contents)                
file.close()


#pick a file to work with
file = open("_a1_100000Ints.txt", "r")
if file.mode == 'r':
   contents = file.read()
file.close()

file = open("__100000_revReversed_Ints.txt", "w+")
revNums(100000, contents)
file.close()

#pick a file to work with
file = open("_a1_200000Ints.txt", "r")
if file.mode == 'r':
    contents = file.read()
file.close()

file = open("__200000_revReversed_Ints.txt", "w+")
revNums(200000, contents)
file.close()

#pick a file to work with
file = open("_a1_400000Ints.txt", "r")
if file.mode == 'r':
    contents = file.read()
file.close()

file = open("__400000_revReversed_Ints.txt", "w+")
revNums(400000, contents)
file.close()

#pick a file to work with
file = open("_a1_600000Ints.txt", "r")
if file.mode == 'r':
    contents = file.read()
file.close()

file = open("__600000_revReversed_Ints.txt", "w+")
revNums(600000, contents)
file.close()

#pick a file to work with
file = open("_a1_800000Ints.txt", "r")
if file.mode == 'r':
    contents = file.read()
file.close()

file = open("__800000_revReversed_Ints.txt", "w+")
revNums(800000, contents)
file.close()

#pick a file to work with
file = open("_a1_1000000Ints.txt", "r")
if file.mode == 'r':
   contents = file.read()
file.close()


file = open("__1000000_revReversed_Ints.txt", "w+")
revNums(1000000, contents)
file.close()
"""
