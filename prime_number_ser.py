# Input the range
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

print(f"Prime numbers between {start} and {end} are:")

# Loop through each number in the range
for num in range(start, end + 1):
    # Prime numbers are greater than 1
    if num > 1:
        # Check if the number is divisible by any number other than 1 and itself
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)
