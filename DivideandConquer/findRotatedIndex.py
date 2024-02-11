"""Write a function called findRotatedIndex which accepts a rotated array of sorted numbers and an integer. 
The function should return the index of num in the array. If the value is not found, return -1."""

# Time Complexity Constraint: O log N

# Approach:
# In our output, the array is no longer sorted since it has been rotated, so we can'r use binary search here
# Using a loop, we can check each value in the arr and see if it matches the target, if it does we return the index 
# Otherwise we return -1 
def find_rotated_index(list, target):

    for i in range(len(list)):
        if list[i] == target:
            return i 
    
    return -1 

print(find_rotated_index([3,4,1,2],4)) # 1 
print(find_rotated_index([6, 7, 8, 9, 1, 2, 3, 4], 8)) # 2
print(find_rotated_index([6, 7, 8, 9, 1, 2, 3, 4], 3)) # 6
print(find_rotated_index([37,44,66,102,10,22],14)) # -1
print(find_rotated_index([6, 7, 8, 9, 1, 2, 3, 4], 12)) # -1