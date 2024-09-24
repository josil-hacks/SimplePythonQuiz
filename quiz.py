"""The following code was written by John Silvell
This program will be a small litle quiz about some basic computer science."""

#When the program starts the points shall be set to zero
points = int(0)

# Introduction to the user
print("=== WELCOME TO MY QUIZ ===")
print()
print("You will be asked 5 questions about some basic computer knowledge. For each correct answer you will be given a point.")
print("Please be careful when you write your answer as the computer cannot recognise misspellings.")
print()

# For a more personal experience, the program will ask the user for their name
print("But before we get started I do want to know your name...")
username = input("What is your name?: ")
print()
print("Nice to meeting you, " + username +"! Let us get started!")
print()
print()
print()

# This is where the acutal quiz begins and here is question no. 1
print("1. Who is the founder of Microsoft?")
print()
answer1 = input("Your answer: ")
print()
print()

# If the user answers correct, the variable points will increase by 1. 
if answer1 == "Bill Gates" or answer1 == "bill gates":
    points = int(+1)
    print(points)
    print("Correct!")
    print()
else:
    print(points)
    print("Incorrect")
    
# Question no. 2
print("2. Who devloped the open source operating system, Linux?")
print()
answer2 = input("Your answer: ")
print()
print()

# If the user answers correct, the variable points will increase by 1. 
if answer2 == "Linus Torvalds" or answer2 == "linus torvalds":
    points = int(+1)
    print(points)
    print("Correct!")
    print()
elif answer2 == "Linus Torvald" or answer2 == "linus torvald":
    points = int(+1)
    print(points)
    print("Almost correct but I am being nice by giving you a point anyway.")
    print()
else:
    print(points)
    print("Incorrect")