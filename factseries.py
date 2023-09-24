num=int(input("Enter the range:"))
x=int(input("Enter x value:"))
sum=1
fact=1
for i in range(1,num+1):
    if num < 0:
        print("Sorry, factorial does not exist for negative numbers")
    elif num == 0:
        print("The factorial of 0 is 1")
    else:
        for i in range(1,num + 1):
            fact = fact*i
sum=sum+((x**i)/fact)
print("sum=",sum)