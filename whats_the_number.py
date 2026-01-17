import random

computer_number = random.randint(1, 100)

while True:
    user_number = input("Please, enter your guess(1-100): ")

    if not user_number.isdigit():
        print("Sorry, you should only enter numbers between 1 and 100")
        continue
    else:
        user_number = int(user_number)
        if user_number > computer_number:
            print("Lower!")
            continue
        elif user_number < computer_number:
            print("Higher!")
        else:
            print("You guessed it! CONGRATULATIONS!")
            break