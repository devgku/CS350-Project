import random
import time


#reverse sorted order data set.
#pick a file to work with
file = open("special.txt", "r")
if file.mode == 'r':
   contents = file.read()
file.close()

n = 0
def tenPctUnsorted(n, contents):  
    #lower bounds
    nLower = int(.45 * n)
    #upper bounds
    nUpper = int(.55 * n)
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

file = open("_tenPctUnsorted_special.txt", "w+")
tenPctUnsorted(50, contents)                
file.close()




# add name to file. Will generate n integers separated by \n 

#pick a file to work with
file = open("_a1_10Ints.txt", "r")
if file.mode == 'r':
   contents = file.read()
file.close()

#creates a file to 
file = open("_tenPctUnsorted_10Ints.txt", "w+")
tenPctUnsorted(10, contents)                
file.close()



file = open("_a1_100Ints.txt", "r")
if file.mode == 'r':
   contents = file.read()
file.close()


#pick a file to work with
file = open("_tenPctUnsorted_100Ints.txt", "w+")
tenPctUnsorted(100, contents)                
file.close()


file = open("_a1_1000Ints.txt", "r")
if file.mode == 'r':
   contents = file.read()
file.close()


file = open("_tenPctUnsorted_1000Ints.txt", "w+")
tenPctUnsorted(1000, contents)                
file.close()


#pick a file to work with
file = open("_a1_10000Ints.txt", "r")
if file.mode == 'r':
   contents = file.read()
file.close()

file = open("_tenPctUnsorted_10000Ints.txt", "w+")
tenPctUnsorted(10000, contents)                
file.close()


#pick a file to work with
file = open("_a1_100000Ints.txt", "r")
if file.mode == 'r':
   contents = file.read()
file.close()


file = open("_tenPctUnsorted_100000Ints.txt", "w+")
tenPctUnsorted(100000, contents)                
file.close()


#pick a file to work with
file = open("_a1_1000000Ints.txt", "r")
if file.mode == 'r':
   contents = file.read()
file.close()


file = open("_tenPctUnsorted_1000000Ints.txt", "w+")
tenPctUnsorted(1000000, contents)
file.close()
