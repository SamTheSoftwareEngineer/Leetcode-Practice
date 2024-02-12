"""Write a function that accepts a string that contains all the letters of the alphabet except one and returns the missing letter.
The function should have a time complexity of O(N)"""


# Approach:
# Initialize an empty hashmap to store the occurrence of each letter.
# Loop through the given string and update the hashmap with the count of each letter.
# After populating the hashmap, loop through the alphabet letters and check if any letter is missing in the hashmap.
# Return the missing letter.

def find_missing_letter(s):
    alphabet_map = {}

    # Step 1: Populate the hashmap
    for char in s:
        # If the character is not in the map, we return the value of zero, otherwise we increment it by 1
        alphabet_map[char] = alphabet_map.get(char, 0) + 1

    # Step 2: Check for the missing letter
    for letter in "abcdefghijklmnopqrstuvwxyz":  
        if alphabet_map.get(letter, 0) == 0:
            return letter

# Example usage
input_string = "abcdefghijklnopqrstuvwxyz"  # Replace with your input
result = find_missing_letter(input_string)
print(result)
