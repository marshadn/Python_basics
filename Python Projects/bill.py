

def calculate_total_bill(item_price, quantity=1):                       
    # Calculate the total cost without any discounts
    total_cost = item_price * quantity

    # Apply a discount for bulk purchases
    # If the quantity is 10 or more, apply a 10% discount``
    if quantity >= 10:
        discount=(100-10)/100
        total_cost *= discount  # 10% discount(discount=100%-10%=90% --> 90/100=0.9)
 # Apply a 5% discount for items priced above ₹100
    if item_price > 100:
        discount=(100-5)/100
        total_cost *= discount  # 5% discount(discount=100%-5%=95% --> 95/100=9.5)
 # Return the total cost after applying discounts
    return total_cost

# Create a shopping cart with item prices and quantities
shopping_cart = [
    {"item_price": 25.0, "quantity": 3},
    {"item_price": 120.0, "quantity": 2},
    {"item_price": 8.0, "quantity": 12},
] 

# Calculate the total bill for the shopping cart using a loop
total_bill = 0.0

# Loop through shopping_cart
for item in shopping_cart:
    item_price = item["item_price"]
    quantity = item["quantity"]
    # Calculate the total cost for the current item
    item_total = calculate_total_bill(item_price, quantity)
    # Add the item total to the overall bill
    total_bill += item_total

# Print the total bill for the customer
print(f"Total Bill: ₹{total_bill}")
