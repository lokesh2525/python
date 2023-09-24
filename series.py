n=int(input("Enter the range:"))
x=int(input("Enter x value:"))
sum=1
for i in range(1,n+1):
    sum=sum+((x**i)/i)
print("sum=",sum)