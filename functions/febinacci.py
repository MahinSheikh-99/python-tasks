# method 1
def fibbonacci1 () :
    a = 0
    b = 1
    print("Method 1")
    num = int(input("Enter value = "))
    for i in range(1, num+1, 1):
        c = a + b
        a = b
        b = c
    print(c)

fibbonacci1()

# method 2
def fibbonacci2 (x) :
    a = 0
    b = 1
    for i in range(1, num+1, 1):
        c = a + b
        a = b
        b = c
    print(c)
print("Method 2")
num = int(input("Enter value = "))
fibbonacci2(num)

# method 3
def fibbonacci3 (x) :
    a=0
    b=1
    for i in range(1, num+1, 1):
        c = a + b
        a = b
        b = c
    return c
print("Method 3")
num = int(input("Enter value = "))
r_value = fibbonacci3(num)
print(r_value)