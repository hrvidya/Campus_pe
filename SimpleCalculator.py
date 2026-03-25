# Calculator Program
#Using try and except just to handle edge cases
try:
    #Take user input
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    #operations
    print("\n Results:")
    print("Addition:",a+b)
    print("Subtraction:",a-b)
    print("Multiplication:",a*b)
    print("Exponentiation:",a**b)
    #Condition for Division and Modulus as it gives ZeroDivisionError
    if b != 0:
        print("Division:",a/b)
        print("Modulus:",a%b)
    else:
        print("Division: Cannot divide by zero")
        print("Modulus: Cannot modulus by zero")

except ValueError:
    print("Invalid input! Please enter numbers only.")