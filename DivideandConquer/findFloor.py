"""Write a function called findFloor which accepts a sorted array and a value x, and returns the floor of x in the array. The floor of x in an array is the largest element in the array which is smaller than or equal to x.
 If the floor does not exist, return -1."""

# Approach:
# Initialize left to 0 and right to the index of the last element in the array.
# Initialize floor to -1.
# Use a while loop to perform binary search on the array:
# Calculate the middle index mid of the current range.
# If the middle element is equal to x, return the middle element.
# If the middle element is less than x, update floor to the middle element, and move the left pointer to mid + 1.
# If the middle element is greater than x, move the right pointer to mid - 1.
# Return the floor value after the while loop completes.

def findFloor(arr, x):
        left = 0
        right = len(arr) - 1
        floor = -1
    
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == x:
                return arr[mid]
            elif arr[mid] < x:
                floor = arr[mid]
                left = mid + 1
            else:
                right = mid - 1
    
        return floor