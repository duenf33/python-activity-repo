'''
Activity 10
* write a function that given a list will print out all the values in that list

'''

def func1(nums):
    for i in nums:
        print(i)

func1([5,2,6,1,8])

'''
* Write a function that takes in one integer as a parameter and will print out your name as many times as specified by the argument.

'''

name = input("Enter Your Name: ")
integer = input("Enter a numnber: ")

def func2(elem):
    for elem in name:
        print(name)

func2(integer)