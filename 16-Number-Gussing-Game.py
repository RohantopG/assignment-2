#here i have user the random module at first i didnt understnad then i saw some tutorila in udemy and understood and solved it

import random

while True:
    print("\n Number gussing games")
    print("Guess the number between 1 and 100")
    
    secret_number = random.randint(1, 100)
    attempts = 7
    used_attempts = 0

    while attempts > 0:
        guess = int(input("\nEnter your guess: "))
        used_attempts += 1
        attempts -= 1

        if guess == secret_number:
            print(f" You guessed it in {used_attempts} attempts.")
            break
        elif guess > secret_number:
            print("Too High!")
        else:
            print("Too Low!")

        if attempts > 0:
            print("Attempts remaining:", attempts)
        else:
            print("\n Game Ended!")
            print("The correct number was:", secret_number)

    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    
    if play_again != "yes":
        print("bye")
        break
