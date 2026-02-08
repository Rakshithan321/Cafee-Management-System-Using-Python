import datetime

# 🟢 WELCOME MESSAGE
print("=" * 50)
print("🍽️  WELCOME TO RAKRISH RESTAURANT  🍽️")
print("Serving delicious food made with love ❤️")
print("Open Hours: 10 AM – 10 PM |")
print("=" * 50)

# Optional pause so welcome message is visible
input("👉 Press Enter to view the menu...")

# 🧾 MENU
menu = {
    "pizza": 100,
    "burger": 80,
    "sandwich": 60,
    "coffee": 40,
    "tea": 20,
    "fries": 50,
    "ice cream": 70
}

# 📋 Display Menu
print("\n📋 TODAY'S MENU")
print("-" * 40)
for item, price in menu.items():
    print(f"{item.capitalize():<20} Rs{price}")
print("-" * 40)

# 🛒 Take Orders
orders = {}

while True:
    item = input("\nEnter item to order (or type 'done' to finish): ").lower().strip()

    if item == "done":
        break

    if item not in menu:
        print("❌ Sorry, that item is not available.")
        continue

    try:
        qty = int(input(f"Enter quantity for {item.capitalize()}: "))
        if qty <= 0:
            print("⚠️ Quantity must be greater than 0.")
            continue
    except ValueError:
        print("⚠️ Invalid quantity.")
        continue

    # Add to orders
    if item in orders:
        orders[item] += qty
    else:
        orders[item] = qty

    print(f"✅ Added {qty} x {item.capitalize()} to your order.")

# 🧾 BILL
if not orders:
    print("\n🛑 You did not order anything.")
else:
    print("\n🧾 FINAL BILL")
    print("-" * 50)
    print(f"{'Item':<20}{'Qty':<5}{'Price'}")
    print("-" * 50)

    subtotal = 0
    for item, qty in orders.items():
        price = menu[item] * qty
        subtotal += price
        print(f"{item.capitalize():<20}{qty:<5}Rs{price}")

    gst = round(subtotal * 0.05, 2)
    discount = round((subtotal + gst) * 0.10, 2) if subtotal >= 300 else 0
    total = round(subtotal + gst - discount, 2)

    print("-" * 50)
    print(f"{'Subtotal':<30}Rs{subtotal:.2f}")
    print(f"{'GST (5%)':<30}Rs{gst:.2f}")
    print(f"{'Discount (10%)':<30}-Rs{discount:.2f}")
    print(f"{'Total Amount':<30}Rs{total:.2f}")
    print(f"{'Date & Time':<30}{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 50)
    print("🙏 Thank you for visiting Rakrish Restaurant! Come again! 😊")

