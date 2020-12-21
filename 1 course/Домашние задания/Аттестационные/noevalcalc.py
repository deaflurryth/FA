# -*- coding: utf-8 -*-

#1) Реализовать текстовый калькулятор нескольких правильных, неправильных и смешанных дробей
#   и обычных чисел с математическим порядком вычисления.
#2) Способ записи смешанных дробей – 5(1/4), правильных – 5/9, неправильных 19/7.
#3) Результат должен быть сокращен и при необходимости в виде смешанной дроби.
#4) После завершения операции позволяет ввести следующее выражение.  ✓
#  Завершение работы с программой вызывается при вводе команды exit. ✓
#5) Также добавить в калькулятор возможность сохранение результата вычислений по команде ‘save наименование_результата’. ✓ +-
#6) Реализовать сохранение до 10 результатов. При вводе команды del наименование_результата удаляет результат из сохраненных. ✓
#7) При вводе команды to double, калькулятор выводит результат в виде числа с плавающей точкой.
#8) Функцию eval() и его поодобия использовать ЗАПРЕЩЕНО!!!!!

import math
import parser
a= 1
b= 1
mathconsta= {
            '+': (a + b),
            '-': (a - b),
            '*': (a * b),
            '/': (a / b),
            '^': (a ** b),
            }

cache= {} #Результаты вычислений
output= 0
temp= []

def main():
    global cache, output, temp
    holder= input('Input:  ')
    if 'save' in holder:                             #сохранение результата
        for www in temp:
            cache.update({www: www})
        print('Output: save success')
        main()
    elif 'del' in holder:                            #удаление результата
        mdel= input('Enter the name of the result to be deleted:  ')
        if str(mdel) in temp:
            for www in temo:
                print(f'result {www} successfully deleted')
                del cache[www]
            print('delete success')
        else:
            print('not found, try another name...')
        main()

    else:
                                                    #начало крови, пота и боли(рекурсивный алгоритм аля рекурсия)
        holder= holder.replace(' ', '')             #разгребаем мусорные кучи с пробелами(реплесаем на 0(убираем))

        for key in cache.keys():                    #достаем m1(условно) и вставляем в выражение, используем получившийся рез
            holder= holder.replace(key, str(cache[key][0])+ '/' + str(cache[key][2]))

        holder= list(holder)

        empty= 0
        while empty< (len(holder)):                  #реанимирую слитность после list, они ведь разделились
            try:
                holder[empty]= int(holder[empty])
                holder[empty+ 1]= int(holder[empty+ 1])

            except:
                empty+= 1

            else:
                holder[empty]= int(str(holder[empty])+ str(holder[empty+ 1]))
                holder.pop(empty+ 1)

        for empty in range(len(holder)- 1):           #таким образом заменяется - на + с отрицательным числом
            if (holder[empty]== '-') and (empty== 0):
                holder.pop(empty)
                holder[empty]= -holder[empty]

            elif holder[empty]== '-':
                holder[empty]= '+'
                holder[empty+ 1]= -holder[empty+ 1]

        for empty in range(len(holder)-5):           #устраиваем переворот среди смешанных чисел в неправильные дроби
            if (type(holder[empty])== int) and (holder[empty+ 1]=='( ') and (type(holder[empty+ 2])== int) and (holder[empty+ 3]== '/') and (type(holder[empty+ 4])== int) and (holder[empty+ 5]== ')'):
                holder[empty+ 2]+= holder[empty]* holder[empty+ 4]
                holder.pop(empty)
                holder.pop(empty)
                holder.pop(empty+ 3)

        def steples(brack):                          #из названия функции понятно, что здесь наглая работа со скобками
            brack.remove('(')
            step= 0
            counter= 0
            while counter< brack.count(')'):
                step= brack.index(')', step)
                counter+= 1
            brack.pop(step)
            return brack

        def addition(first, second):                 #скромное сложение
            if (len(first)== 1) and (len(second)== 1):
                return [first[0]+ second[0]]
            elif (len(first)== 1) and (len(second)== 3):
                return [first[0]* second[2]+ second[0], '/', second[2]]
            elif (len(first)== 3) and (len(second)== 1):
                return [second[0]* first[2]+ first[0], '/', first[2]]
            elif (len(first)== 3) and (len(second)== 3):
                return [first[0]* second[2]+ second[0]* first[2], '/', first[2]* second[2]]

        def multiplication(first, second):          #скромное умножение
            if (len(first)== 1) and (len(second)== 1):
                return [first[0]* second[0]]
            elif (len(first)== 1) and (len(second)== 3):
                return [first[0]* second[0], '/', second[2]]
            elif (len(first)== 3) and (len(second)== 1):
                return [second[0]* first[0], '/', first[2]]
            elif (len(first)== 3) and (len(second)== 3):
                return [first[0]* second[0], '/', first[2]* second[2]]


        eznumbconsta= [ 2,      3,       5,     7,      11,     13,     17,     19,     23,     29,     31,     37,
                        41,     43,	    47,	    53,	    59,	    61,	    67,	    71,	    73,	    79,	    83,	    89,
                        97,     101,    103,    107,    109,    113,    127,    131,    137,    139,    149,    151,
                        157,	163,	167,	173,	179,	181,	191,	193,    197,	199,	211,	223,
                        227,	229,	233,	239,	241,	251,	257,	263,	269,	271,	277,	281,
                        283,	293,	307,	311	,   313,	317,	331,	337,	347,	349,	353,	359,
                        367,	373,	379,	383,	389,	397,	401,	409,	419,	421,	431,	433,
                        439,	443,	449,	457,	461,	463,	467,	479,	487,	491,	499,	503,
                        509,	521,	523,	541,	547,	557,	563,	569,	571,	577,	587,	593,
                        599,	601,	607,	613,	617,	619,	631,	641,	643,	647,	653,	659,
                        661,	673,	677,	683,	691,	701,	709,	719,	727,	733,	739,	743,
                        751,	757,	761,	769,	773,	787,	797,	809,	811,	821,	823,	827,
                        829,	839,	853,	857,	859,	863,	877,	881,	883,    887,	907,	911,
                        919,	929,	937,	941,	947,	953,	967,	971,	977,	983,	991,	997
                       ]
        def divisionFinder(first, second):           #здесь ищем делители(наибольший общий делитель, если быть точным)
            for nod in eznumbconsta:
                if (first[0]%nod== 0) and (second[0]%nod== 0):
                    first[0]= first[0]// nod         #gcd из math хотел вставить, но с ним почему-то не работает
                    second[0]= second[0]// nod
                    divisionFinder(first, second)

        def division(first, second):                 #скромное деление
            divisionFinder(first, second)
            return [first[0], '/', second[0]]

