num=int(input("Enter the number:"))
sum=0
while num!=0:
    digit = num % 10
    num //= 10
    sum=sum*(digit**3)
    
if sum==num:
    print("The number is armstrong")
else:
    print("The number is not armstrong")