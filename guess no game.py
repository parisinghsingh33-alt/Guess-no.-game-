import random

def choose_difficulty():
    print("\nChoose Difficulty Level:")
    print("1. Easy   (1 to 50)")
    print("2. Medium (1 to 100)")
    print("3. Hard   (1 to 500)")

    while True:
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            return 50
        elif choice == "2":
            return 100
        elif choice == "3":
            return 500
        else:
            print("Invalid choice! Please select 1, 2, or 3.")


def play_game():
    maximum = choose_difficulty()
    secret_number = random.randint(1, maximum)
    attempts = 0

    print(f"\nGuess the number between 1 and {maximum}!")

    while True:
        try:
            guess = int(input("Enter your guess: "))

            if guess < 1 or guess > maximum:
                print(f"Please enter a number between 1 and {maximum}.")
                continue

            attempts += 1

            if guess < secret_number:
                print("Too low! Try a higher number.")

            elif guess > secret_number:
                print("Too high! Try a lower number.")

            else:
                print("\nCongratulations! You guessed correctly!")
                print("The secret number was:", secret_number)
                print("Total attempts:", attempts)
                return attempts

        except ValueError:
            print("Invalid input! Please enter a whole number.")


def main():
    best_score = None

    print("===== NUMBER GUESSING GAME =====")

    while True:
        attempts = play_game()

        if best_score is None or attempts < best_score:
            best_score = attempts
            print("New best score!")

        print("Best score (lowest attempts):", best_score)

        replay = input("\nDo you want to play again? (yes/no): ")
        if replay.lower() not in ["yes", "y"]:
            print("\nThank you for playing!")
            print("Your best score was:", best_score, "attempts.")
            break


# Start the game
main()