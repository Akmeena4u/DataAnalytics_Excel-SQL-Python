import random
import re  # Import the regular expressions module

# Set initial values
guesses = 0

while True:
    # Ask for the login ID
    login_id = input("Enter your 6-digit  login ID: ")

    # Check if the login ID matches the pattern (6 alphanumeric characters)
    if re.match("^[a-zA-Z0-9]{6}$", login_id):
        print("Login successful! Let's play.")
    else:
        print("Invalid login ID. Please enter a 6-digit alphanumeric ID.")
        continue

    # Choose a difficulty level
    difficulty = input("Choose a difficulty level (easy, medium, hard): ")

    if difficulty == "easy":
        top_of_range = 10
        max_guesses = 3
    elif difficulty == "medium":
        top_of_range = 50
        max_guesses = 7
    elif difficulty == "hard":
        top_of_range = 100
        max_guesses = 10
    else:
        print("Invalid difficulty level. Please choose from easy, medium, or hard.")
        continue

    # Generate a random number
    random_number = random.randint(0, top_of_range)
    print(f"Guess a number between 0 and {top_of_range}.")

    # Start the guessing loop
    while guesses < max_guesses:
        guesses += 1
        user_guess = input("Make a guess: ")

        if user_guess.isdigit():
            user_guess = int(user_guess)
            if user_guess > top_of_range:
                print('Please guess a number within the range.')
                continue
        else:
            print('Please type a number next time.')
            continue

        if user_guess == random_number:
            print("You got it!")
            break
        elif user_guess > random_number:
            print("You were above the number!")
        else:
            print("You were below the number!")

    if guesses >= max_guesses:
        print(f"Sorry, you've reached the maximum number of guesses ({max_guesses}). The number was {random_number}.")

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == "yes":
        guesses = 0
    else:
        print("Thanks for playing!")
        break

