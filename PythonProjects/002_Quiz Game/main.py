import re

ID = input("Enter Application ID: ")

# Check if the name is a 6-digit alphanumeric value
if not re.match(r'^[a-zA-Z0-9]{6}$', ID):
    print("Invalid Application ID. Please enter a 6-digit alphanumeric ID.")
else:
    print("Welcome to the objective round placement Quiz!")

    playing = input("Do you want to start the Quiz? (yes/no): ")

    if playing.lower() != "yes":
        quit()

    print("Okay! Let's Start :)")
    score = 0

    answer = input("Which programming language is known for its use in data analysis and scientific computing? ")
    if answer.lower() == "python":
        print('Correct!')
        score += 1
    else:
        print("Incorrect!")

    answer = input("What does 'HTTP' stand for in the context of web addresses? ")
    if answer.lower() == "Hypertext Transfer Protocol":
        print('Correct!')
        score += 1
    else:
        print("Incorrect!")

    answer = input("What is the primary programming language used for web development on the client side? ")
    if answer.lower() == "javascript":
        print('Correct!')
        score += 1
    else:
        print("Incorrect!")

    answer = input('What does "CEO" stand for in the business world? ')
    if answer.lower() == "chief executive officer":
        print('Correct!')
        score += 1
    else:
        print("Incorrect!")

    answer = input("What is the time complexity of binary search in a sorted array of n elements? ")
    if answer.lower() == "o(log n)":
        print('Correct!')
        score += 1
    else:
        print("Incorrect!")

    answer = input("What does OOP stand for in the context of programing paradigm? ")
    if answer.lower() == "object oriented programming":
        print('Correct!')
        score += 1
    else:
        print("Incorrect!")

    answer = input("What does SQL stand for in the context of databases? ")
    if answer.lower() == "structured query language":
        print('Correct!')
        score += 1
    else:
        print("Incorrect!")

    answer = input('In programming, what does "API" stand for? ')
    if answer.lower() == "application programming interface":
        print('Correct!')
        score += 1
    else:
        print("Incorrect!")

    answer = input("What is a data structure commonly used for implementing a Last-In-First-Out (LIFO) behavior? ")
    if answer.lower() == "stack":
        print('Correct!')
        score += 1
    else:
        print("Incorrect!")

    answer = input("Which data structure follows the FIFO (First-In-First-Out) principle for data retrieval? ")
    if answer.lower() == "queue":
        print('Correct!')
        score += 1
    else:
        print("Incorrect!")

    print("You got " + str(score) + " questions correct!")
    print("You got " + str((score / 10) * 100) + "%.")
   
    if score >= 7:
        print("Congratulations! You are selected for the next round.")
    else:
        print("Better luck next time. Please prepare well for future opportunities.")
