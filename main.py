# print ('Hello world')
# print('Hello Git')


# Перевіряємо кратність
# num = int(input())

# if num % 3 == 0 and num % 5 == 0:
#     print("FizzBuzz")
# elif num % 3 == 0:
#     print("Fizz")
# elif num % 5 == 0:
#     print("Buzz")
# else:
#     print(num)
# fruit = "apple"

# match fruit:
#     case "apple":
#         print("This is an apple.")
#     case "banana":
#         print("This is a banana.")
#     case "orange":
#         print("This is an orange.")
#     case _:
#         print("Unknown fruit.")

'''
можно использовать начиная с Python 3.10

'''
# # Зчитування рядка від користувача
# user_input = input("Введіть рядок: ")

# # Ініціалізація змінних для підрахунку символів та пробілів
# total_chars = len(user_input)  # загальна кількість символів у рядку
# space_count = 0  # кількість пробілів

# # Підрахунок кількості пробілів
# for char in user_input:
#     if char == " ":
#         space_count += 1

# # Виведення результатів
# print(f"Загальна кількість символів у рядку: {total_chars}")
# print(f"Кількість пробілів у рядку: {space_count}")

# задача с использованием ord

# def string_to_codes(string: str) -> dict:
#     # Ініціалізація словника для зберігання кодів
#     codes = {}  
#     # Перебір кожного символу в рядку
#     for ch in string:  
#         # Перевірка, чи символ вже є в словнику
#         if ch not in codes:
#             # Додавання пари символ-код в словник  
#             codes[ch] = ord(ch)  
#     return codes

# result = string_to_codes("Hello world!")
# print(result)


# Factorial
# def factorial(n):
#     if n == 0: # базовий випадок
#         return 1
#     else:
#         return n * factorial(n-1) # рекурсивний випадок

# print(factorial(5)) # виведе 120

# Fibonacci
# def fibonacci(n):
#     if n <= 1: # базовий випадок
#         return n
#     else:
#         return fibonacci(n-1) + fibonacci(n-2) # рекурсивний випадок

# print(fibonacci(10)) # виведе 55

# def factorial(n):
#     print("Виклик функції factorial з n = ", n)
#     if n == 1:
#         print("Базовий випадок, n = 1, повернення 1")
#         return 1
#     else:
#         result = n * factorial(n-1)
#         print("Повернення результату для n = ", n, ": ", result)
#         return result

# print(factorial(5))

# выведение слов со строки списком
# text = "Lorem ipsum dolor "
# alphabet = "abcdefhijklmnopqrstuvwxyz"
# words = []
# start = 0
# for  indx, char in enumerate(text):
#     if not char.lower() in alphabet:
#         word = text[start:indx]
#         words.append(word.strip())
#         start = indx
# print (words)

# text = "Lorem ipsum dolor "
# dict_counter = {}
# for char in text:
#     counter = dict_counter.get(char, 0)
#     # try:
#     #     counter = dict_counter[char] #отримуємо значення по ключу
#     # except KeyError:
#     #     counter = 0    
#     counter += 1
#     dict_counter[char] = counter #записуємо значення по ключу
# print(dict_counter)
# first_name = Petro  
# last_name = Ivanovich
# middle_name = Zaliznyak
# def get_fullname (first_name, last_name, middle_name = ""):
#     if middle_name == "":
#         print(f"{first_name} {last_name}")
#     else:
#         print(f"{first_name} {middle_name} {last_name}")
# get_fullname("Petro", "Zaliznyak", "Ivanovich")

# def first(size, *args):
#     value = []
#     for arg in args:
#         value.append(arg)
#     print(size + len(value))
# first(5, 'first', 'second', 'third')

# def first (size, *args):
#     print (size + len(args))
# first(5, 'first', 'second', 'third')    


# Перевірка на правильність введення пароля
# password = input('Enter Password: ')

# if password == 'Password':
#     print ('Access')
# else:
#     print ('Accesse denied')
# Перевірка балансу
# balance = 0.6 + 0.7

# if round(balance, 2) >= 1.3:
#     print ('You have enough money')
# else:
#     print('You are poor')

# Використання тернарного оператора на визначення парності або непарності числа
# number = int(input('Enter natural number: '))

# result = 'even' if number % 2 == 0 else 'odd'
# print (f'Your number {number} is {result}')


# Послідовність чисел Фібоначчі
# a, b = 0, 1
# for _ in range(10):
#     print(a)
#     a, b = b, a + b


