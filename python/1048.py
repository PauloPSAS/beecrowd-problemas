salary = float(input())
newSalary = pct = salaryAdjustment = 0

if 0 <= salary <= 400.:
    pct = 15
    newSalary = salary + (salary * pct / 100)
    salaryAdjustment = salary * pct / 100

elif 400.01 <= salary <= 800.:
    pct = 12
    newSalary = salary + (salary * pct / 100)
    salaryAdjustment = salary * pct / 100

elif 800.01 <= salary <= 1200.:
    pct = 10
    newSalary = salary + (salary * pct / 100)
    salaryAdjustment = salary * pct / 100

elif 1200.01 <= salary <= 2000.:
    pct = 7
    newSalary = salary + (salary * pct / 100)
    salaryAdjustment = salary * pct / 100
else:
    pct = 4
    newSalary = salary + (salary * pct / 100)
    salaryAdjustment = salary * pct / 100

print(f"Novo salario: {newSalary:.2f}\nReajuste ganho: {salaryAdjustment:.2f}\nEm percentual: {pct} % ")
