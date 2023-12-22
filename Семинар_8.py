filePath = 'phonebook.txt'

def show_menu():
    print('1. Распечатать справочник\n'
        '2. Найти телефон по фамилии\n'
        '3. Изменить номер телефона\n'
        '4. Удалить запись\n'
        '5. Найти абонента по номеру телефона\n'
        '6. Добавить абонента в справочник\n'
        '7. Скопировать из другого справочника\n'
        '8. Закончить работу', sep = '\n')
    choice = int(input('Введите номер: '))
    return choice

def read_txt(filePath): 
    phone_book = []
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    with open(filePath, 'r', encoding = "utf-8") as phb:
        for line in phb:
            record = dict(zip(fields, line.split(',')))
            phone_book.append(record)
    return phone_book

def write_txt(filePath, phone_book):
    with open(filePath, 'w', encoding = "utf-8") as phout:
        for i in range(len(phone_book)):
            s = ''
            for v in phone_book[i].values():
                s += v + ','
            phout.write(f'{s[:-1]}\n')

def find_by_lastname(phone_book, last_name):
    for item in phone_book:
        if last_name == item['Фамилия']:
            return item['Телефон']
        return "Не верные данные"
    
def change_number(phone_book, last_name, new_number):
    newItem = {}
    for item in phone_book:
        if last_name == item['Фамилия']:
            newItem = item
            newItem['Телефон'] = new_number
            phone_book.remove(item)
            phone_book.append(newItem)
            write_txt(filePath, phone_book)
            return 'Номер изменен'
    return ' Абонент не найден'

def delete_by_lastname(phone_book, last_name):
    for item in phone_book:
        if last_name == item['Фамилия']:
            phone_book.remove(item)
            write_txt(filePath, phone_book)
            return 'Абонент удален'
  
    
def find_by_number(phone_book, number):
    for item in phone_book:
        if number == item['Телефон']:
            return item['Фамилия']
        return "Абанент не найден"  
            
def add_user(phone_book, user_data):
    phone_book.append(user_data)
    write_txt(filePath, phone_book)
    return 'Контакт' + user_data['Имя'] + ' ' + user_data['Фамилия'] +'добавлен'





def work_with_phonebook():

    choice = show_menu()

    phone_book = read_txt(filePath)

    while (choice != 8):

        if choice == 1:
            print(phone_book)

        elif choice == 2:
            last_name = input('Введите фамилию: ')
            print(find_by_lastname(phone_book, last_name))

        elif choice == 3:
            last_name = input('Введите фамилию: ')
            new_number = input('Введите новый номер: ')
            print(change_number(phone_book, last_name, new_number))

        elif choice == 4:
            last_name = input('Введите фамилию: ')
            print(delete_by_lastname(phone_book, last_name))

        elif choice == 5:
            number = input('Введите телефон: ')
            print(find_by_number(phone_book, number))

        elif choice == 6:
            fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
            user_data = {}
            for item in fields:
                inputStr = input('Введите' + item + ': ')
                if len(inputStr) == 0:
                    inputStr = input('Введите' + item + ': ')
                user_data[item] = inputStr
            print(add_user(phone_book, user_data))  
        elif choice == 7:
            fileName = input('Введите имя файла: ')
            if len(fileName) > 0:
                phoneList = read_txt(fileName)
                for index in range(len(phoneList)):
                    print(f'{(index + 1)}. {phoneList[index]["Имя"]} {phoneList[index]["Фамилия"]} - {phoneList[index]["Телефон"]}')
                numberItem = (int(input('Введите номер строки нужного абонента: ')) - 1)
                phone_book.append(phoneList[numberItem])
                write_txt(filePath, phone_book)
        choice = show_menu()

work_with_phonebook()
