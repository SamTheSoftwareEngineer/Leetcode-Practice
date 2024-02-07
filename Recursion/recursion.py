"""Write a function that accepts an array of arrays which contains numbers and arrays. Using recursion, return just the numbers"""


# Approach:
# 1. We iterate over each item in the outer array
# 2. If the value is another array, we recursively call the function on that subarray
def return_numbers(arr):
    for value in arr:
        # if the current item is a "list" e.g an array
        if isinstance(value, list):
            return_numbers(value)
        else:
            print(value)

print(return_numbers([[1,2,3,4,5],7,8,8]))