lst=[]
#add elements to a list
lst.append('hello')
lst.append(10)
lst.append(10.5)
lst.append([2,3,4])
print(lst)
#print length of list
print(len(lst))
#remove element at particular index
lst.pop(1)
print(lst)
#remove a particular element or value
lst.remove(10.5)
print(lst)
#print element that is popped
print(lst.pop(0))
#add required element at required position
lst.insert(0,'hello')
print(lst)
#adds a list at the end of other
a=[1,2,3]
b=[4,5,6]
a.extend(b)
print(a)
#return count of any element
l1=[1,2,3,1,5,3,2,2,1,1,6]
print(l1.count(1))
#copies a list
l2=a.copy()
print(l2)
#clears the list
a.clear()
print(a)
#sorting list ascending order
a=[3,1,2]
a.sort()
print(a)
#sorting in descending order
a.sort(reverse=True)
print(a)
#sort and return
x=[3,1,2]
y=sorted(x)
print(x)
print(y)