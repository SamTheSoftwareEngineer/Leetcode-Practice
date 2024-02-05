def findIntersection(arr):
    duplicates = set()

    for char in arr:
        if char in duplicates:
            return char 
        
        duplicates.add(char)


print(findIntersection(["a","b","c","d","e","e"])) # e
print(findIntersection(["a", "b", "c", "d"])) # None 