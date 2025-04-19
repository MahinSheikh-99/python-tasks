for i in range(1, 6, 1):
    for j in range(5, i-1, -1):
        print(j, end="")
    for k in range(1, i*2, 1):
        print(" ",end="")
    for l in range(i, 6, 1):
        print(l,end="")
    print()

for i in range(1, 5, 1):
    for j in range(5, 4-i, -1):
        print(j,end="")
    for k in range(1, j*2, 1):
        print(" ",end="")
    for l in range(5-i, 6, 1):
        print(l,end="")
    print()