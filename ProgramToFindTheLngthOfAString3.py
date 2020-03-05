# Python program to find the length of a string (4th Way!)

# using join and count 
  
# Returns length of string

def findLen(str):
    if not str:
        return 0
    else:
        some_random_text = "py"
        return ((some_random_text).join(str)).count(some_random_text) + 1

str = str(input("Enter the string : " ))

print(findLen(str))
