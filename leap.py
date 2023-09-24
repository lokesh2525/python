num=int(input("Enter the Year:"))
if num%100!=0:
    if num%4==0:
        print("The Given Year is Leap Year")
    else:
        print("The Given Year is not Leap Year")
elif num%400==0:
    print("The Given Year is Leap Year")
else:
    print("The Given Year is not Leap Year")
    
        
