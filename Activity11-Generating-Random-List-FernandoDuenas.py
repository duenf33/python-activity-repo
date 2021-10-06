'''

Write a function that will take in an integer as a parameter, and will create a list of the size passed in as an argument. I also want you to populate that whole list with random numbers between 0-1023. You're going to be using the getrandbits() method of the random module, so think about how to arrive at that outcome.

#Example I/O
Input -> 5
Output -> [x, y, z, a, b]

'''
import random

# this is what I was coming out with. It definetily shows I was a little bit confuse with it. I need to look more into it.
'''def intParam(num):
    print("line 13: ",*range(random.randrange(num + 1)))
    for i in range(random.randrange(num)):
        num = num + 1
        print("Line 16: ",num)
        if num:
            print(random.getrandbits(num))
            return num

print("Result: ",intParam(5))'''

# def functionName(num = 5):
#     #Create a list of the size passed in
#     solution = []  # I need to get this to be of length (the argument passed in.)
    
#     # I need to populate that list with as many items as specified in the argument, I can loop using the condition that I start at 0 and stop at the number passed in as the argument.

#     for i in range(num):
#         # Random Number to append between 0-1023 or 1024.
#             # 1 1 1 1 1 1 1 1 1 1
#         # I need to get a random number betwee 0-1023 or 1023.
#         '''randomNum = random.getrandbits(10)'''
#         '''print(f"My random number at the {i+1} iteration and the random number is {randomNum}")'''
#         '''solution.append(randomNum)'''
#         solution.append(random.getrandbits(10))
#         # print(f"My list now looks like this: {solution}")

#     # print(f"this is my final solution: {solution}")
#     print(f"How many times did 1025 appear in a list {solution.count(1023)}")
#     return solution

# functionName(512)
        
# -------------------------------------------

#Activity 11.1: Working with RandRange
'''
Similar to the previous problem, I want you to create a function that will generate a random list and takes in a number as a parameter that will be the size of the list. BUT I want the values passed in to range between 20 and 78 specifically exclusive of the 78.

#Step 1: Write the function name and make sure it has a parameter place holder that will represent an Integer in your function
#Step 2: Make a new list
#Step 3: Make that list the size of the paramter/argument passed in
#Step 4: 
#Step 5: Return the List
'''

def randomList(num = 3):
    result = []                                 # the result empty list will hold the values appended to it the "num" times from the range 20 to 78.
    for i in range(num):                        # this will iterate thru the num input param.
        result.append(random.randrange(20,78))  # appending random number from 20 to 78 to the list result.
    # print(result.count(78))
    print(result)
    return result

randomList(5)


