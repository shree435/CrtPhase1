username=input("Enter username:")
password=input("Enter password:")
if len(password)>=8:
    print("Your username is "+username+"and password is "+password)
else:
    print("Your password must be minimum 8 charecters long.Try again!")
