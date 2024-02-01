# Write a function that returns the intersection of 2 arrays. Return the result as a third array. 
def findIntersection(arr1, arr2):
    intersection = []
    hashmap = {}

    # Populate the hashmap with values from arr1
    for i in arr1:
        hashmap[i] = True
    
    # Check for intersection with arr2 and populate the intersection list
    for j in arr2:
        if j in hashmap:
            intersection.append(j)

    return intersection

print(findIntersection([1,2,3,4,5], [0,2,4,6,8]))  # Output: [2, 4]