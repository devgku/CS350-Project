#This program creates text files to test the sort programs
#from 10^1 to 10^6  five digit integers. 
import random

n = 0
def randNums(n):    
    for i in range(n):      
       file.write("%d\n" % (random.randint(10000,99999)))


# add name to file. Will generate n integers separated by \n 
file = open("tenInts.txt", "w+")
randNums(10)                
file.close()

file = open("hundredInts.txt", "w+")
randNums(100)                
file.close()

file = open("thousandInts.txt", "w+")
randNums(1000)                
file.close()

file = open("tenThousandInts.txt", "w+")
randNums(10000)                
file.close()

file = open("hundredThousandInts.txt", "w+")
randNums(100000)                
file.close()

file = open("millionInts.txt", "w+")
randNums(1000000)                
file.close()

