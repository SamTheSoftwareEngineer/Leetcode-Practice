"""Write a function called findRotationCount which accepts an array of distinct numbers sorted in increasing order. 
The array has been rotated counter-clockwise n number of times. Given such an array, find the value of n.
"""

# Approach:
# If we keep track of the start value of the arr (the minimum since the arr is sorted), its index will be our 
# number of rotations
# Using binary search we can search for the minimum value using two pointers
# Our left pointer will search for the minimum value's index while our right pointer will tell us whether to look
# on the right or left side of the list 
# Once we find the minimum number, we simply return its index (our left pointer)
def find_rotation_count(arr):
    left = 0
    right = len(arr) - 1
    
    while left < right:
        mid = (left + right) // 2
        
        if arr[mid] > arr[right]:
            left = mid + 1
        else:
            right = mid
    
    return left


