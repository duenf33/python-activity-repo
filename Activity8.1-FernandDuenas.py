'''
Activity 8

- Write a Program to check the greatest among 3 numbers.

'''
num1 = input("Enter first number: ") # grabbing numbers from input.
num2 = input("Enter second number: ")
num3 = input("Enter third number: ")

def greatestNum(num):
    print("Out of these numbers: ", sorted(num)) # displaying sorted numbers from least to greater
    if num1 >= num2 and num1 >= num3:
        number = num1
    elif num2 >= num1 and num2 >= num3:
        number = num2
    else: 
        number = num3
    print("The greatest number is: ", number)

greatestNum([num1, num2, num3]) 

