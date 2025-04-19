# Method 1
print("Method 1")
def factorial1 () :
    temp = 1
    num = int(input("Enter value = "))
    for i in range (1, num+1):
        temp = i*temp
    print(temp)
factorial1()

# Method 2
def factorial1 (x) :
    temp = 1
    for i in range (1, num+1):
        temp = i*temp
    print(temp)

print("Method 2")
num = int(input("Enter value = "))
factorial1(num)

# Method 3
def factorial1 (x) :
    temp = 1
    for i in range (1, num+1):
        temp = i*temp
    return temp

print("Method 2")
num = int(input("Enter value = "))
r_value = factorial1(num)
print(r_value)