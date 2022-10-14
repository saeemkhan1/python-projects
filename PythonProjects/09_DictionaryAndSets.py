##############
# Dictionary
##############

myDictionary = {
    "fast": "Usain Bolt",
    "genius": "Albert Einstein",
    "fittest": "Mr. Olympia",
    "marks": [1, 2, 5],
    "dictionarywithinadictionary": {'Mr. Olympia': 'Arnold'},
    1: 2

}
print(type(myDictionary))   # Printing the 'Type' Dictionary
print(myDictionary)         # Printing the content of the Dictionary
m = (list(myDictionary))    # Changing the 'type' from 'dict' to 'list' using Typecasting
print(type(m))              # Printing the new 'type' of the Dictionary, which is now 'List'


#####################
# Dictionary Methods
#####################

print(myDictionary.keys())      # Prints the keys of the Dictionary
print(myDictionary.values())    # Prints the values of the Dictionary
print(myDictionary.items())     # Prints the [key, values] (all contents) of the Dictionary

myDictionary.update({"fast": "Saeem Khan"})
myDictionary.update({"genius": "SDK"})

dictionaryUpdate = {
    "slow": "Mr. Slow",
    "medium": "Mr. Medium",
    "Average Marks": [81.8, 92.9, 85, True]
}
myDictionary.update(dictionaryUpdate)       # Updates the Dictionary by adding key-value pairs from "dictionaryUpdate"

print(myDictionary.items())

print(myDictionary.get("medium"))      # Prints value associated with key "medium"

print(myDictionary["medium"])          # Prints value associated with key "medium"

print(myDictionary.get("medium2"))     # Will return None as "medium2" is not present in the Dictionary

print(myDictionary["medium2"])         # Will throw an error as "medium2" is not present in the Dictionary



#########
# Sets
#########

setA = {1, 2, 3, 5, 5, 5}   # Set will not have repetitive elements inside
print(type(setA))
print(setA)

# This syntax will create an empty dictionary and not an empty set
a = {}
print(type(a))

# An empty set can be created using the below syntax

b = set()
print(type(b))

# Adding Values in an empty set using .add method
b.add("StringA")
b.add(4)
b.add(5)
b.add(5)            # Can not add duplicate values in Set
b.add(23)
b.add((2, 4, 7))    # Can add Tuple in a Set

print(b)
print(len(b))       # Prints the Length of the Set


b.remove(23)        # Removes 23 from Set b
print(b)
print(len(b))

b.pop()             # Removes random element from the set b
print(b)


# Cannot add List or Dictionary in a Set
c = set()
c.add({"Name": "Python"})


