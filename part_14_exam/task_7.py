#Панграмма – это фраза, содержащая в себе все буквы алфавита.
# Обычно панграммы используют для презентации шрифтов, чтобы можно было в одной фразе рассмотреть все глифы.

#Напишите функцию is_pangram(text), которая принимает в качестве аргумента строку текста на английском языке
# и возвращает значение True, если текст является панграммой, или значение False в противном случае.

#Примечание. Гарантируется, что введённая строка содержит только буквы английского алфавита и пробелы.

def is_pangram(text):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for letter in text.lower():
        if letter in letters:
            letters.remove(letter)
    return len(letters) == 0

# считываем данные
text = input()

# вызываем функцию
print(is_pangram(text))




def is_pangram(text):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    text_set = set(text.lower().replace(' ', ''))
    return alphabet <= text_set

text = input()

print(is_pangram(text))