#       def slashdiv(first, second):
#           slash= [str(int(first[0])* int(second[2])), '/', str(int(first[2])* int(second[0]))]
#           return slash

        def power(first, second):
            first= int(first)
            second= int(second)
            return str(pow(first, second))


        def recursion(rec):                          #собственно квинтэссенция математического порядка вычислений, разделяем на два и определяем порядок действий
            if ('+' in rec) and ((('(' not in rec) and (')' not in rec)) or (rec.index('(')> rec.index('+')) or (rec.index(')')< rec.index('+'))):
                first= rec[0: rec.index('+')]
                second= rec[rec.index('+')+ 1:]
                return (addition(recursion(first), recursion(second)))
            elif ('*' in rec) and ((('(' not in rec) and (')' not in rec)) or (rec.index(')')> rec.index('*')) or (rec.index(')')< rec.index('*'))):
                first= rec[0: rec.index('*')]
                second= rec[rec.index('*')+ 1:]
                return (multiplication(recursion(first), recursion(second)))
            elif ('/' in rec) and ((('(' not in rec) and (')' not in rec)) or (rec.index(')')> rec.index('/')) or (rec.index(')')< rec.index('/'))):
                first= rec[0: rec.index('/')]
                second= rec[rec.index('/')+ 1:]
                return (division(recursion(first), recursion(second)))
            elif ('^' in rec) and ((('(' not in rec) and (')' not in rec)) or (rec.index(')') > rec.index('^')) or (rec.index(')') < rec.index('^'))):
                first = rec[0: rec.index('^')]
                second = rec[rec.index('^') + 1:]
                return (power(recursion(first), recursion(second)))        #не работает, но добавил, чтобы было
            elif ('(' in rec) and (')' in rec):
                steples(rec)
                return(recursion(rec))
            else:
                return rec
        try:
            output= recursion(holder)                     #начало рукурсивного алгоритма
            output= division([output[0]], [output[2]])    #сокращаем при возможности

            if output[0]< output[2]:                      #Вешаем еще одну обработку неправильных дробей(прям как eval())
                print(str(output[0])+ '/' + str(output[2]))
                temp.append(str(output[0])+ '/' + str(output[2]))
            elif output[0]> output[2]:
                print(str(output[0]// output[2])+ '(' + str(output[0]% output[2])+ '/' + str(output[2]) + ')')
                temp.append(str(output[0]// output[2])+ '(' + str(output[0]% output[2])+ '/' + str(output[2])+ ')')
            else:
                print(1)
            main()                                        #и все по новой..возвращение к истокам :(
        except Exception as ex:
            main()                                        #добавляем исключение, в котором мы возрващаемся к началу
main()


