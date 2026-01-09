import random

# ------------------------
# SLOT FUNCTIONS
# ------------------------

def spin_row():
    symbols = ["🥂", "🍉", "🍊", "🍇", "🍰"]
    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print(" | ".join(row))
    print()

def get_payout(row, bet):
    # All symbols match
    if row[0] == row[1] == row[2]:
        if row[0] == "🥂":
            return bet * 5
        elif row[0] == "🍰":
            return bet * 4
        elif row[0] == "🍇":
            return bet * 3
        else:
            return bet * 2
    else:
        return 0

# ------------------------
# MAIN GAME
# ------------------------

def main():
    print("🎰 Welcome to Python Slot Machine 🎰\n")

    while True:
        try:
            balance = int(input("Enter your starting balance: "))
            if balance <= 0:
                print("Balance must be greater than 0.\n")
            else:
                break
        except ValueError:
            print("Please enter a valid number.\n")

    print("\n💡 Match all 3 symbols to win!")
    print("Type 'q' anytime to quit.\n")

    while balance > 0:
        print(f"💰 Current balance: {balance}")

        bet = input("Enter your bet amount: ")

        if bet.lower() == "q":
            break

        try:
            bet = int(bet)
            if bet <= 0:
                print("Bet must be greater than 0.\n")
                continue
            if bet > balance:
                print("❌ Insufficient balance!\n")
                continue
        except ValueError:
            print("❌ Enter a valid number.\n")
            continue

        balance -= bet

        row = spin_row()
        print("\n🔄 Spinning...\n")
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f"🎉 You won {payout}!")
            balance += payout
        else:
            print("😢 No match. Try again!")

        print()

    print("\n🏁 Game Over!")
    print(f"💰 Final balance: {balance}")
    print("Thanks for playing! 🙏")

# ------------------------
# RUN GAME
# ------------------------

if __name__ == "__main__":
    main()
