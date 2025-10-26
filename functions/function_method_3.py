# Function with Parameters and Arguments

'''A parameter is the variable listed inside the parentheses in the function definition.
An argument is the actual value that is sent to the function when it is called.'''

# Define a function to add two numbers
def add(x, y):
    z = x + y              # Add x and y, store the result in z
    return z               # Return the result to the caller

# Define a function to subtract two numbers
def sub(x, y):
    z = x - y              # Subtract y from x
    print("subtraction is ", z)  # Print the subtraction result

# Take first number input from user
val1 = int(input("Enter value 1= "))   # Convert input string to integer
# Take second number input from user
val2 = int(input("Enter value 2= "))

# Call the add() function and store its returned value in r_value
r_value = add(val1, val2)
print("addition is ", r_value)         # Display the addition result

# Take another number input for subtraction
d = int(input("Enter value = "))

# Call the sub() function using the previous addition result and new number
sub(r_value, d)
