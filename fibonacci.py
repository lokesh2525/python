num=int(input("Enter the any number:"))
a=0
b=1
count=1
print("Fibonacci sequence:")
while count<num:
    print(a)
    c=a+b
    a=b
    b=c
    count=count+1
    
    