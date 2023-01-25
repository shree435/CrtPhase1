lst = []
d = {}
for i in range(2):
    d.update({
        'name': input(),
        'rollNumber': input()
    })
    lst.append(d)
print(d)