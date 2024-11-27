#Заголовок программы
#1.Подключите модуль random;
#2.Сгенерируйте случайное число от 1 до 100
#3. Выведите текст приветствия пользователю: 'Добро пожаловать в числовую угадайку'.

#Пользователь потенциально может ввести неверные данные, например, не число, или число превышающее 100
#Важно предусмотреть такую возможность, чтобы программа продолжала правильно работать.
# Обработка такого рода ситуаций называется защитой от дурака.

#Напишите функцию is_valid() в которую передается один строковый аргумент.
# Функция возвращает значение True если переданный аргумент является целым числом от 1 до 100 и False в противном случае.

#Организуйте цикл, который будет запрашивать у пользователя данные
# (цикл может быть бесконечным (while True) или может использовать сигнальную метку с последующим переключением, после угадывания числа);
#Запросите у пользователя число от 1 до 100
#Проверьте введенные данные с помощью функции is_valid():
#если данные некорректны, выведите текст: 'А может быть все-таки введем целое число от 1 до 100?' и перейдите к следующей итерации основного цикла;
#если данные корректны, преобразуйте их к целому числу для удобства дальнейшей работы.

#Организуйте сравнение введенного числа с загаданным числом:
#Если введенное число меньше загаданного числа, выведите текст: 'Ваше число меньше загаданного, попробуйте еще разок';
#Если введенное число больше загаданного числа, выведите текст: 'Ваше число больше загаданного, попробуйте еще разок';
#Если введенное число равно загаданному числу, выведите текст: 'Вы угадали, поздравляем!'.
#Выведите прощальное сообщение пользователю: 'Спасибо, что играли в числовую угадайку. Еще увидимся...'.

#Улучшения проекта
#Добавьте подсчет попыток, сделанных пользователем. Когда число отгадано, программа должна показать количество попыток;
#Добавьте возможность генерации нового числа (повторная игра), после того, как пользователь угадал число;
#Добавить возможность указания правой границы для случайного выбора числа (от 1 до n).


import random

def is_valid(input_string):
    if input_string.isdigit():
        number = int(input_string)
        return 1 <= number <= 100
    return False

print("Welcome to the number guessing game!")
while True:
    # Set right boarder for digit generation
    while True:
        upper_bound = input("Type right boarder for random digit (n > 1): ")
        if is_valid(upper_bound) and int(upper_bound) > 1:
            upper_bound = int(upper_bound)
            break
        else:
            print("Please, type digit not less than 1 and not more than 100 .")
    # Random digit generation
    random_number = random.randint(1, upper_bound)
    print(f"A number from 1 to {upper_bound} is guessed. Try to guess!")
    # Attempts counter
    attempts = 0
    while True:
        user_input = input("Type a digit: ")
        attempts += 1
        if not is_valid(user_input) or not (1 <= int(user_input) <= upper_bound):
            print(f"Or maybe we should introduce an integer from 1 to {upper_bound}?")
            continue

        user_number = int(user_input)
        # Compare of typed number with the guessed one
        if user_number < random_number:
            print("Your number is less than the guessed one, try again")
        elif user_number > random_number:
            print("Your number is higher than the guessed one, try again")
        else:
            print(f"You guessed it, congratulations! It took 10 {attempts} tries.")
            break  # Number is guessed, break current game
    # Play again
    play_again = input("Would you like to play again? (yes/no): ").strip().lower()
    if play_again != "yes":
        print("Thanks for playing the number guessing game. See you later...")
        break



#move to functions

import random
#Check if the input string is a valid integer.
def is_valid_number(input_string):
    return input_string.isdigit()

#Check if the number is within the specified range.
def is_within_range(number, lower_bound=1, upper_bound=100):
    return lower_bound <= number <= upper_bound

#Prompt the user for a valid upper bound.
def get_upper_bound():
    while True:
        upper_bound = input("Type the upper bound for the random digit (n > 1): ")
        if is_valid_number(upper_bound) and int(upper_bound) > 1:
            return int(upper_bound)
        else:
            print("Please, type a number greater than 1.")

#Prompt the user for a valid guess within the given upper bound.
def get_user_input(upper_bound):
    while True:
        user_input = input(f"Type a digit (1 to {upper_bound}): ")
        if not is_valid_number(user_input):
            print(f"Please, type a valid number between 1 and {upper_bound}.")
            continue
        user_number = int(user_input)
        if not is_within_range(user_number, 1, upper_bound):
            print(f"Please, choose a number between 1 and {upper_bound}.")
            continue
        return user_number

#Main function to handle the guessing game logic.
def play_game():
    print("Welcome to the number guessing game!")

    while True:
        upper_bound = get_upper_bound()
        random_number = random.randint(1, upper_bound)
        print(f"A number from 1 to {upper_bound} has been selected. Try to guess!")

        attempts = 0
        while True:
            user_number = get_user_input(upper_bound)
            attempts += 1

            # Compare the user's guess with the random number
            if user_number < random_number:
                print("Your number is less than the guessed one. Try again!")
            elif user_number > random_number:
                print("Your number is higher than the guessed one. Try again!")
            else:
                print(f"You guessed it! Congratulations! It took {attempts} tries.")
                break  # Correct guess, exit the loop

        # Ask if the player wants to play again
        play_again = input("Would you like to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            print("Thanks for playing! See you later...")
            break

# Start the game
play_game()







