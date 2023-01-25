x=input("Enter any number:")
try:
    x=int(x)
    if x > 0 and x < 20:
        if x % 2 == 0:
            print('Weird number')
        else:
            print("Normal number")
    elif x >= 20 and x < 30:
        print("Normal number")
    elif x >= 30:
        if x % 2 == 1:
            print("Normal number")
        else:
            print("Weird number")
    else:
        print("Invalid Input")
except:
    print("Invalid Input")