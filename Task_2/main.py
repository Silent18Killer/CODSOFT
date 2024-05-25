                                # CALCULATOR

'''
    Design a simple calculator with basic arithmetic operations.
    Prompt the user to input two numbers and an operation choice.
    Perform the calculation and display the result.
'''

def calculator():
    print("Simple Calculator")
    print("Select operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    
    while True:
    
        operation = input("Enter choice (1/2/3/4) : ")
        
        if operation in ('1', '2', '3', '4'):
            
            try:
                num1 = float(input("Enter first number : "))
                num2 = float(input("Enter second number : "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
            
            
            if operation == '1':
                result = num1 + num2
                print(f"The result of {num1} + {num2} is: {result}")
            elif operation == '2':
                result = num1 - num2
                print(f"The result of {num1} - {num2} is: {result}")
            elif operation == '3':
                result = num1 * num2
                print(f"The result of {num1} * {num2} is: {result:.2f}")
            elif operation == '4':
                if num2 != 0:
                    result = num1 / num2
                    print(f"The result of {num1} / {num2} is: {result:.2f}")
                else:
                    print("Error: Division by zero is not allowed.")
                
            next_calculation = input("Let's do the next calculation? (yes/no): ") 
            if next_calculation == "no":
                break
                    
        else:
            print("Invalid Input")


calculator()