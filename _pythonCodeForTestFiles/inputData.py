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

file36 = open("_200000_binaryDigits.txt", "r")
if file36.mode == 'r':
    contents36 = file36.read()

file37 = open("_400000_binaryDigits.txt", "r")
if file37.mode == 'r':
    contents37 = file37.read()

file38 = open("_600000_binaryDigits.txt", "r")
if file38.mode == 'r':
    contents38 = file38.read()

file39 = open("_800000_binaryDigits.txt", "r")
if file39.mode == 'r':
    contents39 = file39.read()


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

file40 = open("__200000_revSorted_ints.txt", "r")
if file40.mode == 'r':
    contents40 = file40.read()

file41 = open("__400000_revSorted_ints.txt", "r")
if file41.mode == 'r':
    contents41 = file41.read()

file42 = open("__600000_revSorted_ints.txt", "r")
if file42.mode == 'r':
    contents42 = file42.read()

file43 = open("__800000_revSorted_ints.txt", "r")
if file43.mode == 'r':
    contents43 = file43.read()

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

file44 = open("_a1_200000Ints.txt", "r")
if file44.mode == 'r':
    contents44 = file44.read()

file45 = open("_a1_400000Ints.txt", "r")
if file45.mode == 'r':
    contents45 = file45.read()

file46 = open("_a1_600000Ints.txt", "r")
if file46.mode == 'r':
    contents46 = file46.read()

file47 = open("_a1_800000Ints.txt", "r")
if file47.mode == 'r':
    contents47 = file47.read()

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

file48 = open("_fiftyPctUnsorted_200000Ints.txt", "r")
if file48.mode == 'r':
    contents48 = file48.read()

file49 = open("_fiftyPctUnsorted_400000Ints.txt", "r")
if file49.mode == 'r':
    contents49 = file49.read()

file50 = open("_fiftyPctUnsorted_600000Ints.txt", "r")
if file50.mode == 'r':
    contents50 = file50.read()

file51 = open("_fiftyPctUnsorted_800000Ints.txt", "r")
if file51.mode == 'r':
    contents51 = file51.read()

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

file52 = open("_tenPctUnsorted_200000Ints.txt", "r")
if file52.mode == 'r':
    contents52 = file52.read()

file53 = open("_tenPctUnsorted_400000Ints.txt", "r")
if file53.mode == 'r':
    contents53 = file53.read()

file54 = open("_tenPctUnsorted_600000Ints.txt", "r")
if file54.mode == 'r':
    contents54 = file54.read()

file55 = open("_tenPctUnsorted_800000Ints.txt", "r")
if file55.mode == 'r':
    contents55 = file55.read()

file33 = open("_tenPctUnsorted_1000000Ints.txt", "r")
if file33.mode == 'r':
    contents33 = file33.read()

file34 = open("_tenPctUnsorted_special.txt", "r")
if file34.mode == 'r':
    contents34 = file34.read()

file56 = open("__10_sorted_ints.txt", "r")
if file56.mode == 'r':
    contents56 = file56.read()

file57 = open("__100_sorted_ints.txt", "r")
if file57.mode == 'r':
    contents57 = file57.read()

file58 = open("__1000_sorted_ints.txt", "r")
if file58.mode == 'r':
    contents58 = file58.read()

file59 = open("__10000_sorted_ints.txt", "r")
if file59.mode == 'r':
    contents59 = file59.read()

file60 = open("__100000_sorted_ints.txt", "r")
if file60.mode == 'r':
    contents60 = file60.read()

file61 = open("__200000_sorted_ints.txt", "r")
if file61.mode == 'r':
    contents61 = file61.read()

file62 = open("__400000_sorted_ints.txt", "r")
if file62.mode == 'r':
    contents62 = file62.read()

file63 = open("__600000_sorted_ints.txt", "r")
if file63.mode == 'r':
    contents63 = file63.read()

file64 = open("__800000_sorted_ints.txt", "r")
if file64.mode == 'r':
    contents64 = file64.read()

file65 = open("__1000000_sorted_ints.txt", "r")
if file65.mode == 'r':
    contents65 = file65.read()

file66 = open("__sorted_special.txt", "r")
if file66.mode == 'r':
    contents66 = file66.read()

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
array36 = contents36.split()
array37 = contents37.split()
array38 = contents38.split()
array39 = contents39.split()
array40 = contents40.split()
array41 = contents41.split()
array42 = contents42.split()
array43 = contents43.split()
array44 = contents44.split()
array45 = contents45.split()
array46 = contents46.split()
array47 = contents47.split()
array48 = contents48.split()
array49 = contents49.split()
array50 = contents50.split()
array51 = contents51.split()
array52 = contents52.split()
array53 = contents53.split()
array54 = contents54.split()
array55 = contents55.split()
array56 = contents56.split()
array57 = contents57.split()
array58 = contents58.split()
array59 = contents59.split()
array60 = contents60.split()
array61 = contents61.split()
array62 = contents62.split()
array63 = contents63.split()
array64 = contents64.split()
array65 = contents65.split()
array66 = contents66.split()

arraySetBinaryDigits = [array1,array2,array3,array4,array5,array35,array36,array37,array38,array39,array6]
arraySetRevSorted = [array7,array13,array8,array9,array10,array11,array40,array41,array42,array43,array12]
arraySetRandom = [array15,array14,array16,array17,array18,array19,array44,array45,array46,array47,array20]
arraySetFiftyUnsorted = [array21,array27,array22,array23,array24,array25,array48,array49,array50,array51,array26]
arraySetTenUnSorted = [array28,array34,array29,array30,array31,array32,array52,array53,array54,array55,array33]
arraySorted = [array56,array66,array57,array58,array59,array60,array61,array62,array63,array64,array65]

