from random import random,randint
n=int(input("Enter max limit:"))
computer=0
player=0
array=['rock','paper','scissor']
while player<n and computer<n:
    a=array[randint(0,2)]
    print("Choose among the following: ",array)
    b=input("Your turn:").lower()
    print("Computer turn:"+a)
    if a=='rock' and b=='paper':
        player=player+1
        print("Player Score Is "+str(player))
        print("Computer Score Is "+str(computer))
    elif a=='paper' and b=='rock':
        computer=computer+1
        print("Player Score Is " + str(player))
        print("Computer Score Is " + str(computer))
    elif a=='paper' and b=='scissor':
        player=player+1
        print("Player Score Is " + str(player))
        print("Computer Score Is " + str(computer))
    elif a=='scissor' and b=='paper':
        computer=computer+1
        print("Player Score Is " + str(player))
        print("Computer Score Is " + str(computer))
    elif a=='rock' and b=='scissor':
        computer=computer+1
        print("Player Score Is " + str(player))
        print("Computer Score Is " + str(computer))
    elif a=='scissor' and b=='rock':
        player=player+1
        print("Player Score Is " + str(player))
        print("Computer Score Is " + str(computer))
    elif a==b:
        print("Player Score Is " + str(player))
        print("Computer Score Is " + str(computer))
        continue
    else:
        print("Invalid input")
if player==n:
    print("You Won")
else:
    print("Computer Won")
