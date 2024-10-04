# MaxSubArray problem - using Divide and Conquer stradegy
# Week 1
# Given an array of numbers, find the maximum SubArray for the part of the array that goes from A sub l to A sub u.

array = [1, 19, 5, -4, 7, 18, 15, -10]
# 1st try (according to the lecture psuedo code)


# def maxSubArray(A, l, u):
#     # base case: if sub arr has only has one element
#     if (u == l):
#         return 0
#     # base case 2: if sub arr has 2 elements
#     if (u == l + 1):
#         return max(A[u]-A[l], 0)
#     # find a mid point
#     mid = (l + u) // 2
#     # call the function recursively on left & right side
#     left = maxSubArray(A, l, mid)
#     right = maxSubArray(A, mid + 1, u)
#     # handle a case where max sub array is found across both sides
#     minLeft = minElement(A, l, mid)
#     maxRight = maxElement(A, mid + 1, u)
#     # return which ever is largest
#     return max(left, right, (maxRight - minLeft))


# def minElement(A, l, u):
#     minElm = float('inf')
#     for i in range(u + 1):
#         minElm = min(minElm, A[i])
#     return minElm


# def maxElement(A, l, u):
#     maxElm = float('-inf')
#     for i in range(u + 1):
#         maxElm = max(maxElm, A[i])
#     return maxElm


# print(maxSubArray(array, 0, len(array) - 1))
# print(minElement(array, 0, len(array)-1))
# print(maxElement(array, 0, len(array)-1))


# 2nd try (according to the text book psuedo code)

# def findMaximumSubarray(A, low, high):
#     if high == low:
#         return (low, high, A[low])
#     else:
#         mid = (low + high) // 2

#         (left_low, left_high, left_sum) = findMaximumSubarray(A, low, mid)
#         (right_low, right_high, right_sum) = findMaximumSubarray(A, mid + 1, high)
#         (cross_low, cross_high, cross_sum) = findMaxCrossingSubarray(A, low, mid, high)

#         if left_sum >= right_sum and left_sum >= cross_sum:
#             return (left_low, left_high, left_sum)
#         elif right_sum >= left_sum and right_sum >= cross_sum:
#             return (right_low, right_high, right_sum)
#         else:
#             return (cross_low, cross_high, cross_sum)


# def findMaxCrossingSubarray(A, low, mid, high):
#     # Calculate maximum subarray sum on the left side of mid
#     left_sum = float("-inf")
#     sum = 0
#     max_left = mid
#     for i in range(mid, low - 1, -1):
#         sum += A[i]
#         if sum > left_sum:
#             left_sum = sum
#             max_left = i

#     # Calculate maximum subarray sum on the right side of mid
#     right_sum = float("-inf")
#     sum = 0
#     max_right = mid + 1
#     for j in range(mid + 1, high + 1):
#         sum += A[j]
#         if sum > right_sum:
#             right_sum = sum
#             max_right = j

#     # Combine the left_sum and right_sum to form the crossing subarray
#     return (max_left, max_right, left_sum + right_sum)


# # Example usage
# array = [1, 19, 5, -4, 7, 18, 15, -10]
# result = findMaximumSubarray(array, 0, len(array) - 1)
# print(result)

# Brute force way

def findM(a):
    max_dif = float('-inf')
    max_left = None
    max_right = None
    for left in range(len(a)-1):
        for right in range(left + 1, len(a), 1):
            dif = a[right] - a[left]
            if dif > max_dif:
                max_dif = dif
                max_left = left
                max_right = right
    return max_left, max_right, max_dif


# array = [1, 19, 5, -4, 7, 18, 15, -10]
print(findM(array))
