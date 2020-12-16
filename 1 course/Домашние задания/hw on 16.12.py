import math
import random
from random import random, randrange, randint
def task1(p1, p2):
    assert isinstance(p1, tuple) and isinstance(p2, tuple), "Неверный тип данных"
    assert len(p1)== 2 and len(p2)== 2, "Кортеж должен иметь 2 элемента"
    for i in p1:
        if not(isinstance(i, float) or isinstance(i, int)):
            raise TypeError("Некорректный тип данных в первом котреже")
    for i in p2:
        if not(isinstance(i, float) or isinstance(i, int)):
            raise TypeError("Некорректный тип данных во втором котреже")
    x1= p1[0]
    y1= p1[1]
    x2= p2[0]
    y2= p2[1]
    ky= x1-x2
    kx= y1-y2
    b= x1*y2-x2*y1
    if b>0:
        return f'{ky}y={kx}x +{b}'
    else:
        return f'{ky}y= {kx}x -{-b}'
#task1((66, 13), (12, 36))

########################################################################

def task2():
    monthly= 0
    loan= 0
    inter= 0
    payments= 0
    Duration= 0
    Price= input("Сумма займа/кредита: ")
    Rate= int(input("Процентная ставка: "))
    Time= input("Примерное время выплачивания(в годах): ")
    Duration= float(Time)
    loan= float(Price)
    inter= float(Rate)
    payments= Duration* 12
    monthly= loan* inter* (1+ inter)* payments \
                    / ((1+ Rate)* payments- 1)
    print("Ежемесячный платеж в рублях %.2f ₽" % monthly)
#task2()

########################################################################

def task3():
    list1= [666, [312, 321], king, 'fighter', 12, "first", 'man', ['lmao', 'pink'], zxc]
    list2= [king, 'main', 'fighter', 12, [312, 321]]
    list3= []
    for www in list1:
        if www in list3:
            continue
        for ww in list2:
            if www == ww:
                list3.append(www)
                break
    print(list3)
#task3()

########################################################################

#task4
whitelist= ['grape', 'apple', 'table', 'extrarifle100','knife','old_sword and wooden_shield', 'an', 'a', 'just', 'qwertyuioasdfghjklzxcvbnm,qwerty112345']
#for www in range(10):
    #whitelist.append(randint(-1000, 1000))
print(whitelist)
whitelist.sort(key=len)
print(whitelist)

########################################################################
#task5
blacklist= []
for www in range(10):
    add= str(input('Введите слова: '))
    blacklist.append(add)
print(dict((x, blacklist.count(x)) for x in set(blacklist) if blacklist.count(x)> 1))
