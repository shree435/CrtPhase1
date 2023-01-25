lst = [10, 20, 30, 40, 50]
x = int(input("Enter any number:"))
for i in range(0, len(lst)):
    if lst[i] == x:
        print(i)