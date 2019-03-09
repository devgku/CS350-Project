contents = []

#pick a file to work with
file = open("special.txt", "r")
if file.mode == 'r':
    contents = file.read()
file.close()

n = 0
def sortNums(n, contents):
    arr = list(map(int, contents.split()))
    arr.sort()
    for i in range(n):
        file.write("%d\n" % (arr[i]))


file = open("__sorted_special.txt", "w+")
sortNums(50, contents)
file.close()



# add name to file. Will generate n integers separated by \n

#pick a file to work with
file = open("_a1_10Ints.txt", "r")
if file.mode == 'r':
    contents = file.read()
file.close()

#creates a file to
file = open("__10_sorted_Ints.txt", "w+")
sortNums(10, contents)
file.close()



file = open("_a1_100Ints.txt", "r")
if file.mode == 'r':
    contents = file.read()
file.close()


#pick a file to work with
file = open("__100_sorted_Ints.txt", "w+")
sortNums(100, contents)
file.close()


file = open("_a1_1000Ints.txt", "r")
if file.mode == 'r':
    contents = file.read()
file.close()


file = open("__1000_sorted_Ints.txt", "w+")
sortNums(1000, contents)
file.close()


#pick a file to work with
file = open("_a1_10000Ints.txt", "r")
if file.mode == 'r':
    contents = file.read()
file.close()

file = open("__10000_sorted_Ints.txt", "w+")
sortNums(10000, contents)
file.close()


#pick a file to work with
file = open("_a1_100000Ints.txt", "r")
if file.mode == 'r':
    contents = file.read()
file.close()

file = open("__100000_sorted_Ints.txt", "w+")
sortNums(100000, contents)
file.close()

#pick a file to work with
file = open("_a1_200000Ints.txt", "r")
if file.mode == 'r':
    contents = file.read()
file.close()

file = open("__200000_sorted_Ints.txt", "w+")
sortNums(200000, contents)
file.close()

#pick a file to work with
file = open("_a1_400000Ints.txt", "r")
if file.mode == 'r':
    contents = file.read()
file.close()

file = open("__400000_sorted_Ints.txt", "w+")
sortNums(400000, contents)
file.close()

#pick a file to work with
file = open("_a1_600000Ints.txt", "r")
if file.mode == 'r':
    contents = file.read()
file.close()

file = open("__600000_sorted_Ints.txt", "w+")
sortNums(600000, contents)
file.close()

#pick a file to work with
file = open("_a1_800000Ints.txt", "r")
if file.mode == 'r':
    contents = file.read()
file.close()

file = open("__800000_sorted_Ints.txt", "w+")
sortNums(800000, contents)
file.close()

#pick a file to work with
file = open("_a1_1000000Ints.txt", "r")
if file.mode == 'r':
    contents = file.read()
file.close()


file = open("__1000000_sorted_Ints.txt", "w+")
sortNums(1000000, contents)
file.close()