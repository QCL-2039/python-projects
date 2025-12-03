print("🍔 Welcome to Our Food Shop! 🍕")
print("--------------------------------------\n")

foods = {
    "Burger": 150,
    "Pizza": 350,
    "Pasta": 200,
    "Sandwich": 120,
    "French Fries": 90,
    "Chicken Wings": 220,
    "Grilled Chicken": 300,
    "Beef Steak": 550,
    "Fried Rice": 180,
    "Biriyani": 250,
    "Kebab": 140,
    "Shawarma": 160,
    "Hotdog": 100,
    "Noodles": 130,
    "Soup": 110,
    "Salad": 90,
    "Ice Cream": 80,
    "Milkshake": 150,
    "Coffee": 70,
    "Tea": 40
}

# Show menu
print("📋 Here are the available foods:\n")
for item, price in foods.items():
    print(f"{item:20} : {price} tk")

print("\n--------------------------------------")
print("🛒 Start adding items to your cart!")
print("Type 'q' anytime to checkout.\n")

food_cart = []
total_price = 0

while True:
    food = input("👉 Enter your food name (q to quit): ").strip()

    if food.lower() == "q":
        break

    food_name = food.title()

    if food_name in foods:
        food_cart.append(food_name)
        total_price += foods[food_name]
        print(f"✔️ Added {food_name} ({foods[food_name]} tk)\n")
    else:
        print(f"❌ '{food}' is not in our shop. Please try again.\n")

# Checkout summary
print("\n========== 🧾 Your Order Summary ==========")

if len(food_cart) == 0:
    print("Your cart is empty.")
else:
    for item in food_cart:
        print(f"- {item} : {foods[item]} tk")

    print("--------------------------------------")
    print(f"💰 Total Price: {total_price} tk")

print("\n🙏 Thank you for shopping with us!")


#emojis are taken from chatgpt