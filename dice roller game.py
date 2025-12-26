import random

# Dice faces as strings (ASCII art)
DICE_FACES = {
    1: ["┌─────┐",
        "│     │",
        "│  ●  │",
        "│     │",
        "└─────┘"],
    2: ["┌─────┐",
        "│ ●   │",
        "│     │",
        "│   ● │",
        "└─────┘"],
    3: ["┌─────┐",
        "│ ●   │",
        "│  ●  │",
        "│   ● │",
        "└─────┘"],
    4: ["┌─────┐",
        "│ ● ● │",
        "│     │",
        "│ ● ● │",
        "└─────┘"],
    5: ["┌─────┐",
        "│ ● ● │",
        "│  ●  │",
        "│ ● ● │",
        "└─────┘"],
    6: ["┌─────┐",
        "│ ● ● │",
        "│ ● ● │",
        "│ ● ● │",
        "└─────┘"]
}


dice=int(input("How many dice?"))



dice_count=[]
for dice in range(dice):
    num=random.randint(1,6)
    dice_count.append(num)
print(dice_count)

for dice in dice_count:
    for dice in DICE_FACES.get(dice):
     print(dice)

total=sum(dice_count)
print(total)


# # Roll six dice
# dice_values = [random.randint(1, 6) for _ in range(6)]

# # Print dice with boxes side by side
# print("🎲 Dice Roll Results:\n")
# for row in range(5):  # each dice has 5 rows
#     row_str = ""
#     for value in dice_values:
#         row_str += DICE_FACES[value][row] + "  "  # spacing between dice
#     print(row_str)

# # Show numeric values
# print("\nDice values:", dice_values)
