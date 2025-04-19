for i in range (1, 6, 1):
    for j in range(1, 6-i, 1):
        print(" ",end="")
    for k in range(1, 1+i, 1):
        print(k,end="")
    for l in range(i-1, 0, -1):
        print(l,end="")
    print()

for x in range (4, 0, -1):
    for y in range(1, 6-x, 1):
        print(" ",end="")
    for z in range(1, x+1, 1):
        print(z,end="")
    for v in range(x-1, 0, -1):
        print(v,end="")
    print()