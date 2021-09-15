# 1. 
firstName = "Fernando"
lastName = "Duenas"
favoriteColor = "blue"
favoriteMeal = "BBQ"

# 2. Print out a sentence in Pythin that references your variables and say "My first name is ...... my last name is...... my favorite color is ...... and my favorite mean is......"


# 3. Repeat this using:
    # a. F-string
print("F-String ===> ",f"My First Name is {firstName}. My Last Name is {lastName}. My favorite color is {favoriteColor} and my favorite meal is {favoriteMeal}")

    # b. Concatenation
print("Concatenation ===> ","My first name is " + firstName + ". My last name is " + lastName + ". My favorite color is" + favoriteColor + " and my favorite meal is " + favoriteMeal + ".")

    # c. Argument by Position
argByPos = "my name is {0}. my last name is {1}. My favorite color is {2} and my favorite meal is {3}".format(firstName, lastName, favoriteColor, favoriteMeal)
print("Argument by Position ===> ",argByPos)

    # d. Argument by Name
argByName = "my first name is {first}. My last name is {last}. My favorite color is {favColor} and my favorite meal is {favMeal}".format(first = "fernando", last = "duenas", favColor = "blue", favMeal = "BBQ")
print("Argument by Name ===> ",argByName)

# 4. Submit a file named Activity4-YourName with the appropriate pythin extension to Populi, Slack and Email. 


