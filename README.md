# Fibonacci Sequence in Python

## Description
This Python script generates a Fibonacci sequence of a specified length, input by the user. The sequence is built by adding the last two numbers to produce the next one.

## Overview
1. **User Input**: 
   - The script prompts the user to enter the number of terms they want in the Fibonacci sequence.
2. **Sequence Generation**:
   - The script initializes two variables, `number1` and `number2`, to 0 and 1, respectively.
   - Using a loop, the script alternates between updating `number1` and `number2` to produce the next number in the Fibonacci sequence.
   - For even positions, `number1` is updated by adding `number2` to it.
   - For odd positions, `number2` is updated by adding `number1` to it.
   - The updated number is printed in each iteration of the loop.
3. **Output**:
   - The script prints each number in the Fibonacci sequence until the sequence reaches the user-specified length.

## Output
- **After running the script, you will see**:
    - The Fibonacci sequence printed line by line up to the number of terms specified by the user.

## Code
```python
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
```

## Example

```
Enter Number of Range: 5
1
2
3
5
8
```

## Key
- [Description](#description)
- [Overview](#overview)
- [Output](#output)
- [Code](#Code)
- [Example](#Example)

---

This README should provide clear instructions and explanations for anyone using or reviewing the code.
