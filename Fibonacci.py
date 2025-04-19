a = 0
b = 1

num = int(input("Enter value = "))
for i in range(1, num+1, 1):
    print(a)
    c = a + b
    a = b
    b = c
    # print(a)