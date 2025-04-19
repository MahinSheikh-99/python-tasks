num=0
for i in range (num, num < 5,1) :
    # print(i)
    print("1:addition, 2:subtraction, 3:multiplication, 4:division")
    val1 = int(input("Enter value 1= "))
    val2 = int(input("Enter value 2= "))
    num = int(input("Enter value= "))
    if (num==1):
        calculation= val1 + val2
        print(calculation)
    elif (num==2):
        calculation= val1 - val2
        print(calculation)
    elif (num==3):
        calculation= val1 * val2
        print(calculation)
    elif (num==4):
        calculation= val1 / val2
        print(calculation)
    elif (num==5):
        break