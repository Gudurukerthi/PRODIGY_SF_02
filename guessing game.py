import random

def guess_number():
    # Generate a random number between 1 and 100
    random_number = random.randint(1, 100)
    attempts = 0

    while True:
        # Prompt the user to guess a number
        guess = int(input("Guess a number between 1 and 100: "))
        attempts += 1

        # Check if the guess is correct
        if guess == random_number:
            print(f"Congratulations! You guessed the number {random_number} correctly in {attempts} attempts.")
            break
        elif guess < random_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

def main():
    play_again = "y"
    while play_again.lower() == "y":
        guess_number()
        play_again = input("Do you want to play again? (y/n): ")

if __name__ == "__main__":
    main()
