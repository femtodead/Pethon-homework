# №8.1[49]. Создать телефонный справочник с возможностью импорта и экспорта данных в формате .csv

# Информация о человеке:

# Фамилия, Имя, Телефон, Описание

# Корректность и уникальность данных не обязательны.

# Функционал программы

# 1) телефонный справочник хранится в памяти в процессе выполнения кода.

# Выберите наиболее удобную структуру данных для хранения справочника.

# 2) CRUD: Create, Read, Update, Delete

# Create: Создание новой записи в справочнике: ввод всех полей новой записи, занесение ее в справочник.

# Read: он же Select. Выбор записей, удовлетворяющих заданном фильтру: по первой части фамилии человека. Берем первое совпадение по фамилии.

# Update: Изменение полей выбранной записи. Выбор записи как и в Read, заполнение новыми значениями.

# Delete: Удаление записи из справочника. Выбор - как в Read.

# 3) экспорт данных в текстовый файл формата csv

# 4) импорт данных из текстового файла формата csv

# Используйте функции для реализации значимых действий в программе

# Усложнение.

# - Сделать тесты для функций

# - Разделить на model-view-controller

def Create(phonebook): # Create: Создание новой записи в справочнике: ввод всех полей новой записи, занесение ее в справочник.
    surname = input("Введите фамилию: ")
    name = input("Введите имя: ")
    phone = input("Введите телефон: ")
    diskrip = input("Введите описание: ")
    phonebook.append([surname,name,phone,diskrip])
    yes_no = input("Сделать еще одну запись?\nДа - 1\nНет - 2\n")
    if yes_no == '1':
        return Create(phonebook)
    elif yes_no == '2':
        return export_phonebook(phonebook), menu(phonebook)
    else:
        return print("Неверная запись")
    



def Read(phonebook): # Read: он же Select. Выбор записей, удовлетворяющих заданном фильтру: по первой части фамилии человека. Берем первое совпадение по фамилии.
    surname_fragment = input("Введите часть фамилию: ")
    for idn,el in enumerate(phonebook):
        for idx,letter in enumerate(surname_fragment):
            if letter != el[0][idx]:
                break
            elif idx == len(surname_fragment)-1:
                print(idn,el)
                return idn
    menu(phonebook)
def Update(phonebook): # Update: Изменение полей выбранной записи. Выбор записи как и в Read, заполнение новыми значениями.
    idn = Read(phonebook)
    surname = input("Введите фамилию: ")
    name = input("Введите имя: ")
    phone = input("Введите телефон: ")
    diskrip = input("Введите описание: ")
    phonebook[idn]=[surname,name,phone,diskrip]
    export_phonebook(phonebook)
    menu(phonebook)


def Delete(phonebook): # Delete: Удаление записи из справочника. Выбор - как в Read.
    idn = Read(phonebook)
    phonebook.pop(idn)
    export_phonebook(phonebook)
    menu(phonebook)

def menu(phonebook): # Меню действий
    number = input("\nДобавить элемент в таблицу - 1 \nПоиск по имени - 2 \nИзменение записи - 3 \nУдаление записи - 4 \n Вернутся - 5 \nВыберете номер функции: ")
    if number == '1':
        return Create(phonebook)
    elif number == '2':
        return Read(phonebook)
    elif number == '3':
        return Update(phonebook)
    elif number == '4':
        return Delete(phonebook)
    elif number == '5':
        return main(phonebook)
    else:
        print("Номер функции введен не правильно")
# menu(phonebook)

def Print_List(phonebook): # печать + id
    print([(id+1,el) for id,el in enumerate(phonebook)])


# 3) импорт данных в текстовый файл формата csv
def Inport_phonebook(phonebook):
    import os
    datapath = os.path.join(".", 'seminar_8')
    file = open(os.path.join(datapath,file_name()), mode = "r", encoding="utf-8")
    phonebook = [el.strip().split(" ") for el in file]
    file.close()
    return phonebook


# 4) экспорт данных из текстового файла формата csv

def export_phonebook(phonebook):
    print(phonebook)
    import os
    datapath = os.path.join(".",'seminar_8')
    file = open(os.path.join(datapath,file_name()), mode = "w", encoding="utf-8")
    for el in phonebook:
        file.write(f"{el[0]} {el[1]} {el[2]} {el[3]}\n")
    file.close()

def file_name(): # название файла
    return input("Введите название файла: ")
# def file_path(): # путь файла
#     return input("Введите путь к файлу: ")

def main():
    phonebook = [] 
    phonebook = Inport_phonebook(phonebook)
    number = input("\nИмпортировать файл - 1 \nРабота с файлом - 2 \nЭкспортировать файл - 3 \nВыход - 4 \nВыберете номер: ")
    if number == '1':
        return Inport_phonebook(phonebook)
    elif number == '2':
        return menu(phonebook)
    elif number == '3':
        return export_phonebook(phonebook)
    elif number == '4':
        return
    else:
        print("Номер введен не правильно")    


main()