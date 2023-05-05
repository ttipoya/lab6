#Вариант 28. Фирма занимается сборкой компьютеров. В компьютере компоненты N типов.
#На складе находятся компоненты разных компаний. Количество компаний К1, К2, … КN.
#Сформировать все возможные варианты комплектации компьютеров.
from itertools import product
from random import randint
print('Введите число число типов компонентов N: ',end = '')
n = int(input())
print('ЧАСТЬ 1')
print('--------------------')
firm = []
uslov = []
cena = []
kol = 0
suma = 0
fl = 0
mini = 99999999
minikomb = ''
for i in range(1, n + 1):
    firm.append('K' + str(i))
for i in product(firm, repeat=n):
    #print(i)
    kol = kol + 1
print('Всего комбинаций:' + str(kol))
print('--------------------')
kol = 0
print('ЧАСТЬ 2.1')
print('Допустим у нас есть список всех компаний и дано условие, что компоненты должны быть компаний к которым больше всего доверия')
print('--------------------')
for i in range(0,len(firm),2):
    uslov.append(firm[i])
for i in product(uslov, repeat=n):
    #print(i)
    kol = kol + 1
print('Всего комбинаций при новом условии:' + str(kol))
print('--------------------')
print('ЧАСТЬ 2.2')
print('Допустим фирму попросили собрать максимально дорогой компьютер так, \n'
      'чтобы количество одинаковых компаний не превышало 2')
print('--------------------')
print('Цены на компоненты компаний:')
for i in range(1,n+1):
    cena.append(randint(10000,20000))
    print('K'+str(i) + '='+ str(cena[i-1]),end=' ')
print('')
print('--------------------')
for i in product(firm, repeat=n):
    for m in range(0,n):
        for j in range(1,n+1):
            if int(i[m][-1]) == j and i.count(i[m]) <= 2:
                fl += 1
                suma = suma + cena[j - 1]
            elif i.count(i[m]) > 2:
                suma = 0
    if suma < mini and suma !=0 and fl == 5:
        mini = suma
        minikomb = i
    suma= 0
    fl = 0
print('Маскимальная цена:',mini)
print('Комбинация:',minikomb)
