#Генератор безопасных паролей
#Описание проекта: программа генерирует заданное количество паролей и включает в себя умную настройку на длину пароля, а также на то, какие символы требуется в него включить, а какие исключить.

#Составляющие проекта:

#Целые числа (тип int);
#Переменные;
#Ввод / вывод данных (функции input() и print());
#Условный оператор (if/elif/else);
#Цикл for;
#Написание пользовательских функций;
#Работа с модулем random для генерации случайных чисел.


#Подключите модуль random;
# Создайте строковые константы:
    #digits: 0123456789;
    #lowercase_letters: abcdefghijklmnopqrstuvwxyz;
    #uppercase_letters: ABCDEFGHIJKLMNOPQRSTUVWXYZ;
    #punctuation: !#$%&*+-=?@^_.
#Создайте переменную chars = '', которая будет содержать все символы, которые могут быть в генерируемом пароле.

#Программа должна запрашивать у пользователя следующую информацию:

#Количество паролей для генерации;
#Длину одного пароля;
#Включать ли цифры 0123456789?
#Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ?
#Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz?
#Включать ли символы !#$%&*+-=?@^_?
#Исключать ли неоднозначные символы il1Lo0O?

#На основании введенной пользователем информации, сформируйте переменную chars, содержащую все символы, которые могут быть в генерируемом пароле.

#Напишите функцию generate_password(), которая принимает два аргумента:

    #length: длину пароля;
    #chars: алфавит из символов которого состоит пароль;
#и возвращает пароль.

#Используя цикл for, сгенерируйте необходимое количество паролей.


import random

# String constants
DIGITS = "0123456789"
LOWERCASE_LETTERS = "abcdefghijklmnopqrstuvwxyz"
UPPERCASE_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
PUNCTUATION = "!#$%&*+-=?@^_."


# Function to generate password
def generate_password(length, chars):
    return ''.join(random.choice(chars) for i in range(length))

# Function to handle user input and generate passwords
def generate_passwords():
    # Request user input
    num_passwords = int(input("Enter the number of passwords to generate: "))
    password_length = int(input("Enter the length of each password: "))

    # Build the available character set for the password
    chars = ''

    if input("Include digits (0123456789)? (yes/no): ").lower() == 'yes':
        chars += DIGITS
    if input("Include uppercase letters (ABCDEFGHIJKLMNOPQRSTUVWXYZ)? (yes/no): ").lower() == 'yes':
        chars += UPPERCASE_LETTERS
    if input("Include lowercase letters (abcdefghijklmnopqrstuvwxyz)? (yes/no): ").lower() == 'yes':
        chars += LOWERCASE_LETTERS
    if input("Include special characters (!#$%&*+-=?@^_)? (yes/no): ").lower() == 'yes':
        chars += PUNCTUATION
    if input("Exclude ambiguous characters (il1Lo0O)? (yes/no): ").lower() == 'yes':
        chars = ''.join([ch for ch in chars if ch not in "il1Lo0O"])

    # Check if the character set is empty
    if not chars:
        print("Error: No characters selected for the password.")
        return  # Exit the function if no characters were selected

    # Generate and print the passwords
    for _ in range(num_passwords):
        print(generate_password(password_length, chars))


generate_passwords()
