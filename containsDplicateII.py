# Given an integer array nums and an integer k, 
# return true if there are two distinct indices i and j in the array such that
# nums[i] == nums[j] and abs(i - j) <= k.


def containsDuplicate(nums, k):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j] and abs(i - j) <= k:
                return True
        return False 
    
print(containsDuplicate([1,2,3,1], 4)) # Expect true 
# nums = [1,2,3,1], k = 3 
print(containsDuplicate([1,2,3,1,2,3], 2)) # Expect False
# nums = [1,2,3,1,2,3], k = 2
