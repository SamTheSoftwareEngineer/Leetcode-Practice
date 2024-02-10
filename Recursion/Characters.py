"""Use recursion to write a function that accepts an array of strings and returns the total number of chars across all strings"""

def count_total_characters(array):
    # Base case: when the array is empty
    if len(array) == 0:
        return 0

    # Alternative base case: when there is only one string in the array
    if len(array) == 1:
        return len(array[0])

    return len(array[0]) + count_total_characters(array[1:])

input = ["ab", "c", "def", "ghij"] 
print(count_total_characters(input))  # Output: 10