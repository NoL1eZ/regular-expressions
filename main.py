from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re

with open('phonebook_raw.csv', encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
print(contacts_list)

# TODO 1: выполните пункты 1-3 ДЗ

pattern = r'\+*[8|\+7]\s*\(*(495)\)*\s*\-*(\d{3})\-*(\d{2})\-*(\d+)((\s)\(*(доб.)\s(\d+)\)*)*'
num_pattern_new = r'+7(\1)\2-\3-\4\6\7\8'
contacts_list_new = list()
for page in contacts_list:
  page_string = ','.join(page) # объединение в строку
  format_page = re.sub(pattern, num_pattern_new, page_string) # замена шаблонов в строке
  page_list = format_page.split(',') # формируем список строк
  contacts_list_new.append(page_list)

contacts_list = contacts_list_new

counter = 0
tmp = []
for contact in contacts_list:
    if contact[0].count(' ') == 2:
        line = contact[0].split(' ')
        tmp.append(line)
        for i in range(3, 7):
            tmp[counter].append(contact[i])
        counter += 1
    elif contact[0].count(' ') == 1:
        line = contact[0].split(' ')
        tmp.append(line)
        for i in range(2, 7):
            tmp[counter].append(contact[i])
        counter += 1
    elif contact[0].count(' ') == 0:
        tmp.append([contact[0]])
        if contact[1].count(' ') == 1:
            line = contact[1].split(' ')
            for info in line:
                tmp[counter].append(info)
            for i in range(3, 7):
                tmp[counter].append(contact[i])
            counter += 1
        else:
            for i in range(1, 7):
                tmp[counter].append(contact[i])
            counter += 1

# print(tmp)
contacts_list = []

for i in tmp:
    for j in tmp:
        if i[0] == j[0] and i[1] == j[1] and i is not j:
            if i[2] == '':
                i[2] = j[2]
            if i[3] == '':
                i[3] = j[3]
            if i[4] == '':
                i[4] = j[4]
            if i[5] == '':
                i[5] = j[5]
            if i[6] == '':
                i[6] = j[6]

for i in tmp:
    contacts_list.append(tuple(i))

contacts_list = list(set(contacts_list))

a = []

for i in contacts_list:
    a.append(list(i))

contacts_list = a

print(contacts_list)


# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding='utf-8') as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(contacts_list)