# def fibonachi(number):
#     return number if number == 1 or number == 0 else fibonachi(number-2) + fibonachi(number-1)

# print(fibonachi(3)) 


# def gretting(**kwargs):
#     # print(kwargs)
#     # Параметри дістаються через функцію довідника .get -> не створює нові значення у довіднику
#     name = kwargs.get("name", "Unknown")
#     age = kwargs.get("age", 18)
#     print(f"Hello {name}, you are have {age} years old")

# gretting(name="Oleh")
# gretting(name="Oleh", age="100")

# import datetime

# specific_day = datetime.datetime(year=2022, month=2, day=24, hour=4, minute=30, second=0)
# now_day = datetime.datetime.now()

# future_day = now_day + datetime.timedelta(10)
# print(future_day)


# from datetime import datetime

# # Встановлення дати спалення Москви Наполеоном (14 вересня 1812 року)
# napoleon_burns_moscow = datetime(year=1812, month=9, day=14)

# # Поточна дата
# current_date = datetime.now()

# # Розрахунок кількості днів
# days_since = current_date.toordinal() - napoleon_burns_moscow.toordinal()
# print(days_since)

# from datetime import datetime

# # Поточний час
# now = datetime.now()

# # Конвертація datetime в timestamp
# timestamp = datetime.timestamp(now)
# print(timestamp)  # Виведе timestamp поточного часу


# from datetime import datetime

# # Припустимо, є timestamp
# timestamp = 1807186666

# # Конвертація timestamp назад у datetime
# dt_object = datetime.fromtimestamp(timestamp)
# print(dt_object)  # Виведе відповідний datetime


# from datetime import datetime
# now = datetime.now()
# formatted_date = now.strftime("%d-%m-%Y %H:%M:%S")
# print (formatted_date)


# from datetime import datetime

# # Припустимо, у нас є дата у вигляді рядка
# date_string = "2023.03.14"

# # Перетворення рядка в об'єкт datetime
# datetime_object = datetime.strptime(date_string, "%Y.%m.%d")
# print(datetime_object)  # Виведе об'єкт datetime, що відповідає вказаній даті та часу


# from datetime import datetime

# # Створення об'єкта datetime
# now = datetime.now()

# # Отримання ISO календаря
# iso_calendar = now.isocalendar()

# print(f"ISO рік: {iso_calendar[0]}, ISO тиждень: {iso_calendar[1]}, ISO день тижня: {iso_calendar[2]}")


# from datetime import datetime, timezone

# local_now = datetime.now()
# utc_now = datetime.now(timezone.utc)

# print(local_now)
# print(utc_now)  # Виведе поточний час в UTC


# from datetime import datetime, timezone, timedelta

# utc_time = datetime.now(timezone.utc)

# # Створення часової зони для Східного часового поясу (UTC-5)
# eastern_time = utc_time.astimezone(timezone(timedelta(hours=-5)))
# # Перетворює час UTC в час Східного часового поясу
# print(eastern_time)  


# import time

# current_time = time.time()
# print(f"Поточний час: {current_time}")
# local_time = time.localtime(current_time)
# print(f"Місцевий час: {local_time}")


# import time

# print("Початок паузи")
# time.sleep(5)
# print("Кінець паузи")


# import time

# # Записуємо час на початку виконання
# start_time = time.perf_counter()

# # Виконуємо якусь операцію
# for _ in range(1_000_000):
#     pass  # Просто проходить цикл мільйон разів

# # Записуємо час після виконання операції
# end_time = time.perf_counter()

# # Розраховуємо та виводимо час виконання
# execution_time = end_time - start_time
# print(f"Час виконання: {execution_time} секунд")

# import random

# dice_roll = random.randint(1, 6)
# print(f"Ви кинули {dice_roll}")
# import random

# fill_percentage = random.random() * 100
# print(f"Заповнення: {fill_percentage:.2f}%")


# url_search = "<https://www.google.com/search?q=Cat+and+dog&ie=utf-8&oe=utf-8&aq=t>"
# _, query = url_search.split('?')
# print(query)

# obj_query = {}
# for el in query.split('&'):
#     key, value = el.split('=')
#     obj_query.update({key: value.replace('+', ' ')})
# print(obj_query)


# symbols = "0123456789ABCDEF"
# code = [
#         '0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111',
#         '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111'
#         ]

