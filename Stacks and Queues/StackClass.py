def string_stack(string):
    stack = []
    reversed_string = ""

# Loop through each char and append it to the stack (sam where s is at the bottom of the stack)
    for char in string:
        stack.append(char)

# While the stack is not empty, keep popping chars and append them to the string 
    while stack:
        reversed_string += stack.pop()


    return reversed_string

print(string_stack("sam"))
