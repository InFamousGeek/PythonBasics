# Python Program to find the length of a String (2nd way)

# using for loop 

# Returns length of string 
def findLen(str):
    counter = 0 
    for i in str:
        counter += 1
    return counter

str = str(input("Enther the string : "))

print(findLen(str))
