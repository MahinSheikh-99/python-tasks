# Method 1
def swipe1 () :
    print("method 1")
    val1 = int(input("Enter value 1= "))
    val2 = int(input("Enter value 2= "))
    temp = val1
    val1 = val2
    val2 = temp
    # val1, val2 = val2, val1

    print("after swip value 1 =",val1)
    print("after swip value 2 =", val2)
swipe1()

# Method 2
def swipe2 (a,b) :
    temp = a
    a = b
    b = temp
    # a, b = b, a

    print("after swip value 1 =", a)
    print("after swip value 2 =", b)

print("method 2")
val1 = int(input("Enter value 1= "))
val2 = int(input("Enter value 2= "))

swipe2 (val1,val2)

# Method 3
def swipe3 (a,b) :
    temp = a
    a = b
    b = temp
    # a, b = b, a
    return a, b

print("Method 03")
val1 = int(input("Enter value 1= "))
val2 = int(input("Enter value 2= "))
r_value1, r_value2 = swipe3 (val1,val2)
print("after swip value 1 =", r_value1)
print("after swip value 2 =", r_value2)