number=int(input("Enter number between 1-20:"))

while number<0 or number>20:
    print(f" {number} is not valid")
    number=int(input("Enter number between 1-20:"))

print(f"Your number is {number}")