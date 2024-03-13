def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.
    
    Args:
    - price: The original price of the item.
    - discount_percent: The discount percentage to be applied.
    
    Returns:
    - The final price after applying the discount if the discount is 20% or higher,
      otherwise returns the original price.
    """
    if discount_percent >= 20:  # Check if the discount is 20% or higher
        discounted_price = price - (price * discount_percent / 100)  # Calculate the discounted price
        return discounted_price
    else:
        return price  # Return the original price if discount is less than 20%

# Prompting user to enter original price and discount percentage
original_price = float(input("Enter the original price of the item: $"))
discount_percentage = float(input("Enter the discount percentage: "))

# Calculating the final price after applying the discount
final_price = calculate_discount(original_price, discount_percentage)

# Displaying the final price
print(f"The final price after applying the discount is: ${final_price:.2f}")
