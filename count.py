num=int(input("Enter the number:"))
count=0
while num!=0:
    num //= 10
    count=count+1
print("The number Digit is:",count)