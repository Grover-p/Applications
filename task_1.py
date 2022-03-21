from chardet import detect
import csv
import re


list_file = ['info_1.txt', 'info_2.txt', 'info_3.txt']


content = [['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']]

for el in list_file:
    data_list = []
    with open(f'{el}', 'rb') as txt_file:
        CONTENT = txt_file.read()
        ENCODING = detect(CONTENT)['encoding']
        data = CONTENT.decode(ENCODING)

    sys_manufacturer = re.compile(r'Изготовитель системы:\s*\S*')
    data_list.append(sys_manufacturer.findall(data)[0].split()[2])

    os = re.compile(r'Windows\s\S*')
    data_list.append(os.findall(data)[0])

    product_code = re.compile(r'Код продукта:\s*\S*')
    data_list.append(product_code.findall(data)[0].split()[2])

    type_manufacturer = re.compile(r'Тип системы:\s*\S*')
    data_list.append(type_manufacturer.findall(data)[0].split()[2])

    content.append(data_list)


with open('out_file.csv', 'w', encoding='utf-8') as f_n:
    for row in content:
        file_writer = csv.writer(f_n, lineterminator="\n")
        file_writer.writerow(row)