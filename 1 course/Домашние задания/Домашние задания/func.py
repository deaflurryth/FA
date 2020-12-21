import csv
def task1(first, second):              #Задание 1
    with open('teachers.csv', 'r') as File:
        teachbaza= csv.DictReader(File, delimiter=',', encoding='utf8')
        teach= [i for i in teachbaza if i['id']== first]
        if not teach: return None
    with open('students.csv', 'r') as File2:
        studbaza= csv.Dictreader(File2, delimiter= ',', encoding='utf8')
        stud= [i for i in studbaza if i['group_id']== second]
    with open('subjects.csv', 'r') as File3:
        subbaza= csv.Dictreader(File3, delimiter=',', encoding='utf8')
    with open('results.csv', 'r') as File4:
        resbaza= csv.DcitReader(File4, delimiter=',', encoding='utf8')
    for subject in subbaza:
        result= [for i in resbaza if i['subject']== subject['id'] and i['id']== first]
        star5= 0
        star4= 0
        star3= 0
        star2= 0
        if result:
            for student in studbaza:
                result= [i for i in result if i['student_id']== second]
                if result:
                    full= int(result['full'])
                    if 85< full< 100: star5+= 1
                    elif 70< full< 85: star4+=1
                    elif 50<full< 70: star3+=1
                    elif full<50: star2+=1
                    results= {subject['subject_name']: {"5":star5, "4":star4, "3":star3, "2":star2}}
    if results:
        return results
    else:
        return False

def task2(last_name, first_name, middle_name, to_json=False):                     #Задание 2
teachers_input = csv.DictReader(open('teachers.csv'), delimiter=";")
teacher_id = next(i for i in teachers_input if i['last_name'] == last_name and i['first_name'] == first_name and i['middle_name'] == middle_name)['id']
groups_input = csv.DictReader(open('groups.csv'), delimiter=";")
res = {}
for group in groups_input:
    value = task2(teacher_id, group['id'])
    if value:
        item = {group['name']: value}
        res.update(item)
            if to_json:
                with open(to_json, "w", encoding="utf-8") as file:
                    json.dump(res, file)
    return True
    return res

def task3(e_year, sub_name, json_=False):                                #Задание 3
    star= ''
    bigdata= {}
    groupid= [infl['id'] for infl in groups if inflp['entry_year']== (e_year)]
    groupname= {infl['id']: infl['name'] for infl in groups if infl['entry_year']== (e_year)}
    for res1 in res:
        if subjects[res1['subject']]== sub_name and students[res1['student_id']]['group_id'] in groupid:
            groupid= students[res1['student_id']][group_id]
            if int(res1['total'])> 85:
                star= '5'
            elif int(res1['total'])> 70:
                star= '4'
            elif int(res1['total'])> 50:
                star= '3'
            else:
                star= '2'
    return task3




def task4(student_id):                                    #Задание 4
    full= {'att1': 0, 'att2': 0, 'exam': 0, 'total': 0}
    for res1 in res:
        if res1['student_id']== str(student_id):
            full['att1']+= int(res1['att1'])
            full['att2'] += int(res1['att2'])
            full['exam'] += int(res1['exam'])
            full['total'] += int(res1['total'])
    return full

#Задание 5 и 6 не получилось








