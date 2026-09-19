import os


# ================= UTIL =================

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


# ================= MENU =================

MENU = {
    "Pizza": {
        "Margherita": 15,
        "Pepperoni": 18,
        "Quattro Formaggi": 20,
        "BBQ Chicken": 22,
        "Diavola": 21
    },
    "Drinks": {
        "Coca-Cola": 4,
        "Fanta": 4,
        "Sprite": 4,
        "Water": 2
    },
    "Sides": {
        "Garlic Bread": 7,
        "Chicken Wings": 12,
        "French Fries": 8
    }
}


# ================= FUNCTIONS =================

def show_menu():
    print("\n" + "=" * 40)
    print("            PYTHON PIZZA")
    print("=" * 40)

    for category, items in MENU.items():

        print(f"\n--- {category} ---")

        for item, price in items.items():
            print(f"{item:<25} ${price:.2f}")

    print("=" * 40)


def find_item(item_name):

    for category in MENU.values():

        for item, price in category.items():

            if item.lower() == item_name.lower():
                return item, price

    return None, None


# ================= START =================

clear_screen()

print("=" * 40)
print("      WELCOME TO PYTHON PIZZA!")
print("=" * 40)

show_menu()

order = []
subtotal = 0


# ================= ORDER =================

while True:

    print("\nWhat would you like to order?")
    print("Type the item name or type 'done' to finish.")

    item_input = input("Your choice: ").strip()

    if item_input.lower() == "done":
        break

    item, price = find_item(item_input)

    if item is None:
        print("❌ We don't have that item on the menu.")
        continue

    quantity_input = input(
        f"How many {item} would you like? "
    )

    if not quantity_input.isdigit() or int(quantity_input) <= 0:

        print("❌ Please enter a valid quantity.")
        continue

    quantity = int(quantity_input)

    total_item_price = price * quantity

    order.append({
        "name": item,
        "quantity": quantity,
        "price": price,
        "total": total_item_price
    })

    subtotal += total_item_price

    print(f"✓ Added {quantity}x {item} to your order.")
    print(f"  Price: ${total_item_price:.2f}")


# ================= EMPTY ORDER =================

if not order:

    clear_screen()

    print("You didn't order anything.")
    print("Thank you for visiting Python Pizza!")

    input("\nPress Enter to exit...")
    exit()


# ================= DELIVERY =================

clear_screen()

print("=" * 40)
print("             DELIVERY")
print("=" * 40)

print("1. Pickup")
print("2. Standard Delivery - $3")
print("3. Express Delivery - $6")

while True:

    delivery_choice = input(
        "\nChoose delivery option: "
    )

    if delivery_choice == "1":

        delivery_type = "Pickup"
        delivery_fee = 0
        break

    elif delivery_choice == "2":

        delivery_type = "Standard Delivery"
        delivery_fee = 3
        break

    elif delivery_choice == "3":

        delivery_type = "Express Delivery"
        delivery_fee = 6
        break

    else:

        print(
            "❌ Invalid choice. "
            "Please choose 1, 2 or 3."
        )


# ================= PAYMENT =================

clear_screen()

print("=" * 40)
print("              PAYMENT")
print("=" * 40)

print("1. Cash")
print("2. Card")
print("3. PayPal")

while True:

    payment_choice = input(
        "\nChoose payment method: "
    )

    if payment_choice == "1":

        payment_method = "Cash"
        break

    elif payment_choice == "2":

        payment_method = "Card"
        break

    elif payment_choice == "3":

        payment_method = "PayPal"
        break

    else:

        print(
            "❌ Invalid choice. "
            "Please choose 1, 2 or 3."
        )


# ================= FINAL BILL =================

total = subtotal + delivery_fee

clear_screen()


# ================= RECEIPT =================

print("=" * 50)
print("                 PYTHON PIZZA")
print("=" * 50)

print("\nYOUR ORDER")
print("-" * 50)

for item in order:

    print(
        f"{item['quantity']}x "
        f"{item['name']:<25} "
        f"${item['total']:.2f}"
    )

print("-" * 50)

print(
    f"{'Subtotal:':<37}"
    f"${subtotal:.2f}"
)

print(
    f"{'Delivery:':<37}"
    f"${delivery_fee:.2f}"
)

print("-" * 50)

print(
    f"{'TOTAL:':<37}"
    f"${total:.2f}"
)

print("\nORDER DETAILS")
print("-" * 50)

print(f"Delivery: {delivery_type}")
print(f"Payment:  {payment_method}")

print("\n" + "=" * 50)

print("        🍕 THANK YOU FOR YOUR ORDER! 🍕")

print("=" * 50)


# ================= KEEP PROGRAM OPEN =================

input("\nPress Enter to exit...")