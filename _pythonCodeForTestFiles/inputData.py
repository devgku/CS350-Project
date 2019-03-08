# this file creates array sets of experimental data using in sorting algorithms

# import experimental data from txt files.
file1 = open("_10_binaryDigits.txt", "r")
if file1.mode == 'r':
    contents1 = file1.read()

file2 = open("_50_binaryDigits.txt", "r")
if file2.mode == 'r':
    contents2 = file2.read()

file3 = open("_100_binaryDigits.txt", "r")
if file3.mode == 'r':
    contents3 = file3.read()

file4 = open("_1000_binaryDigits.txt", "r")
if file4.mode == 'r':
    contents4 = file4.read()

file5 = open("_10000_binaryDigits.txt", "r")
if file5.mode == 'r':
    contents5 = file5.read()

file35 = open("_100000_binaryDigits.txt", "r")
if file35.mode == 'r':
    contents35 = file35.read()

file6 = open("_1000000_binaryDigits.txt", "r")
if file6.mode == 'r':
    contents6 = file6.read()

file7 = open("__10_revSorted_ints.txt", "r")
if file7.mode == 'r':
    contents7 = file7.read()

file8 = open("__100_revSorted_ints.txt", "r")

if file8.mode == 'r':
    contents8 = file8.read()

file9 = open("__1000_revSorted_ints.txt", "r")
if file9.mode == 'r':
    contents9 = file9.read()

file10 = open("__10000_revSorted_ints.txt", "r")
if file10.mode == 'r':
    contents10 = file10.read()

file11 = open("__100000_revSorted_ints.txt", "r")
if file11.mode == 'r':
    contents11 = file11.read()

file12 = open("__1000000_revSorted_ints.txt", "r")
if file12.mode == 'r':
    contents12 = file12.read()

file13 = open("__rev_special.txt", "r")
if file13.mode == 'r':
    contents13 = file13.read()

file14 = open("special.txt", "r")
if file14.mode == 'r':
    contents14 = file14.read()

file15 = open("_a1_10Ints.txt", "r")
if file15.mode == 'r':
    contents15 = file15.read()

file16 = open("_a1_100Ints.txt", "r")
if file16.mode == 'r':
    contents16 = file16.read()

file17 = open("_a1_1000Ints.txt", "r")
if file17.mode == 'r':
    contents17 = file17.read()

file18 = open("_a1_10000Ints.txt", "r")
if file18.mode == 'r':
    contents18 = file18.read()

file19 = open("_a1_100000Ints.txt", "r")
if file19.mode == 'r':
    contents19 = file19.read()

file20 = open("_a1_1000000Ints.txt", "r")
if file20.mode == 'r':
    contents20 = file20.read()

file21 = open("_fiftyPctUnsorted_10Ints.txt", "r")
if file21.mode == 'r':
    contents21 = file21.read()

file22 = open("_fiftyPctUnsorted_100Ints.txt", "r")
if file22.mode == 'r':
    contents22 = file22.read()

file23 = open("_fiftyPctUnsorted_1000Ints.txt", "r")
if file23.mode == 'r':
    contents23 = file23.read()

file24 = open("_fiftyPctUnsorted_10000Ints.txt", "r")
if file24.mode == 'r':
    contents24 = file24.read()

file25 = open("_fiftyPctUnsorted_100000Ints.txt", "r")
if file25.mode == 'r':
    contents25 = file25.read()

file26 = open("_fiftyPctUnsorted_1000000Ints.txt", "r")
if file26.mode == 'r':
    contents26 = file26.read()

file27 = open("_fiftyPctUnsorted_special.txt", "r")
if file27.mode == 'r':
    contents27 = file27.read()

file28 = open("_tenPctUnsorted_10Ints.txt", "r")
if file28.mode == 'r':
    contents28 = file28.read()

file29 = open("_tenPctUnsorted_100Ints.txt", "r")
if file29.mode == 'r':
    contents29 = file29.read()

file30 = open("_tenPctUnsorted_1000Ints.txt", "r")
if file30.mode == 'r':
    contents30 = file30.read()

file31 = open("_tenPctUnsorted_10000Ints.txt", "r")
if file31.mode == 'r':
    contents31 = file31.read()

file32 = open("_tenPctUnsorted_100000Ints.txt", "r")
if file32.mode == 'r':
    contents32 = file32.read()

file33 = open("_tenPctUnsorted_1000000Ints.txt", "r")
if file33.mode == 'r':
    contents33 = file33.read()

file34 = open("_tenPctUnsorted_special.txt", "r")
if file34.mode == 'r':
    contents34 = file34.read()
#fills array object with file data
array1 = contents1.split()
array2 = contents2.split()
array3 = contents3.split()
array4 = contents4.split()
array5 = contents5.split()
array6 = contents6.split()
array7 = contents7.split()
array8 = contents8.split()
array9 = contents9.split()
array10 = contents10.split()
array11 = contents11.split()
array12 = contents12.split()
array13 = contents13.split()
array14 = contents14.split()
array15 = contents15.split()
array16 = contents16.split()
array17 = contents17.split()
array18 = contents18.split()
array19 = contents19.split()
array20 = contents20.split()
array21 = contents21.split()
array22 = contents22.split()
array23 = contents23.split()
array24 = contents24.split()
array25 = contents25.split()
array26 = contents26.split()
array27 = contents27.split()
array28 = contents28.split()
array29 = contents29.split()
array30 = contents30.split()
array31 = contents31.split()
array32 = contents32.split()
array33 = contents33.split()
array34 = contents34.split()
array35 = contents35.split()

arraySetBinaryDigits = [array1,array2,array3,array4,array5,array35,array6]
arraySetRevSorted = [array7,array13,array8,array9,array10,array11,array12]
arraySetRandom = [array15,array14,array16,array17,array18,array19,array20]
arraySetFiftyUnsorted = [array21,array27,array22,array23,array24,array25,array26]
arraySetTenUnSorted = [array28,array34,array29,array30,array31,array32,array33]


