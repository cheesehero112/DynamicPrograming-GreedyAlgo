# Challenge 1
# https://www.youtube.com/watch?v=ib4BHvr5-Ao

# Given an array of numbers, Write a function to return the minimum value while doing a three way search

# write a function that finds the min elm
# input: array // output: recursive function
# return null if the array is empty
# return the evaluated result of findMin function

def findMinElement(array):
    if len(array) == 0:
        return null
    return findMin(0, len(array) - 1, array)


# write a function that finds the min recursively
# input: (i, j, array) // output: smallest number
    # define a base case - if all 3 sections' index are the same, there is only one elm in the array. If so return the last elm of the array
    # define the 2 mid points in the array (mid1, mid2)
    # i --- mid1 --- mid2 --- j
    # return the min of calling the function recursively

def findMin(i, j, array):
  # handle size 1 interval
    if (i == j):
        return array[i]
  # handle size 2 interval
    if j - i == 1:
        return min(array[i], array[i + 1])
  # handle size 3 interval
    if j - i == 2:
        return min(array[i], array[i + 1], array[i + 2])
    third = round((j - i)/3)
    midIndex1 = i + third
    midIndex2 = i + 2 * third

    min1 = findMin(i, midIndex1, array)
    min2 = findMin(midIndex1 + 1, midIndex2, array)
    min3 = findMin(midIndex2 + 1, j, array)
    return min(min1, min2, min3)


# answer should be
arr1 = [3, 2, 1, 4, 10, 6, 9, 8, 12, -10, -3.5]
# midIndex1 = round(0 + len(arr1)/3)
# midIndex2 = len(arr1) - midIndex1
# print(midIndex1, midIndex2)

print(findMinElement(arr1))
