cost=int(input("\n Enter the Cost Price:"))
user=str(input("\n The user is Student(y/n):"))

if user=="y":
    if cost>500:
        discount=(cost*10)/100
        selling_price=cost-discount
    else:
        discount=(cost*5)/100
        selling_price=cost-discount
elif user=="n":
    if cost>500:
        discount=(cost*8)/100
        selling_price=cost-discount
    else:
        discount=(cost*2)/100
        selling_price=cost-discount
else:
    print("Invalid Details")

print("\n The Cost Price:",cost)    
print("\n The discount is:",discount)
print("\n The selling price:",selling_price)