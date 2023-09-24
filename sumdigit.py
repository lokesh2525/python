num=int(input("Enter the number:"))
sum=0
while num!=0:
    digit = num % 10
    num //= 10
    sum=sum+digit
print("Sum of digit: " + str(sum))