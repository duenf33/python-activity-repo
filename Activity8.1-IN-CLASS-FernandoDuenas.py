'''
- Create a function that takes in 3 integers as parameters. Perform some operation that will compare these values and order the numbers from least to greatest. Return these values as a set in a tuple.
    * This function will take in 3 numbers as input (in the parameter).
    * This function will return to me a sorted Tuple of those 3 numbers passed in as input
- Remember to check the data type of the value you are returning. Your function assumes that data type.

'''

num1 = input("1st #: ")
num2 = input("2nd #: ")
num3 = input("3rd #: ")

def intFunc(nums):
    numbers = sorted(nums)
    tuple1 = tuple(numbers)
    return tuple1
    
result = intFunc([num1, num2, num3])
print(result)