# Fibonacci Sequence

# Initialize Variables
number1 = 0  # First number in the sequence
number2 = 1  # Second number in the sequence
counter = 0  # Counter to keep track of iterations

# Get user input for the number of terms in the sequence
end = int(input("Enter Number of Range: "))

# Loop until the counter reaches the user-defined limit (end)
while counter < end:
    # Check if the current position (counter) is even
    if counter % 2 == 0:
        number1 += number2  # Update number1 with the sum of number1 and number2
        print(number1)      # Print the updated number1
    else:
        number2 += number1  # Update number2 with the sum of number1 and number2
        print(number2)      # Print the updated number2
    
    counter += 1  # Increment the counter to move to the next position
