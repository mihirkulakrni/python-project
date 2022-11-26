print ("Marks counter")
sub1 = int(input("Enter your marks(1): "))
sub2 = int(input("Enter your marks(2): "))
sub3 = int(input("Enter your marks(3): "))
sub4 = int(input("Enter your marks(4): "))
sub5 = int(input("Enter your marks(5): "))
avg = (sub1+sub2+sub3+sub4+sub5)/5
if avg >= 90:
    print("Grade A")
elif avg >= 80:
    print("Grade B")
    
elif avg >= 70:
    print("Grade C")

elif avg >= 60:
    print("Grade D")
else:
    print("Grade F Fail!!")
