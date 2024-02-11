"""Given an array of 1s and 0s which has all 1s first followed by all 0s,
 write a function called countZeroes, which returns the number of zeroes in the array."""

# Time Complexity Constraint: O log N


# Approach:
# First we can sort the array so that all the zeroes appear at the start of the arr
# Using a pointer, we can check for our first non-zero char, which indicates that we have reached the end of the zeroes
# We can use a variable to keep count of how many zeroes there are before we reach our first nonZeroChar

def countZeroes(arr):
    arr.sort()
    zero_count = 0

    for i in range(len(arr)):
        if arr[i] == 0:
            zero_count += 1

    return zero_count

print(countZeroes([1,1,1,1,0,0])) # 2
print(countZeroes([1,0,0,0,0])) # 4
print(countZeroes([0,0,0])  )# 3
print(countZeroes([1,1,1,1])) # 0



