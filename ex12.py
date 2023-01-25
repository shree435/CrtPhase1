n1=0
n2=1
print(n1,n2,sep=" ",end=" ")
for i in range (2,100):
    n=n1+n2
    print(n,end=" ")
    n1=n2
    n2=n
