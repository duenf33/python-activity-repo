'''
Mini Activity: While Loops
1. create a while loop that goes through the 12 days of christmas:
    - On the 1 day of christmas
    - On the 2 day of christmas
        ...
    - 12 day of christmas

'''
# this is not the correct answer:
'''day = [
'A partridge in a pear tree',
'Two turtle doves',
'Three french hens',
'Four calling birds',
'Five gold rings',
'Six geese a-laying',
'Seven swans a-swimming',
'Eight maids a-milking',
'Nine ladies dancing',
'Ten lords a-leaping',
'Eleven pipers piping',
'Twelve drummers drumming']

i = 0
while i < len(day):
    elem = day[i]
    i += 1
    print(elem)'''

# this is the correct answer:
'''dayOfXmas = 1
limit = 12

while(dayOfXmas <= limit):
    print(f"on the {dayOfXmas} day of christmass...")
    dayOfXmas += 1
'''
'''
2. Create a while loop that takes a list of integers, and gives the sum of the integers.

'''

# this is the wrong answer:
'''# these is the list of numbers that will pass thru the while loop
nums = [9, 5, 7, 2, 12, 174, 1]

i = 0   # the index will start at 0
total = 0
while i < len(nums):    # if the index 0 is less than the length of the list (the amount of items) 
    total = nums[i]     # each item in the list will be added to the total variable.
    i += 1              # the index "i" will keep incrementing by one. 
   
    print(total)      # this will list all the items in the list in the same order.
# for some reason I have been having some issues trying to add everything in the total variable. I know there is a method sum() that easealy adds everything in a list, but, this is kicking my ass.'''

# this is the correct answer:
myNumbers = [9, 5, 7, 2, 12, 174, 1]
# initia
i = 0
sum1 = 0
while(i < len(myNumbers)):
    # define the logic:
    sum1 = sum1 + myNumbers[i]
    #increment:
    i = i + i

print(sum1)
print(sum(myNumbers))