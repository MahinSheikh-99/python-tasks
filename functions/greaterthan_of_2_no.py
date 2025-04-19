# function Method 01
def comparesion_1 () :
    val1 = int(input("Enter value 1= "))
    val2 = int(input("Enter value 2= "))
    if (val1>val2):
        print(val1," is Greater than ",val2)
    else:
        print(val2," is Greater than ",val1)
print("Method 01")
comparesion_1()

# function Method 02
def comparesion_2 (x,y) :
    if (x>y):
        print(x,"is Greater",y)
    else:
        print(y,"is Greater",x)

print("Method 02")
val1 = int(input("Enter value 1= "))
val2 = int(input("Enter value 2= "))

comparesion_2 (val1, val2)

# function Method 03
def comparesion_3 (x,y) :
    if (x > y):
        return x
    else:
        return y
print("Method 03")
val1 = int(input("Enter value 1= "))
val2 = int(input("Enter value 2= "))
c=comparesion_3(val1,val2)
print(c,"is Greater")