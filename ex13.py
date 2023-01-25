def invert(string):
    res=''
    for i in string:
        if i==0:
            res=res+'1'
        else:
            res=res+'0'
    return res
x=int(input("Enter first number: "))
y= int(input("Enter second number: "))
z=input("Enter operation: ")
new_x=bin(x)[2:]
new_y=bin(y)[2:]
new_x=invert(new_x)
new_y=invert(new_y)
x=int(new_x,2)
y=int(new_y,2)
if z=='&':
    print(x^y)