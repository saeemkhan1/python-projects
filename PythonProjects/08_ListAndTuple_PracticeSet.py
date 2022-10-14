# Write a Python program, to store values in a List provided by a User

l1 = input("Enter the 1st Input:")
l2 = input("Enter the 2nd Input:")
l3 = input("Enter the 3rd Input:")
l4 = input("Enter the 4th Input:")
l5 = input("Enter the 5th Input:")
l6 = input("Enter the 6th Input:")
l7 = input("Enter the 7th Input:")

listOfValues = [l1, l2, l3, l4, l5, l6, l7]

print(listOfValues)


# Write a Python program, to accept values in a List provided by a User and Sort
# Typecasting to int from string (Which is default Data Type)
s1 = int(input("Enter the 1st Input:"))
s2 = int(input("Enter the 2nd Input:"))
s3 = int(input("Enter the 3rd Input:"))
s4 = int(input("Enter the 4th Input:"))
s5 = int(input("Enter the 5th Input:"))
s6 = int(input("Enter the 6th Input:"))
List = [s1, s2, s3, s4, s5, s6]
List.sort()
print(List)

# Check that a Tuple cannot be changed

tupleCheck = (23, 45.5, "Saeem")
#tupleCheck [0] = 75         # Throws an error as expected

# Write a Python Program to sum of all the elements in a List

item1 = int(input("Enter the 1st Input:"))
item2 = int(input("Enter the 2nd Input:"))
item3 = int(input("Enter the 3rd Input:"))
item4 = int(input("Enter the 4th Input:"))
item5 = int(input("Enter the 5th Input:"))
item6 = int(input("Enter the 6th Input:"))

listItem = [item1, item2, item3, item4, item5, item6]

print(sum(listItem))

# Write a Pythin Program, to count the number of zero in the given Tuple

tupleZeroCount = (7, 0, 8, 0, 0, 9)
print(tupleZeroCount.count(0))



