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
