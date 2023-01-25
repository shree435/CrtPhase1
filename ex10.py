l=[{'20a31a0427@pragati.ac.in':'Srivalli'},
   {'20a31a0459@pragati.ac.in':'Prasad'},
   {'20a31a0405@pragati.ac.in':'Aishwarya'},
   {'20a31a0460@pragati.ac.in':'Tarak'}]
username = input()
password = input()
temp={
    username:password
}
for temp in l:
    if temp.keys==username and temp.values==password:
        print('Correct password')
else:
    print('Wrong Password')