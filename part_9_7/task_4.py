#Под "тяжестью" слова будем понимать сумму кодов по таблице Unicode всех символов этого слова.
#Напишите программу, которая принимает 4 слова и находит среди них самое тяжелое слово.
# Если самых тяжелых слов будет несколько, то программа должна вывести первое из них.

first_word, second_word, third_word, fourth_word = input(), input(), input(), input()
max_weight = 0
first_word_weight = 0
second_word_weight = 0
third_word_weight = 0
fourth_word_weight = 0
for symbol in first_word:
    first_word_weight += ord(symbol)
for symbol in second_word:
    second_word_weight += ord(symbol)
for symbol in third_word:
    third_word_weight += ord(symbol)
for symbol in fourth_word:
    fourth_word_weight += ord(symbol)
max_weight_word = max(first_word_weight, second_word_weight, third_word_weight, fourth_word_weight)
if max_weight_word == first_word_weight:
    print(first_word)
elif max_weight_word == second_word_weight:
    print(second_word)
elif max_weight_word == third_word_weight:
    print(third_word)
elif max_weight_word == fourth_word_weight:
    print(fourth_word)

#Fixed in this way:
first_word, second_word, third_word, fourth_word = input(), input(), input(), input()
max_weight = 0
max_weight_word = ""
for word in (first_word, second_word, third_word, fourth_word):
    word_weight = sum(ord(symbol) for symbol in word)
    if word_weight > max_weight:
        max_weight = word_weight
        max_weight_word = word
print(max_weight_word)
