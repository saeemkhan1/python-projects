# Write a program to write a dictionary of words with meanings,
# user can select words and will get a reply in return

dictionary = {"Admire": "Regard with respect",
              "Great": "Very Well",
              "Awesome": "Fantastic",
              "Mighty": "Very Strong"
           }
print("Enter any words from below:\n", dictionary.keys())
z = input("Enter the Word:")
print("Meaning of your word is: ", dictionary.get(z))

# Write a program to input 8 numbers from user, and display only the unique numbers
a = set()
b = int(input("Enter your element: "))
c = int(input("Enter your element: "))
d = int(input("Enter your element: "))
e = int(input("Enter your element: "))
f = int(input("Enter your element: "))
g = int(input("Enter your element: "))
h = int(input("Enter your element: "))
i = int(input("Enter your element: "))

a.add(b)
a.add(c)
a.add(d)
a.add(e)
a.add(f)
a.add(g)
a.add(h)
a.add(i)

print(a)


# Write a program to input 8 numbers from user, and display only the unique numbers
setB = set()
x = int(input("Enter your element: "))
y = input("Enter your element: ")

setB.add(x)
setB.add(y)
print(setB)

# What will be the length of the following set

s = set()
s.add(20)
s.add(20.0)
s.add("20")
print(len(s))

# What is the type of this set
v = {}
print(type(v))


# Create an empty Dictionary. Allow 4 friends to input their language as value and use keys as their names
# Assume their names are unique
# Ex {"John" : "English",
#      "Harry" : "Hindi",
#       "Saeem": "Bengali",
#       "Mo": "Arabic"
# }

friendsLanguage = {}

name1 = input("Enter your Name: ")
language1 = input("Enter your Language: ")
name2 = input("Enter your Name: ")
language2 = input("Enter your Language: ")
name3 = input("Enter your Name: ")
language3 = input("Enter your Language: ")
name4 = input("Enter your Name: ")
language4 = input("Enter your Language: ")

friendsLanguage[name1] = language1
friendsLanguage[name2] = language2
friendsLanguage[name3] = language3
friendsLanguage[name4] = language4
print(friendsLanguage)



