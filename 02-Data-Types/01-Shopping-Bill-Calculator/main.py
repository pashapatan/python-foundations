
print("Welcome to the Shopping Bill Calculator!")

product_name = input("What is the product name? ")
price = float(input("What is the price? $"))
quantity = int(input("How many do you want? "))
discount_percentage = int(input("What is the discount percentage? "))

total_cost = price * quantity
discount_amount = (discount_percentage * total_cost) / 100
final_amount = total_cost - discount_amount

print("\n----- BILL -----")
print(f"Product: {product_name}")
print(f"Price: ${price:.2f}")
print(f"Quantity: {quantity}")
print(f"Discount: {discount_percentage}%")
print(f"\nSubtotal: ${total_cost:.2f}")
print(f"Discount Amount: ${discount_amount:.2f}")
print(f"Final Total: ${final_amount:.2f}")
