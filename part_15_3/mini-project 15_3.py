#Магический шар 8
#Описание проекта: магический шар 8 (шар судьбы) — шуточный способ предсказывать будущее. Программа должна просить пользователя задать некий вопрос, чтобы случайным образом на него ответить.

#Составляющие проекта:

#Целые числа (тип int);
#Переменные;
#Ввод / вывод данных (функции input() и print());
#Условный оператор (if/elif/else);
#Цикл while;
#Бесконечный цикл;
#Операторы break, continue;
#Работа с модулем random для генерации случайных чисел.

#Подключите модуль random;
#Создайте список answers, содержащий 20 потенциальных ответов (Бесспорно, Предрешено, и т.д.).

#Выведите текстовое сообщение: 'Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.';
#Уточните как зовут пользователя;
#Выведите слова приветствия, например, 'Привет Тимур'.

#Организуйте цикл, который будет запрашивать у пользователя данные;
#Запросите у пользователя вопрос;
#Выведите случайный ответ с помощью функции choice() передав список answers в качестве аргумента;
#Уточните у пользователя, хочет ли он задать еще один вопрос,
# если да, то вернитесь в основной цикл программы,
# если нет выведите сообщение 'Возвращайся если возникнут вопросы!' и завершите программу.

import random

BALL_ANSWERS = [
    "It seems so",
    "It's unclear, try again",
    "Don't even think about it",
    "Unquestionably",
    "It is predetermined",
    "Most likely",
    "Ask again later",
    "My answer is no",
    "No doubt",
    "Good prospects",
    "Better not to tell",
    "According to my data - no",
    "Definitely yes",
    "The signs say yes",
    "Can't predict right now",
    "The prospects are not very good",
    "You can be sure about this",
    "Yes",
    "Focus and ask again",
    "Highly doubtful"
]

print('Hello, World, I am the magic ball, and I know the answer to any of your questions.')
players_name = input('Enter your name: ')
print('Hello', players_name)

#question
while True:
    question = input('Enter your question: ')
    print(random.choice(BALL_ANSWERS))
    ask_again = input('Do you want to ask again? ')
    if ask_again.lower() == 'no':
        print('Come back if you have more questions!')
        break
