# pytohn program to find the length of a string (3rd Way!)

# Using while loop

def findLen(str):
    counter = 0
    while str[counter:]:
        counter += 1
    return counter

str = str(input("Enter the string : "))

print(findLen(str))
