salaries=[]
salaries.append(1000)
salaries.append(9000)
salaries.append(6000)
search=6000
index=-1
i=1

for salary in salaries:
    if salary== search:
       index+=i
       break
    i+=1
    
print(index)
print(salaries)
