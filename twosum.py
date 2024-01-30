"""Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

"""

# O(n^2)
# def twoSum(nums, target):
#     for i in range(len(nums)):
#         for j in range (i+1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 return [i, j]
            
# print(twoSum([2, 7, 11, 15], 9))

# O(n)
def twoSum(nums, target):
    prevMap = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in prevMap:
            return [prevMap[diff], i]
        prevMap[num] = i
    return None 

print(twoSum([2, 7, 11, 15], 9))
print(twoSum([2,5,6,7], 10))
