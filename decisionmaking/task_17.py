# Eligible for Exam: Take attendance and marks. Eligible if attendance>=75 AND
# marks>=40

attendance = int(input("Enter the attendance: "))
marks = int(input("Enter the marks: "))

if attendance>=75 and marks>=40:
    print("You are eligible for exam")
else:
    print("You are not eligible for exam")