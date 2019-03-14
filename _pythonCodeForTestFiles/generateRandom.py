#This program creates text files to test the sort programs
#from 10^0 to 10^6 digit integers. 
import random

def randNums(n):
    array = []
    for i in range(n):
        array.append(random.randint(1,100000))
    return array

randomArray10 = randNums(10)
randomArray50 = randNums(50)
randomArray100 = randNums(100)
randomArray1000 = randNums(1000)
randomArray10000 = randNums(10000)
randomArray100000 = randNums(100000)
randomArray200000 = randNums(200000)
randomArray400000 = randNums(400000)
randomArray600000 = randNums(600000)
randomArray800000 = randNums(800000)
randomArray1000000 = randNums(1000000)


arraySetRandom = [randomArray10,randomArray50,randomArray100,randomArray1000,randomArray10000,randomArray100000, randomArray200000, randomArray400000, randomArray600000, randomArray800000, randomArray1000000]

"""
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

file = open("_a1_200000Ints.txt", "w+")
randNums(200000)
file.close()

file = open("_a1_400000Ints.txt", "w+")
randNums(400000)
file.close()

file = open("_a1_600000Ints.txt", "w+")
randNums(600000)
file.close()

file = open("_a1_800000Ints.txt", "w+")
randNums(800000)
file.close()

file = open("_a1_1000000Ints.txt", "w+")
randNums(1000000)
file.close()

file = open("special.txt", "w+")
randNums(50)                
file.close()
"""