# Method 1
def prime1 () :
    print("method 1")
    num = int(input("Enter value = "))
    for i in range (2, num, 1):
         if (num % i == 0):
            b = 0
            break
         else:
             b = 1
    if (b == 0):
        print(num,"is not prime number")
    else:
        print(num,"is prime number")
prime1()

# Method 2
def prime2 (x) :
    for i in range (2, num, 1):
         if (num % i == 0):
            b = 0
            break
         else:
             b = 1
    if (b == 0):
        print("Given num is not prime number")
    else:
        print ("Given num is prime number")

print("method 2")
num = int(input("Enter value = "))
prime2 (num)

# Method 3
def prime3 (x) :
    for i in range (2, num, 1):
         if (num % i == 0):
            b = 0
            break
         else:
             b = 1
    if (b == 0):
        return "Given num is not prime number"
    else:
        return "Given num is prime number"

print("method 3")
num = int(input("Enter value = "))
r_value = prime2 (num)
print(r_value)