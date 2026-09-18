#Create variables for a product's name, price, quantity, and discount percentage.
#  Calculate and store the final price after discount using only variables and arithmetic operators.

products_name= input("Enter the product name : ")
price = int(input("Enter the price of product: "))
quantity = int(input("Enter the quantity of products you want: "))
discount_percentage = float(input("Enter the discount rate: "))


discount_amount =(price* discount_percentage/100)
original_price = (price - discount_amount)* quantity
print(f"The price of this product is : {original_price}")