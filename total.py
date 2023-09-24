print("Enter your Subjects marks:")

sub1 = float (input ())
sub2= float (input ())
sub3= float (input ())
sub4= float (input ())
sub5= float (input ())

total=sub1+sub2+sub3+sub4+sub5
average = total / 5.0
percentage = (total / 500.0) * 100

if average>=90:
    grade= 'A'
elif average >= 80 and average < 90:
    grade = 'B'
elif average >= 70 and average < 80:
    grade = 'C'
elif average >= 60 and average < 70:
    grade = 'D'
else:
    grade = 'E'
    
print("\n The Total Marks:",total)
print("\n The average is:",average)
print("\n The percentage is:",percentage,"%")
print("\n Grade:",grade)