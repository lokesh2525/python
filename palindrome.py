num=int(input("Enter the number:"))
temp=num
rev=0
while num!=0:
    digit = num % 10
    num //= 10
    rev = rev*10 + digit
if temp==rev:
    print("The number is Palindrome")
else:
    print("The number is Not Palindrome")