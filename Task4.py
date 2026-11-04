original_price = int(input("Enter original price: "))
discount_percentage = int(input("Enter discount percentage: "))

discount_amount = original_price * discount_percentage / 100

final_price = original_price - discount_amount

print("\n==== RESULT ====")
print(f"Discount Amount: {discount_amount}")
print(f"Final Price after Discount: {final_price}")