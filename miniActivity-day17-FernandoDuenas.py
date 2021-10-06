'''
-   I want you to print the numbers between 1 and 100 (inclusive).

1.  If the number is divisible (able to divide) by 3, I would like you to print "fizz" instead of the number.

2.  If the number is divisible by 5 (able to divide), I would like you to print "buzz" instead of the number.

3.  if the number is divisible by BOTH 3 and 5 (able to divide), I would like you to print "fizzbuzz" instead of the number.

4.  If the number is not divisible by either 3 and 5 (abel to divide), I would like you to print the number itself instead.
'''

def fizzbuzz():
    for i in range(1,101):
        if i % 3 == 0 and i % 5 ==0:
            print("fizzbuzz")
        elif i % 3 == 0:        #this needs to be elif or else it will print the result and show the number which is not correct.
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)

fizzbuzz()

