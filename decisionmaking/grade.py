mark = int(input("Enter your mark: "))

if mark>90:
    if mark<=100:
        print("A grade")
if mark>80:
    if mark<=90:
        print("B grade")
if mark>60:
    if mark<=80:
        print("C grade")
else:
    print("Sorry you are failed")