salario = int(input()) 

if (salario > 0 and salario < 600):
    reaju = salario*0.17
    percent = 17
elif (salario > 600.01 and salario < 900):
    reaju = salario*0.13
    percent = 13
elif (salario > 900.01 and salario < 1500):
    reaju = salario*0.12
    percent = 12
elif (salario > 1500.01 and salario < 2000):
    reaju = salario*0.10
    percent = 10
else:
    reaju = salario*0.05
    percent = 5

print("Novo salario: {} \nReajuste ganho: {} \nEm percentual: {}%".format(salario+reaju, reaju, percent))