start=int(input("Start Enter Number = "))
end = int(input("End Enter Number = "))

# for check number of digits
for num in range (start, end+1, 1):
    x=num
    count=0
    
    while(x>0):
        x=int(x/10)
        count=count+1

# for check armstrong no
    sum = 0
    temp = num
    while (temp>0):
        digit=temp%10
        sum += digit**count
        temp //= 10

#for print all armstsrong number
    if num == sum:
        print(num)