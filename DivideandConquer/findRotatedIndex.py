"""Write a function called findRotatedIndex which accepts a rotated array of sorted numbers and an integer. 
The function should return the index of num in the array. If the value is not found, return -1."""

# Time Complexity Constraint: O log N

# Approach:
# Since the array is sorted, we know that all the numbers occur in ascending order which menas we can use binary
# search to eliminate some of the numbers that are less than or greater than our target number

# First, we initialize two pointers on either side of the arr
# Then we calculate our midpoint (left + right) // 2
# If our midpoint happens to be the number, we return it
# Otherwise, if our midpoint is less than the number, we know we have to move our left pointer to the right
# If the midpoint is greater than the number, we move our right pointer to the left 

def find_rotated_index(list, target):
    left = 0
    right = len(list) - 1

    while left <= right:
        mid = (left + right) // 2 
        if list[mid] == target:
            return mid
        elif list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1 
    
    return -1 

print(find_rotated_index([3,4,1,2],4)) # 1 
print(find_rotated_index([6, 7, 8, 9, 1, 2, 3, 4], 8)) # 2
print(find_rotated_index([6, 7, 8, 9, 1, 2, 3, 4], 3)) # 6
print(find_rotated_index([37,44,66,102,10,22],14)) # -1
print(find_rotated_index([6, 7, 8, 9, 1, 2, 3, 4], 12)) # -1