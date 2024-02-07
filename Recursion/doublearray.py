"""Write a function that takes an array of numbers and doubles each number in the arrray in-place"""

# Writing in recursive:
# 1. Write the recursive statement first
# 2. Set the base case 


# Can input zero as a default parameter for the starting arguments 
def double_array(arr, index=0):
    # Base case: when the index goes past the end of the array
    if index >= len(arr):
        return 
    arr[index] *= 2
    double_array(arr, index + 1)

array = [1,2,3,4]
double_array(array)
print(array)