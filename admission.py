per=int(input("Enter your percentage:"))
gender=str(input("Enter gender(f/m):"))

if per>82 and gender=='m':
    print("You can take Admission")
else:
    print("you are not eligible for Admission")