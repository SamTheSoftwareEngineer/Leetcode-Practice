def linear_search(list, target):
    
    for i in range(0, len(list)):
        """Returns the index of the target in the loop, if it exists """
        if list[i] == target:
            return i 
    return None 

def verify(index):
    if index is not None:
        print("Target found at index : ", index)
    else:
        print("Target not found in list.")

numbers = [1,2,3,4,5,6,7,8,9,10]

result = linear_search(numbers, 6)
verify(result)