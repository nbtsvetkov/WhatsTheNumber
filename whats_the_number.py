import random

computer_number = random.randint(1, 100)
tries = 0
difficulty = ""
points = 0
games = 0
wins = 0
losses = 0
new_game = True
another_game = "Do you want to play another game?\n 1. Yes \n 2. No "
select_level = "Please, select a level:\n 1. Easy\n 2. Medium\n 3. Hard\n "




while True:


    if new_game:
        user_command = input(select_level)
        games += 1

        if user_command == "1":
            tries = 10
            difficulty = "Easy"
            print(f"You have selected the {difficulty} difficulty!\nYou have {tries} chances to guess the number!")
        elif user_command == "2":
            tries = 8
            difficulty = "Medium"
            print(f"You have selected the {difficulty} difficulty!\nYou have {tries} chances to guess the number!")
        elif user_command == "3":
            tries = 5
            difficulty = "Hard"
            print(f"You have selected the {difficulty} difficulty!\nYou have {tries} chances to guess the number!")
        elif user_command == "exit":
            break

    if tries == 0:
        print(f"Sorry, you don't have any more tries!")
        losses += 1
        user_command = input(another_game)
        new_game = False

        if user_command == "2" or user_command == "exit":
            print(f"Sorry to see you leave! Bye!\nSTATS\nGAMES:{games}\nWINS:{wins}\nLOSSES:{losses}")
            break
        else:
            computer_number = random.randint(1, 100)
            tries = 6
            difficulty = ""
            new_game = True
            continue

    user_guess = input(f"Guess a number between 1 and 100: ")

    if not user_guess.isdigit():
        print("Sorry, you should only enter numbers between 1 and 100")
        new_game = False
        continue
    else:
        user_number = int(user_guess)
        tries -= 1
        if user_number > computer_number:
            print(f"Too High! You have {tries} left!")
            new_game = False
            continue
        elif user_number < computer_number:
            print(f"Too low! You have {tries} left!")
            new_game = False
            continue
        else:
            wins += 1
            print(f"You guessed the number in {tries} tries! CONGRATULATIONS!\nSTATS\nGAMES:{games}\nWINS:{wins}\nLOSSES:{losses}")
            user_command = input(another_game)
            if user_command == "2":
                new_game = False
                print(f"Sorry to see you leave! Bye!\nSTATS\nGAMES:{games}\nWINS:{wins}\nLOSSES:{losses}")
                break
            elif user_command == "1":
                new_game = True
            continue
