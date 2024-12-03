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

encrypted_text = ''

#count letters in the word:
for i in typed_text:
   z = 0
   for j in i:
       if j.isalpha() == True:
           z += 1
   for j in i: #encrypting
       capital_letters_position_before_encryption = eng_capital_letters.find(j)
       lowercase_letters_position_before_encryption = eng_lowercase_letters.find(j)
       capital_letters_position_after_encryption = capital_letters_position_before_encryption + z
       lowercase_letters_position_after_encryption = lowercase_letters_position_before_encryption + z
       if j.isalpha() == True:
           if j == j.upper():
               encrypted_text += eng_capital_letters[capital_letters_position_after_encryption]
           elif j == j.lower():
               encrypted_text += eng_lowercase_letters[lowercase_letters_position_after_encryption]
       else:

           encrypted_text += j
   encrypted_text += ' '
print(encrypted_text)

