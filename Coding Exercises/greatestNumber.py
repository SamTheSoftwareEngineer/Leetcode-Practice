def greatestNumber(arr):
    greatestValue = arr[0]  # Assume the first element is the greatest number
    
    for i in arr:
        if i > greatestValue:
            greatestValue = i  # Update greatestValue if we find a greater number
    
    return greatestValue
    
print(greatestNumber([3,1,1,0])) # 3 
print(greatestNumber([2,4,6,8])) # 8
