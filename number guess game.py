import random

print("🎯 Welcome to the Number Guessing Game! 🎯")
print("-----------------------------------------\n")


while True:
    try:
        lower = int(input("Set the LOWER bound: "))
        higher = int(input("Set the HIGHER bound: "))
        if lower >= higher:
            print("⚠️  Higher bound must be greater than lower bound. Try again.\n")
        else:
            break
    except ValueError:
        print("⚠️  Please enter valid integers.\n")

print(f"\nGreat! I'm thinking of a number between {lower} and {higher}. Let's start!\n")


num = random.randint(lower, higher)
total_guess = 0

# Game loop
while True:
    try:
        user_guess = int(input("Enter your guess: "))
        total_guess += 1

        if user_guess == num:
            print(f"🎉 Congratulations! You guessed the correct number: {num}")
            print(f"💡 Total attempts: {total_guess}")
            break
        elif user_guess > num:
            print("⬇️  Number is LOWER than your guess.\n")
        else:
            print("⬆️  Number is HIGHER than your guess.\n")

    except ValueError:
        print("⚠️  Please enter a valid integer.\n")

print("\nThanks for playing! 🎲")
