class Office:
    off_name='Pragati'
    off_loc='Surampalem'
class Emp1(Office):
    emp_name='Srivalli'
    emp_id='20a31a0427'
class Emp2(Office):
    emp_name='Bhavana'
    emp_id='20a31a0412'
class House(Emp1,Emp2):
    house_loc='Kakinada'
    house_num='1-20'
obj=House()
print(House.emp_name)
print(House.emp_id)
print(Emp2.off_loc)

