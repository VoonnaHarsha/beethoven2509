from salary_manager import create_salary,read_all,read_by_salary
from salary_manager import salaries,update
create_salary(1000)
create_salary(5000)
create_salary(60000)
create_salary(3000)
result_salaries=read_all()
for salary in result_salaries:
    print(salary)