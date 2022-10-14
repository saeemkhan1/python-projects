#########################################
# Loops in Python, While Loop & For Loop
#########################################


'''while (Condition is TRUE)
        Body of the loop
'''

# While Loop
# Print a number from 1 to 50

i = 1
while i <= 50:
    print(i)
    i = i + 1

# Print the content of a List using While Loop

a = input("Enter Item: \n")
b = input("Enter Item: \n")
c = input("Enter Item: \n")
d = input("Enter Item: \n")

ListToPrint = [a, b, c, d]
i = 0
while i < len(ListToPrint):
    print(ListToPrint[i])
    i = i + 1

# Break Statement in Loop
for i in range(10):
    print(i)
    if i == 5:
        break

#################################################
# For Loop
# Print the content of the Lists using For Loop
#################################################

fruit1 = input("Enter Fruit: \n")
fruit2 = input("Enter Fruit: \n")
fruit3 = input("Enter Fruit: \n")
fruit4 = input("Enter Fruit: \n")
fruit5 = input("Enter Fruit: \n")

FruitList = [fruit1, fruit2, fruit3, fruit4, fruit5]

for item in FruitList:
    print(item)

##############################
# Range Function in For Loop
##############################
for i in range(10):
    print(i)

##################################################
# Multiplication Table of a number using For Loop
##################################################

number = int(input("Enter number: "))
times = int(input("How many times: "))

for times in range(1, times + 1):
    print((number * times))

################################################################
# Multiplication Table of a number using For Loop (another way)
################################################################

number = int(input("Enter number: "))

for times in range(1, 13):
    '''printing using f strings'''
    print(f"{number}X{times}={number * times}")

##################################################
# Write a Python program
# to greet all the person names stored in a List
# which starts with 'S'
##################################################

l1 = ["Harry", "Sam", "Steve", "John", "Tom", "Sarah"]
for names in l1:
    if names.startswith("S"):
        print("Hello ", names)
    else:
        pass

####################################################
# Multiplication Table of a number using While Loop
####################################################

number = int(input("Enter number: "))
count = 1
while count <= 12:
    print(f"{number}X{count}={number * count}")
    count = count + 1


############################################
# Write a Python program
# To find if a given number is Prime or not
############################################
number = int(input("Enter your number: "))

for i in range(2, number):
    if number % i == 0:
        print("Not Prime")
        break
else:
    print("Prime")

############################################
# Write a Python program
# To add all natural number
############################################
naturalNumber = int(input("Enter the Number:\n"))

sumOfAll = 0
i = 1
while i <= naturalNumber:
    sumOfAll = sumOfAll + i
    i = i + 1
print("Total Sum of number = ", sumOfAll)

#################################################################
# Write a Python program to find the factorial of a given number
# using For Loop
#################################################################

userNumber = int(input("Enter the number you want to find the factorial of : "))

factorial = 1
i = 1

for item in range(i, userNumber+1):
    factorial = factorial * i
    i = i + 1
print(f"Factorial of {userNumber} is {factorial}")

#################################################################
# Write a Python program to find the factorial of a given number
# using While Loop
#################################################################

userNumber = int(input("Enter the number you want to find the factorial of : "))

factorial = 1
i = 1

while i <= userNumber:
    factorial = factorial * i
    i = i + 1
print(f"Factorial of {userNumber} is {factorial}")



##########################################################
# Write a Python Program to print the following * Pattern
#   *  *  *  *  *
#   *  *  *  *  *
#   *  *  *  *  *
#   *  *  *  *  *
#   *  *  *  *  *
##########################################################

n = int(input("Enter Number of Rows: "))
for i in range(n):
    for j in range(n):
        print("*", end="  ")
    print()

####################################################################################
# Write a Python Program to print the following * Pattern (aka increasing Triangle)
#   *
#   *  *
#   *  *  *
#   *  *  *  *
#   *  *  *  *  *
#####################################################################################
n = int(input("Enter Number of Rows: "))
for i in range(n):
    for j in range(i+1):
        print("*", end="  ")
    print()

#####################################################################################
# Write a Python Program to print the following * Pattern (aka Decreasing Triangle)
#   *  *  *  *  *
#   *  *  *  *
#   *  *  *
#   *  *
#   *
#####################################################################################
n = int(input("Enter Number of Rows: "))
for i in range(n):
    for j in range(i, n):
        print("*", end="  ")
    print()
##########################################################
# Write a Python Program to print the following * Pattern
#               *
#            *  *
#         *  *  *
#      *  *  *  *
#   *  *  *  *  *
##########################################################
n = int(input("Enter Number of Rows: "))
for i in range(n):
    for j in range(i, n):
        print(" ", end="  ")
    for j in range(i+1):
        print("*", end="  ")
    print()

