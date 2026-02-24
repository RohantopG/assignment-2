# here i am takeing inpit for the subjects
sub1 = float(input("Enter marks for Subject 1: "))
sub2 = float(input("Enter marks for Subject 2: "))
sub3 = float(input("Enter marks for Subject 3: "))
sub4 = float(input("Enter marks for Subject 4: "))
sub5 = float(input("Enter marks for Subject 5: "))


print("\n--- MARKS ENTERED ---")
print("Subject 1:", sub1)
print("Subject 2:", sub2)
print("Subject 3:", sub3)
print("Subject 4:", sub4)
print("Subject 5:", sub5)

#here i am calculating the percentage and total marks and grade and result.
total = sub1 + sub2 + sub3 + sub4 + sub5
percentage = (total / 500) * 100

print("\nTotal Marks:", total, "/ 500")
print("Percentage: {:.2f}%".format(percentage))

#here i am using the if else to calculate the grades
if percentage >= 90:
    grade = "A+ Outstanding"
elif percentage >= 80:
    grade = "A Excellent"
elif percentage >= 70:
    grade = "B Good"
elif percentage >= 60:
    grade = "C Average"
elif percentage >= 50:
    grade = "D Pass"
else:
    grade = "F Fail"

print("Grade:", grade)

# Result Calculation (Pass only if ALL subjects >= 40)
if sub1 >= 40 and sub2 >= 40 and sub3 >= 40 and sub4 >= 40 and sub5 >= 40:
    result = "Pass"
else:
    result = "Fail"

print("Result - ", result)
