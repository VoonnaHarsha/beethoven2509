salaries=[]

#crud-create,readall, readby id,update,delete,read by salary

def create_salary(salary):
    global salaries
    salaries.append(salary)

def read_all():
    return salaries 
def read_by_salary(salary):#return 1st occurance index of salary
    for i in range(len(salaries)):
        if salaries[i]==salary:
           return i
    return -1

def update(old_salary,new_salary):
    global salaries
    index=read_by_salary(old_salary)
    salaries[index]=new_salary
    return salaries

def delete_by_salary(salary):
    global salaries
    index=read_by_salary(salaries)
    salaries.pop(index)

create_salary(1000)
create_salary(5000)
create_salary(8000)
create_salary(3000)
return_salaries=read_all()
for salary in return_salaries:
    print(salary)

print(read_by_salary(8000))
print(read_by_salary(4000))
print(salaries[read_by_salary(8000)])
update(8000,8500)
print(read_all())

