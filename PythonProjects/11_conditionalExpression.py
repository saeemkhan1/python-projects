# If - else Statement

a = 4

if a < 5:
    print("Number is less than 5")
elif a > 5:
    print("Number is greater than 5")

# Write a Python program to print "Adult" when the age entered by the user is greater than or equal to 18

age = int(input("Enter your Age: \n"))

if age >= 18:
    print("Adult")
elif age < 18:
    print("Not an Adult")
