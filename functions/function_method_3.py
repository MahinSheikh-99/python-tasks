def add (x,y) :
    z = x + y
    return z

def sub(x,y) :
    z = x - y
    print("subtraction is ",z)

val1 = int(input("Enter value 1= "))
val2 = int(input("Enter value 2= "))

r_value = add(val1,val2)
print("addition is ",r_value)

d=int(input("Enter value = "))
sub(r_value,d)