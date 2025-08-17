Discount Calculator

This is a simple Python program that calculates the final price of an item after applying a discount only if the discount is 20% or more.

 Features

Prompts the user for:

The original price of an item

The discount percentage

Applies the discount only if it's 20% or more

Displays the final price after applying the discount, or the original price if the discount is too small

 How It Works

The program includes a function:

def calculate_discount(price, discount_percent)


This function:

Applies the discount if discount_percent >= 20

Returns the discounted price

Otherwise, returns the original price

 Usage
1. Run the Program

Make sure you have Python installed, then run the script:

python discount_calculator.py

2. Enter Input When Prompted

Example:

Enter the original price: 100
Enter the discount percentage: 25
Discount applied. Final price: $75.00


If the discount is less than 20%:

Enter the original price: 100
Enter the discount percentage: 10
No discount applied. Final price: $100.00

 Requirements

Python 3.x

No external libraries are needed.

 Error Handling

The program checks for invalid input (non-numeric values) and prompts the user with a simple error message.
 License

This project is free to use and modify. No license is specified.
