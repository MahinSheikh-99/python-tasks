start=3
end = int(input("Enter Number = "))

for num in range (start, end+1, 1):
    for i in range (2, num, 1):
        if (num % i) == 0:
            break
    else :
        print(num)