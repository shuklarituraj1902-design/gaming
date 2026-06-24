import random


def main():
    secret_number = random.randint(1, 100)
    attempts = 0
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        guess_input = input("Enter your guess: ")
        if not guess_input.isdigit():
            print("Please enter a valid integer between 1 and 100.")
            continue

        guess = int(guess_input)
        if guess < 1 or guess > 100:
            print("Your guess must be between 1 and 100.")
            continue

        attempts += 1

        if guess < secret_number:
            print("Too low. Try again.")
        elif guess > secret_number:
            print("Too high. Try again.")
        else:
            print(f"Correct! You guessed the number in {attempts} attempts.")
            break

    print("Thanks for playing!")


if __name__ == "__main__":
    main()
