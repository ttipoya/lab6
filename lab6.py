#Вариант 28. Фирма занимается сборкой компьютеров. В компьютере компоненты N типов.
#На складе находятся компоненты разных компаний. Количество компаний К1, К2, … КN.
#Сформировать все возможные варианты комплектации компьютеров.
from itertools import product
print('Введите число число типов компонентов N: ',end = '')
n = int(input())
print('ЗАДАНИЕ 1')
print('--------------------')
firm = []
uslov = []
osnov = []
s_uslov = []
kol = 0
suma = 0
rast = 0
pods = 0
maxi = 0
maxikomb = ''
minikomb =''
for i in range(1, n + 1):
    firm.append('K' + str(i))
for i in product(firm, repeat=n):
    osnov.append(i)
for i in osnov:
   # print(i)
    kol = kol + 1
print('Всего комбинаций:' + str(kol))
print('--------------------')
kol = 0
print('ЗАДАНИЕ 2.1')
print('Допустим у нас есть список всех компонентов и дано условие, что компоненты должны быть фирмы стоящей на нечётном месте')
print('--------------------')
for i in range(len(firm)):
    if int(firm[i][-1]) % 2 != 0:
        uslov.append(firm[i])
for i in product(uslov, repeat=n):
    s_uslov.append(i)
for i in s_uslov:
 #   print(i)
    kol = kol + 1
print('Всего комбинаций при новом условии:' + str(kol))
print('--------------------')
print('ЗАДАНИЕ 2.2')
print('Допустим у нас есть список всех вариантов и дана задача найти максимальоне расстояние\n'
'между элементами у которых на чётных местах стоят чётные компененты компаний, а на нечётных нечётные')
print('--------------------')
for i in range(len(osnov)):
    rast += 1
    for m in range(0,n):
        if int(osnov[i][m][-1]) %2 == 0 and m % 2 != 0:
            suma = suma + 1
        if int(osnov[i][m][-1]) % 2 != 0 and m % 2 == 0:
            suma = suma + 1
        if suma == n:
            if pods == 0:
                pods+=1
            elif pods == 1:
                if maxi <= rast:
                    maxi = rast
                    maxikomb = osnov[i]
                    minikomb = osnov[i - rast]
                    pods = 0
            rast = 0
    suma = 0
print('Максимальное расстояние:',maxi)
print('Первая комбинация:',minikomb)
print('Вторая комбинация:',maxikomb)
print('--------------------')

