#На вход программе подается строка, содержащая английский текст.
# Напишите программу, которая подсчитывает общее количество артиклей: 'a', 'an', 'the'.

#Примечание. Артикли могут начинаться с заглавной буквы 'A', 'An', 'The'.


typed_text = input().split()
counter = 0
for word in typed_text:
    if word.lower() == 'a' or word.lower() == 'an' or word.lower() == 'the':
        counter += 1
print("Total amount of articles:", counter)


#articles in th list:

typed_text = input().split()
articles = ['a', 'an', 'the']
counter = 0
for word in typed_text:
    if word.lower() in articles:
        counter += 1
print("Total amount of articles:", counter)