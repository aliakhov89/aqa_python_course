#Описание проекта: требуется написать программу, способную шифровать и дешифровать текст в соответствии с алгоритмом Цезаря.
# Она должна запрашивать у пользователя следующие данные:
     #направление: шифрование или дешифрование;
     #язык алфавита: русский или английский;
     # шаг сдвига (со сдвигом вправо).
#Примечание 1. Считайте, что в русском языке 32 буквы (буква ё отсутствует).

#Примечание 2. Неалфавитные символы — знаки препинания, пробелы, цифры — не меняются.

#Примечание 3. Сохраните регистр символов. Например, текст: "Умом Россию не понять" при сдвиге на одну позицию вправо будет преобразован в: "Фнпн Спттйя ож рпоауэ".

#Составляющие проекта:

#Целые числа (тип int);
#Модульная арифметика;
#Переменные;
#Ввод / вывод данных (функции input() и print());
#Условный оператор (if/elif/else);
#Цикл for/while;
#Строковые методы.


def caesar_cipher(text, shift, alphabet, mode='encrypt'):
    result = []

    # Determine to shift to the right or to the left
    if mode == 'decrypt':
        shift = -shift

    # Convert symbols to text
    for char in text:
        if char in alphabet:
            # Get index of a symbol in the alphabet
            new_index = (alphabet.index(char) + shift) % len(alphabet)
            result.append(alphabet[new_index])
        else:
            result.append(char)

    return ''.join(result)


def get_alphabet(language):
    if language == 'russian':
        # Russian alphabet (32 letters without ё)
        return 'АБВГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЫЭЮЯабвгдежзийклмнопрстуфхцчшщыэюя'
    elif language == 'english':
        # English alphabet
        return 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'


def caesar_ciphe_main():
    print("Select alphabet language (russian/english):")
    language = input().strip().lower()

    if language not in ['russian', 'english']:
        print("Wrong language was selected.")
        return

    print("Select direction: encryption (encrypt) or decrypt (decrypt):")
    mode = input().strip().lower()

    if mode not in ['encrypt', 'decrypt']:
        print("Wrong choice of direction")
        return

    print("Enter the shift step (integer):")
    try:
        shift = int(input().strip())
    except ValueError:
        print("The shift step must be an integer.")
        return

    print("Enter text to be processed:")
    text = input()

    #Get the corresponding alphabet
    alphabet = get_alphabet(language)

    #Encrypt or decrypt text
    result = caesar_cipher(text, shift, alphabet, mode)

    #Result
    print(f"Result: {result}")



caesar_ciphe_main()
