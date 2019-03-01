#This program creates text files to test the sort programs
#from 10^0 to 10^6 digit integers. 
import random

n = 0
def randNums(n):    
    for i in range(n):      
       file.write("%d\n" % (random.randint(1,100000)))

# add name to file. Will generate n integers separated by \n 
file = open("_a1_10Ints.txt", "w+")
randNums(10)                
file.close()

file = open("_a1_100Ints.txt", "w+")
randNums(100)                
file.close()

file = open("_a1_1000Ints.txt", "w+")
randNums(1000)                
file.close()

file = open("_a1_10000Ints.txt", "w+")
randNums(10000)                
file.close()

file = open("_a1_100000Ints.txt", "w+")
randNums(100000)                
file.close()

file = open("_a1_1000000Ints.txt", "w+")
randNums(1000000)                
file.close()

file = open("special.txt", "w+")
randNums(50)                
file.close()
