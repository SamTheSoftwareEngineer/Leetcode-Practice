"""Given a sorted array and a number, write a function called 
sortedFrequency that counts the occurrences of the number in the array"""

# Time Constraint: O log N

# Approach:
# Given that the array is sorted, that means that all occurences of the number will be adjacent to each other
# We can use a variable to keep track of the count of the occurences of the number so far 
# Then we can loop through the array and if any number in the array equals the target,, we increment our number count 
# Lastly, we simply return our number count 

def sortedFrequency(arr, number):

    number_count = 0 

    for i in range(len(arr)):
        if arr[i] == number:
            number_count += 1
    
    if number_count == 0:
        return -1
    else:
        return number_count 

print(sortedFrequency([1,1,2,2,2,2,3],2)) # 4
print(sortedFrequency([1,1,2,2,2,2,3],3)) # 1
print(sortedFrequency([1,1,2,2,2,2,3],1)) # 2
print(sortedFrequency([1,1,2,2,2,2,3],4)) #  -1