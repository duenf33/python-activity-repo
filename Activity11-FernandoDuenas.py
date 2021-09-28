# Write a function called isEven() that will take in an integer as a parameter.
# Your function is to return whether or not that number passed in is even.

'''def isEven(elem):
    if elem % 2 == 0:                    # Checking if the number passed as an argument is even or not by checking the remainder. 
        print("even")
        return True
    else:
        print("not even")
        return False
isEven(2)'''

# --------------------------

# Write a function called isSorted which will be passed in a list of numbers/
# Your functions job is to determine if the list is in need of being sorted, or if it already came sorted.
# Your function should return a boolean determining whether or not that is the case.

'''def isSorted(listOfNums):
    if listOfNums == sorted(listOfNums):
        print("Sorted.")
        return True
    else:
        print("not sorted.")
        return False

result = isSorted([1,2,3,4,5,6,7,8,9])
print(result)'''

# ---------------------------

# Write a function that takes in a String as a parameter.
# Your function is to return a Boolean
    # True if it is a Palindrome
    # False if it is not a Palindrome

# What is a Palindrome?
    # A palindrome is any word that when spelled forward or backward
    # result is the same word:
    # Example: "racecar" -> "racecar" (IS a palindrome)
    # Example: "pizza" -> "azzip" (IS NOT a palindrome)

def palindrome(str):
    lowerCaseStr = str.casefold()
    revStr = reversed(lowerCaseStr)
    # listStr = "".join(list(str))
    listStr = list(str)
    # listRevStr = "".join(list(revStr))
    listRevStr = list(revStr)

    print(revStr)
    print("".join(list(str)))
    print("".join(list(revStr)))

    if listStr == listRevStr:
        print("True: ", str)
        return True
    else: 
        print("False", str)
        return False

result = palindrome("car")
print(result)