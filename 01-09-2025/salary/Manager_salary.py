from salary_manager import create_salary,read_all,read_by_salary
from salary_manager import salaries,update,delete_by_salary

def menu():
    message='''
1-create salary
2-read all salaries
3-read by salary
4-update
5-delete
6-exit/logout'''

    choice=int(input(message))
    if choice==1:
       salary=int(input('salary:'))
       create_salary(salary)
    elif choice == 2:
        result_salaries=read_all()
        print('salaries:')

        for salary in result_salaries:
           print(salary)
    elif choice==3:
        salary=int(input('search salary:'))
        index=read_by_salary(salary)
        if salary==-1:
            print('salary not found')
        else:
            print(f'salary is at index{index}')
    elif choice ==4:
        old_salary=int(input('salary to update:'))
        new_salary=int (input('New_salary:'))
        update(old_salary,new_salary)
    elif choice ==5:
        salary=int(input('salary to delete:'))
        delete_by_salary(salary)

    return choice 

def menus():
    print('salary management App')
    choice=menu()
    while choice!=6:
        choice=menu()
    print('Thank you for using APP')

menus()