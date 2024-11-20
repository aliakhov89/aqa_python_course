#Напишите функцию is_palindrome(text), которая принимает в качестве аргумента строку text
# и возвращает значение True если указанный текст является палиндромом и False в противном случае

#Примечание 1. Палиндром – это строка, которая читается одинаково в обоих направлениях

#Примечание 2. При проверке считайте большие и маленькие буквы одинаковыми, а также игнорируйте пробелы, а также символы , . ! ? -.

def is_palindrome(text):
    ignored_symbols = [',', '.', '!', '?', '-', ' ']
    for i in ignored_symbols:
        text = text.replace(i, '')
    text = text.lower()
    return text == text[::-1]

typed_txt = input()

print(is_palindrome(typed_txt))


#з isalnum()
def is_palindrome(text):
    filtered_text = ''.join(symbol.lower() for symbol in text if symbol.isalnum())
    return filtered_text == filtered_text[::-1]

typed_txt = input()
print(is_palindrome(typed_txt))