# Write a program to find the largest of 4 numbers entered by the user

a = int(input("Enter 1st number: \n"))
b = int(input("Enter 2nd number: \n"))
c = int(input("Enter 3rd number: \n"))
d = int(input("Enter 4th number: \n"))

if a > b and a > c and a > d:
    num1 = a
    print("The biggest number is:", num1)
elif b > a and b > c and b > d:
    num2 = b
    print("The biggest number is:", num2)
elif c > a and c > b and c > d:
    num3 = c
    print("The biggest number is:", num3)
else:
    num4 = d
    print("The biggest number is:", num4)

# Write a Python Program to find out whether a student passed or Failed.
# It requires Total 40% and individual 33% (total 3 Subjects)

'''Logic:
subject1 >33
subject2 >33
subject3 >33
total = (s1+s2+s3)/3 >= 40 '''

sub1 = int(input("Enter Subject 01 marks: \n"))
sub2 = int(input("Enter Subject 02 marks: \n"))
sub3 = int(input("Enter Subject 03 marks: \n"))

totalMarks = (sub1 + sub2 + sub3) / 3

if sub1 > 33 and sub2 > 33 and sub3 > 33 and totalMarks >= 40:
    print("Passed")
else:
    print("Failed")

# A Spam comment is defined as a text containing following keywords
# "Make a lot of money", "Buy now", "Subscribe", "Click the Ad"
# Write a Python program to detect a Spam

sentence = input("Enter the Sentence: \n")
if "Make a lot of money" in sentence:
    print("Spam")
elif "Buy now" in sentence:
    print("Spam")
elif "Subscribe" in sentence:
    print("Spam")
elif "Click the Ad" in sentence:
    print("Spam")
else:
    print("Not a Spam")

# Write a program to find if a Username is less than 10 character or not
username = input("Enter Username: \n")
lengthUsername = username.__len__()
if lengthUsername > 10:
    print("Username Accepted")
else:
    print("Username too short")

# Write a Python program to find out whether a name is in the List or not

a = input("Enter Student Name: \n")
b = input("Enter Student Name: \n")
c = input("Enter Student Name: \n")
d = input("Enter Student Name: \n")
e = input("Enter Student Name: \n")

nameList = [a, b, c, d, e]
print(nameList)

'''Finding the name '''
findName = input("Check Student Name: \n")

if findName in nameList:
    print("Student is in the List")
else:
    print("Student Name is Missing!")

# Write a Python Program to determine the Grade of the Subject, based on Marks

sub1 = input("Enter Subject: \n")
sub2 = input("Enter Subject: \n")
sub3 = input("Enter Subject: \n")
sub4 = input("Enter Subject: \n")
sub5 = input("Enter Subject: \n")
sub6 = input("Enter Subject: \n")

subject = [sub1, sub2, sub3, sub4, sub5, sub6]
print(subject)

marks1 = int(input("Enter marks for " + sub1))

if marks1 >= 90:
    print("Marks for " + sub1 + " is Grade A+")
elif marks1 >= 80:
    print("Marks for " + sub1 + " is Grade A")
elif marks1 >= 70:
    print("Marks for " + sub1 + " is Grade B")
elif marks1 >= 60:
    print("Marks for " + sub1 + " is Grade C")
elif marks1 >= 50:
    print("Marks for " + sub1 + " is Grade D")
else:
    print("Marks for " + sub1 + " is Grade F")

marks2 = int(input("Enter marks for " + sub2))

if marks2 >= 90:
    print("Marks for " + sub2 + " is Grade A+")
elif marks2 >= 80:
    print("Marks for " + sub2 + " is Grade A")
elif marks2 >= 70:
    print("Marks for " + sub2 + " is Grade B")
elif marks2 >= 60:
    print("Marks for " + sub2 + " is Grade C")
elif marks2 >= 50:
    print("Marks for " + sub2 + " is Grade D")
else:
    print("Marks for " + sub2 + " is Grade F")

marks3 = int(input("Enter marks for " + sub3))

if marks3 >= 90:
    print("Marks for " + sub3 + " is Grade A+")
elif marks3 >= 80:
    print("Marks for " + sub3 + " is Grade A")
elif marks3 >= 70:
    print("Marks for " + sub3 + " is Grade B")
elif marks3 >= 60:
    print("Marks for " + sub3 + " is Grade C")
elif marks3 >= 50:
    print("Marks for " + sub3 + " is Grade D")
else:
    print("Marks for " + sub3 + " is Grade F")

marks4 = int(input("Enter marks for " + sub4))
if marks4 >= 90:
    print("Marks for " + sub4 + " is Grade A+")
elif marks4 >= 80:
    print("Marks for " + sub4 + " is Grade A")
elif marks4 >= 70:
    print("Marks for " + sub4 + " is Grade B")
elif marks4 >= 60:
    print("Marks for " + sub4 + " is Grade C")
elif marks4 >= 50:
    print("Marks for " + sub4 + " is Grade D")
else:
    print("Marks for " + sub4 + " is Grade F")

marks5 = int(input("Enter marks for " + sub5))

if marks5 >= 90:
    print("Marks for " + sub5 + " is Grade A+")
elif marks5 >= 80:
    print("Marks for " + sub5 + " is Grade A")
elif marks5 >= 70:
    print("Marks for " + sub5 + " is Grade B")
elif marks5 >= 60:
    print("Marks for " + sub5 + " is Grade C")
elif marks5 >= 50:
    print("Marks for " + sub5 + " is Grade D")
else:
    print("Marks for " + sub5 + " is Grade F")


marks6 = int(input("Enter marks for " + sub6))

if marks6 >= 90:
    print("Marks for " + sub6 + " is Grade A+")
elif marks6 >= 80:
    print("Marks for " + sub6 + " is Grade A")
elif marks6 >= 70:
    print("Marks for " + sub6 + " is Grade B")
elif marks6 >= 60:
    print("Marks for " + sub6 + " is Grade C")
elif marks6 >= 50:
    print("Marks for " + sub6 + " is Grade D")
else:
    print("Marks for " + sub6 + " is Grade F")

