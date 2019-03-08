import random
import time


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
file = open("_a1_1000Ints.txt", "r")
if file.mode == 'r':
   contents = file.read()
file.close()

#creates a file to 
file = open("__1000_revSorted_Ints.txt", "w+")
revNums(1000, contents)                
file.close()



file = open("_a1_10000Ints.txt", "r")
if file.mode == 'r':
   contents = file.read()
file.close()


#pick a file to work with
file = open("__10000_revSorted_Ints.txt", "w+")
revNums(10000, contents)                
file.close()


file = open("_a1_100000Ints.txt", "r")
if file.mode == 'r':
   contents = file.read()
file.close()


file = open("__100000_revSorted_Ints.txt", "w+")
revNums(100000, contents)                
file.close()


#pick a file to work with
file = open("_a1_1000000Ints.txt", "r")
if file.mode == 'r':
   contents = file.read()
file.close()

file = open("__1000000_revSorted_Ints.txt", "w+")
revNums(1000000, contents)                
file.close()


#pick a file to work with
file = open("_a1_5000000Ints.txt", "r")
if file.mode == 'r':
   contents = file.read()
file.close()


file = open("__5000000_revSorted_Ints.txt", "w+")
revNums(5000000, contents)                
file.close()


#pick a file to work with
file = open("_a1_10000000Ints.txt", "r")
if file.mode == 'r':
   contents = file.read()
file.close()


file = open("__10000000_revSorted_Ints.txt", "w+")
revNums(10000000, contents)
file.close()
