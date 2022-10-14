###########################################################
# Create a List using [], A list can contain any data type
###########################################################

listA = [9, 2, 4, 54, 6]
# Print a list using print() function
print(listA[2])
# Access List using list index, Update a list
listA[0] = "Saeem"
print(listA)

listB = [1.5, True, "SDK", 12, "Python", "Java", 32, 55.655]
print(listB)

# List slicing
print(listB[0:4])


# List Methods
listC = [9, 2, "Saeem", 54, 6]
listC.sort()                # Sorts the List
listC.reverse()             # Reverses the List
listC.append(45)            # Appends at the end of the List
listC.insert(2, "Saeem")    # Inserts "Saeem" at index 2
listC.remove(54)            # Removes 54 from the List
listC.pop(2)                # Removes items from Index 2

print(listC)






