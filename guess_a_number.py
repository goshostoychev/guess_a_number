from random import randint


computer_number = randint(1, 100)

while True:
    player_input = input("Guess the number: ")

    if not player_input.isdigit():
        print("Invalid input. Try again...")
        continue

    player_number = int(player_input)

    if player_number == computer_number:
        print("You guessed it!")
        break
    elif player_number > computer_number:
        print("Your number is too high!")
    else:
        print("Your number is too low!")

        