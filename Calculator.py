import re  # Import the 're' module to use regular expressions

# Start an infinite loop to keep asking the user for operations
while True:
    # Ask the user for the operation or to exit
    operation = input("What is the operation? (e.g. 5 + 3) or type 'exit' to quit: ")
   
# If the user types 'exit', break the loop and end the program
    if operation.lower() == 'exit':
        print("Goodbye!")
        break

# If the input matches the expected pattern
    count = re.search(r"(\d+)\s*([\+\-\*/])\s*(\d+)", operation)

    if count:
        a = int(count.group(1))  # Get the first number
        b = count.group(2)   # Get the operator
        c = int(count.group(3))  # Get the second number

# Executing the operation based on the chosen operator
        if b == "+":
            result = a + c
        elif b == "-":
            result = a - c
        elif b == "*":
            result = a * c
        elif b == "/":
            if c == 0:
                print("Error: Division by zero is not allowed.")
                continue
            result = a / c
        #  # If the operator is not recognised
        
        else:
            print("Operator not recognised.")
            continue

        print(f"The result is: {result}")
    # # If the input doesn't match the expected format
    else:
        print("This operation is allowed only for numbers.")
