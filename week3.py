def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.
    Only applies the discount if it is 20% or higher.
    
    Parameters:
    - price (float): The original price of the item.
    - discount_percent (float): The discount percentage.
    
    Returns:
    - float: The final price after discount (if applicable).
    """
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        return price - discount_amount
    else:
        return price

# Prompt user for input
try:
    original_price = float(input("Enter the original price: "))
    discount = float(input("Enter the discount percentage: "))

    # Calculate final price
    final_price = calculate_discount(original_price, discount)

    # Output result
    if discount >= 20:
        print(f"Discount applied. Final price: ${final_price:.2f}")
    else:
        print(f"No discount applied. Final price: ${original_price:.2f}")

except ValueError:
    print("Please enter valid numeric values for price and discount.")
