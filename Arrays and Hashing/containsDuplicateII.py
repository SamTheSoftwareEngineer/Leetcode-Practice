# Given an integer array nums and an integer k, 
# return true if there are two distinct indices i and j in the array such that
# nums[i] == nums[j] and abs(i - j) <= k.


# def containsDuplicate(nums, k):
#     for i in range(len(nums)):
#         for j in range(i+1, len(nums)):
#             if nums[i] == nums[j] and abs(i - j) <= k:
#                 return True
#         return False 

def containsDuplicate(nums, k): 
    # Store the indices of each number 
    num_indices = {}
    # Iterate through the array
    for i, num in enumerate(nums):
        # If we see a number that already exists in the hashmap and the diff between the current and stored index is less than k
        if num in num_indices and i - num_indices[num] <= k:
            return True
        num_indices[num] = i
    return False 

print(containsDuplicate([1,2,3,1], 4)) # Expect true 
# nums = [1,2,3,1], k = 3 
print(containsDuplicate([1,2,3,1,2,3], 2)) # Expect False
# nums = [1,2,3,1,2,3], k = 2
