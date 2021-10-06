#Activity 11.2: RPS
'''
- Create a function that plays rock paper scissors with you....
- You are to ask the user for INPUT
- If the user inputs "Rock" -> "Scissors" will lose, and "Paper" will win
- If the user inputs "Paper" -> "Rock" will lose, and "Scissor" will win
- If the user inputs "Scissors" -> "Paper" will lose, and "Rock" will win

#HINT
- How can I make the computer make a RANDOM choice between those.... Then maybe compare that computers choice to the user input.... 
- Since the computers choice can be three different values, what I can you use to store a sequence of values
- 3 values is 3 values, do you know a way to generate a random number between 0 and 3? Will it be inclusive of the 3? 
'''
import random

inputElem = input("Choose... rock, paper or scissors: ")

inputs = ['rock', 'paper', 'scissors']
randomInput = random.randint(0, 2)

def game(elem):

    elemLcase = elem.casefold()
    if inputs[randomInput] == elemLcase:
        return "this is a tie"
    elif elemLcase == 'rock':
        if inputs[randomInput] == 'scissors':
            return 'rock wins'
        else:
            return 'paper loses'
    elif elemLcase == 'paper':
        if inputs[randomInput] == 'rock':
            return 'rock loses'
        else:
            return 'scissors win'
    elif elemLcase == 'scissors':
        if inputs[randomInput] == 'paper':
            return 'paper loses'
        else:
            return 'rock wins'


print(game(inputElem))