# MAP = {}

# for s, c in zip(symbols, code):
#     MAP[ord(s)] = c
#     MAP[ord(s.lower())] = c

# result = "34 DF 56 AC".translate(MAP)
# print(result)

# morze_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
#               'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
#               'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
#               'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
#               'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
#               '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
#               '8': '---..', '9': '----.'}

# # Перетворення ключів словника на Unicode коди
# table_morze_dict = {}
# for k, v in morze_dict.items():
#     table_morze_dict[ord(k)] = v

# string = "hodl"

# result = ""

# for ch in string:
#     result = result + ch.upper().translate(table_morze_dict)

# print(result)

# width = 5
# for num in range(12):
#     print(f'{num:^10} {num**2:^10} {num**3:^10}')

# import re
# text = 'Вивчення Python може бути веселим'
# pattern = 'Python'
# match = re.search(pattern, text)
# if match:
#     print ('Find out:', pattern)
# else:
#     print ('I dont find out it')

# import re

# text = "Вивчення Python може бути веселим."
# pattern = r"в\w*м" 
# '''
# r означає "сирий" рядок (raw string), який каже Python ігнорувати спеціальні символи такі як \n, \t тощо, оскільки це рядок для регулярних виразів.
# в - шукаємо слово яке починається на букву "в".
# \w* - це означає будь-яка кількість букв включно з нулем букв. Бо \w відповідає будь-якому "словесному" символу, а * є квантифікатором, який означає "нуль або більше входжень попереднього елемента".
# м - шукаємо слово яке закінчується на "м".
# '''
# match = re.search(pattern, text, re.IGNORECASE)
# '''
# В функцію search ми передаємо параметр re.IGNORECASE, який робить пошук нечутливим до регістру. А отже слово може бути як з великих так і малих літер
# '''

# if match:
#     print("Знайдено:", match.group())


# import re

# email = "username@domain.com"
# pattern = r"(\w+)@(\w+\.\w+)"
# match = re.search(pattern, email)

# if match:
#     user_name = match.group(1)
#     domain_name = match.group(2)
#     print("Ім'я користувача:", user_name)
#     print("Домен:", domain_name)

# import re

# file_name = "Мій документ Python.txt"
# pattern = r"\s"
# replacement = "_"
# formatted_name = re.sub(pattern, replacement, file_name)

# print(formatted_name) 
# from datetime import datetime 
# user_data = [{'name': 'Bill Gates', 'birthday': '1955.3.25'}, {'name': 'Steve Jobs', 'birthday': '1955.3.21'}, {'name': 'Jane Smith', 'birthday': '1990.01.27'}]
# def prepare_user_list(user_data):
# #     user_file = []
#     for user in user_data:
#         for key, value in user:
#             if key == 'birthday':
#                 user.append(datetime.strptime(value, '%Y.%m.%d'))
# print (prepare_user_list(user_data))              
# from datetime import datetime


# def string_to_date(date_string):
#     return datetime.strptime(date_string, "%Y.%m.%d").date()


# def prepare_user_list(user_data):
#     for user in user_data: 
#         for key, value in user.items():
#             print (key, value)
#             if key == "birthday":
#                 value = string_to_date(value)
#                 user_data.append(user)
#     # return user_data
# # print(prepare_user_list(user_data))     
# 


from datetime import datetime

date = input('Введіть дату у форматі "РРРР-ММ-ДД": ' )

def get_days_from_today(date):
    '''
    Ця функція розраховує різницю між заданою і поточною датами
    '''
    try:   
        given_date = datetime.strptime(date, '%Y-%m-%d')
        current_date = datetime.today()
        difference_days = given_date - current_date
        return difference_days.days
    except ValueError:
        print ('Неправильний фомат дати!',)

get_days_from_today(date)

import random

def get_numbers_ticket(min_num, max_num, quantity):
    '''
    Функція дозволяє згенерувате потрібне число унікальних чисел для лотереї
    '''
    if min_num > 0 and max_num <= 1000 and quantity >= min_num and quantity <= max_num:
        unic_numbers = []
        while len(unic_numbers) < quantity:
            unic_number = random.randint(min_num, max_num)
            if unic_number not in unic_numbers:
                unic_numbers.append(unic_number)
        return unic_numbers
    else:
        print('Числа мають бути позитивними та число випадкових чисел має бути у заданому діапазоні')
print(get_numbers_ticket(1, 49, 20))