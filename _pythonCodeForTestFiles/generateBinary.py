#This program creates text files to test the sort programs
#from 10^0 to 10^6 biniary digits. 
import random

n = 0
def randNums(n):    
    for i in range(n):      
       file.write("%d\n" % (random.randint(0,1)))

# add name to file. Will generate n integers separated by \n 
file = open("_10_binaryDigits.txt", "w+")
randNums(10)                
file.close()

file = open("_50_binaryDigits.txt", "w+")
randNums(50)
file.close()

file = open("_100_binaryDigits.txt", "w+")
randNums(100)                
file.close()

file = open("_1000_binaryDigits.txt", "w+")
randNums(1000)                
file.close()

file = open("_10000_binaryDigits.txt", "w+")
randNums(10000)                
file.close()

file = open("_100000_binaryDigits.txt", "w+")
randNums(100000)                
file.close()

file = open("_200000_binaryDigits.txt", "w+")
randNums(200000)
file.close()

file = open("_400000_binaryDigits.txt", "w+")
randNums(400000)
file.close()

file = open("_600000_binaryDigits.txt", "w+")
randNums(600000)
file.close()

file = open("_800000_binaryDigits.txt", "w+")
randNums(800000)
file.close()

file = open("_1000000_binaryDigits.txt", "w+")
randNums(1000000)                
file.close()


