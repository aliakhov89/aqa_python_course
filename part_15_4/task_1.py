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
digits = "0123456789"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation = "!#$%&*+-=?@^_."


# Function to generate password
def generate_password(length, chars):
    password = ''.join(random.choice(chars) for i in range(length))
    return password


# Function to handle user input and generate passwords
def generate_passwords():
    # Request user input
    num_passwords = int(input("Enter the number of passwords to generate: "))
    password_length = int(input("Enter the length of each password: "))

    # Build the available character set for the password
    chars = ''

    include_digits = input("Include digits (0123456789)? (yes/no): ").lower() == 'yes'
    include_uppercase = input("Include uppercase letters (ABCDEFGHIJKLMNOPQRSTUVWXYZ)? (yes/no): ").lower() == 'yes'
    include_lowercase = input("Include lowercase letters (abcdefghijklmnopqrstuvwxyz)? (yes/no): ").lower() == 'yes'
    include_punctuation = input("Include special characters (!#$%&*+-=?@^_)? (yes/no): ").lower() == 'yes'
    exclude_ambiguous = input("Exclude ambiguous characters (il1Lo0O)? (yes/no): ").lower() == 'yes'

    # Build the character set for password generation
    if include_digits:
        chars += digits
    if include_uppercase:
        chars += uppercase_letters
    if include_lowercase:
        chars += lowercase_letters
    if include_punctuation:
        chars += punctuation
    if exclude_ambiguous:# Remove ambiguous characters
        ambiguous_chars = "il1Lo0O"
        chars = ''.join([ch for ch in chars if ch not in ambiguous_chars])

    # Generate and print the passwords
    for _ in range(num_passwords):
        password = generate_password(password_length, chars)
        print(password)

generate_passwords()
