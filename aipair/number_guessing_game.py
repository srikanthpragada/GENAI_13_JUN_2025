import random

def number_guessing_game():
    secret_number = random.randint(1, 25)
    attempts = 3
    print("Welcome to the Number Guessing Game!")
    print("Guess the number between 1 and 25. You have 3 attempts.")
    
    for attempt in range(1, attempts + 1):
        try:
            guess = int(input(f"Attempt {attempt}: Enter your guess: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue
        if guess == secret_number:
            print(f"Congratulations! You guessed the number {secret_number} correctly.")
            break
        elif guess < secret_number:
            print("Too low!")
        else:
            print("Too high!")
    else:
        print(f"Sorry, you've used all attempts. The number was {secret_number}.")

if __name__ == "__main__":
    number_guessing_game()
