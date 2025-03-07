import random

def number_guessing_game():
    secret_numnber = random.randint(1, 100)
    attempts = 0
    print("Guess the number between 1 and 100!")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts +=1

            if guess < secret_numnber:
                print("Too low! Try again.")
            elif guess > secret_numnber:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    number_guessing_game()