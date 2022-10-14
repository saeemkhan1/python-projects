## Defining a function
def percent(marks):
    per = ((marks[0] + marks[1] + marks[2] + marks[3]) / 400) * 100
    return per


marks1 = [56, 43, 78, 79]
percentage1 = percent(marks1)

marks2 = [65, 37, 87, 97]
percentage2 = percent(marks2)

marks3 = [56, 55, 78, 76]
percentage3 = percent(marks3)

marks4 = [56, 23, 78, 23]
percentage4 = percent(marks4)

print(percentage1, percentage2, percentage3, percentage4)

####################################################################
# Write a Python program to greet a user "Good Day" using functions
####################################################################
def greet(name):
    print("Good Day " + name)


greet(name=input("Enter Name:"))


# Recursive function
def factorial_recursive(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial_recursive(n - 1)


f = factorial_recursive(int(input("Enter number: ")))
print(f)


###############################################################
# Write a Program to find the biggest number out of the three
###############################################################

def maximum(num1, num2, num3):
    if num1 > num2:
        if num1 > num3:
            return num1
        else:
            return num3
    else:
        if num2 > num3:
            return num2
        else:
            return num3


num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
num3 = int(input("Enter 3rd number: "))
m = maximum(num1, num2, num3)

print("Biggest number is " + str(m))


###################################################
# Write a Program to convert Celsius to Fahrenheit
###################################################

def fahrenheit(cel):
    temp = (cel * (9 / 5)) + 32
    return temp


c = int(input("Enter Celsius: "))
f = fahrenheit(c)
print("Fahrenheit is: " + str(f))

##################################################
# Write a program to add sum of n natural numbers
##################################################
# sum (n) = sum (n-1) + n

def sum_recursive(n):
    if n == 1 or n == 0:
        return 1
    return n + sum_recursive(n - 1)


f = sum_recursive(int(input("Enter number: ")))
print(f)


###################################################
# Write a Program to convert inches to cm
###################################################
def centimetre(c):

    temp = (inch * 2.54)
    return temp


inch = int(input("Enter inches: "))
f = centimetre(inch)
print("cm is: " + str(f))




