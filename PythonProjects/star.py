n = int(input("Enter Number of Rows: "))
for i in range(n):
    for j in range(i+1):
        print("*", end="  ")
    print()
