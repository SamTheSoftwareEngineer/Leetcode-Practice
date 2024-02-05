"""Write a function that returns the first non-duplicated (unique) character in a string."""



# Approach:
# We can use a hashmap to store the number of occurences of each letter in the string
# We loop through the string and return the first char with a count of one
def find_non_duplicated_letter(s):
    char_count = {}
    
    # Populate the hashmap with character counts
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    # Find the first non-duplicated character
    for char in s:
        if char_count[char] == 1:
            return char

    # Return None if no non-duplicated character is found
    return None

print(find_non_duplicated_letter("minimum")) # n