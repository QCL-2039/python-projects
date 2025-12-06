print("\n🛒 Welcome to Our Shop!\n")

customer_cart = []
prices = []
total_price = 0

while True:
    food = input("Enter the food name to buy (Press Q to quit): ")

    if food.strip().lower() == "q":
        break
    else:
        # Price input
        price = float(input(f"Enter the price of '{food}': $"))
        
        customer_cart.append(food)
        prices.append(price)
        print(f"👉 Added '{food}' to your cart.\n")

print("\n==============================")
print("🧾 Your Cart Summary")
print("==============================")

for i, item in enumerate(customer_cart):
    print(f"{i+1}. {item} - ${prices[i]}")

total_price = sum(prices)

print("------------------------------")
print(f"💰 Total Price: ${total_price}")
print("==============================\n")

print("✅ Thank you for shopping with us!")
