# Given an integer array nums, return true if any value appears at least twice in the array,
# and return false if every element is distinct.

# Example 1:

# Input: nums = [1,2,3,1]
# Output: true
# Example 2:

# Input: nums = [1,2,3,4]
# Output: false
# Example 3:

# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true

# Approach:
# We can use a set to check for duplicates by adding each element from the nums array into the set
# If we find a number already exist in the set, then that means there is a duplicate present and we can return true
# otherwise we return false



def containsDuplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False 
            


print(containsDuplicate([1,2,3,4,5]))
print(containsDuplicate([]))
print(containsDuplicate([1,2,3,3,4]))
