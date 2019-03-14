#This program creates text files to test the sort programs
#from 10^0 to 10^6 biniary digits. 
import random

n = 0
def randNums(n):
    array = []
    for i in range(n):
        array.append(random.randint(0,1))
    return array

binaryArray10 = randNums(10)
binaryArray50 = randNums(50)
binaryArray100 = randNums(100)
binaryArray1000 = randNums(1000)
binaryArray10000 = randNums(10000)
binaryArray100000 = randNums(100000)
binaryArray200000 = randNums(200000)
binaryArray400000 = randNums(400000)
binaryArray600000 = randNums(600000)
binaryArray800000 = randNums(800000)
binaryArray1000000 = randNums(1000000)

arraySetBinaryDigits = [binaryArray10,binaryArray50,binaryArray100,binaryArray1000,binaryArray10000,binaryArray100000, binaryArray200000, binaryArray400000, binaryArray600000, binaryArray800000, binaryArray1000000]

# add name to file. Will generate n integers separated by \n
"""
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
"""