def number ():
    a= int(input("Enter your number "))
    b= int(input("Enter your number"))
    c=int(input("Enter your number"))

    if (a>=b) and (a>=c):
        return(a)
    elif (b>=a) and (b>=c):
        return(b)
    
    else:
        return(c)    

print(f"The greatest three digit number is:{number()}")            