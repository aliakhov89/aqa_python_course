#На вход программе подается строка текста на английском языке, в которой нужно зашифровать все слова.
#Каждое слово строки следует зашифровать с помощью шифра Цезаря (циклического сдвига на длину этого слова).
# Строчные буквы при этом остаются строчными, а прописные – прописными.
# Гарантируется, что между различными словами присутствует один пробел.

#Формат входных данных
#На вход программе подается строка текста на английском языке.

#Формат выходных данных
#Программа должна вывести зашифрованный текст в соответствии с условием задачи.

#Примечание. Символы, не являющиеся английскими буквами, не изменяются.


eng_capital_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
eng_lowercase_letters = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'

typed_text = input().split()

encrypted_text = ' '.join([ # Count the number of letters in the word using sum() and List Comprehension
    ''.join([(eng_capital_letters[(eng_capital_letters.find(char) + sum(1 for c in word if c.isalpha()))] if char.isupper()
            else
            eng_lowercase_letters[(eng_lowercase_letters.find(char) + sum(1 for c in word if c.isalpha()))]) if char.isalpha()
        else char  # If the character is not a letter, keep it unchanged
        for char in word
    ])
    for word in typed_text
])

print(encrypted_text)

