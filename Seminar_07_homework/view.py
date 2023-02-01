#from controller import *

def menu():
    print('\n'
        'Введите номер действия:\n\n'
        '1. Показать справочник\n'
        '2. Поиск абонента\n'
        '3. Новый абонент\n'
        '4. Экспорт файла в ".txt"\n'
        '5. Выход\n')
    answer = int(input("Выполняется команда: "))
    return answer

def table():
    print()
    horizont = '-' * 79
    print(horizont)     
    print("| ID  | Фамилия         | Имя             | Отчество        | Телефон         |")
    print(horizont)     

def print_book(data):
    table()
    for i in range(len(data)):
        print(f"| {str(i+1).rjust(3)} | {data[i][1].ljust(15)} | {data[i][2].ljust(15)} | {data[i][3].ljust(15)} | {data[i][4].ljust(15)} |")
        print('-'*79)

def search_subscriber(data):
    name = input("Введите искомого абонента: ")
    count = 0
    print("Результат поиска: ")
    table()
    for i in range(len(data)):
        if name in data[i]:
            print(f"| {str(i+1).rjust(3)} | {data[i][1].ljust(15)} | {data[i][2].ljust(15)} | {data[i][3].ljust(15)} | {data[i][4]} |")
            print('-'*79)
            count += 1
    print(f"Найдено {count} записей.")

def new_subscriber(data):
    data.append([])  
    index = len(data)-1
    data[index].append(str(index + 1))    
    data[index].append(input("Введите фамилию: "))
    data[index].append(input("Введите имя: ")) 
    data[index].append(input("Введите отчество: "))     
    data[index].append(input("Введите номер телефона: ")) 

def export_file_txt(data):
    data1 = open (f'telephone_book.txt', 'w', encoding = 'utf-8')    
    for i in range(len(data)):
        data1.writelines(f'{("_").join(data[i])}\n')
    data1.close()

def export_file(data):
    data1 = open (f'telephone_book.txt', 'w', encoding = 'utf-8')    
    for i in range(len(data)):
        data1.writelines(f'{("_").join(data[i])}\n')
    data1.close()

def save_file_csv(data):
    data1 = open (f'telephone_book.csv', 'w', encoding = 'utf-8')    
    for i in range(len(data)):
        data1.writelines(f'{("_").join(data[i])}\n')
    data1.close()

def save_request(data):
    print("Сохранить изменения?")
    question = input("Нажмите:\nY/Д - да\nN/Н - нет\n").lower()
    if question == 'y'.lower() or question == 'д'.lower():
        save_file_csv(data)
        return False
    elif question == 'n'.lower() or question == 'н'.lower():
        return False
    else:
        print("Введен некорректный ответ")
        save_request(data)