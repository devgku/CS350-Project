import random

def quickSort(lst):
    if len(lst) <= 1:
        return lst
    else:
        p = random.choice(lst)
        low  = [x for x in lst if x <  p]
        med  = [x for x in lst if x == p]
        high = [x for x in lst if x >  p]
        return quickSort(low) + med + quickSort(high)

"""arr = [10, 7, 8, 9, 1, 5]
sortedArray = quickSort(arr)
print ("Sorted array is:")
print (sortedArray)"""
