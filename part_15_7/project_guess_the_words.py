#Описание проекта: программа загадывает слово, а пользователь должен его угадать.
# Изначально все буквы слова неизвестны.
# Также рисуется виселица с петлей. Пользователь предлагает букву, которая может входить в это слово.
# Если такая буква есть в слове, то программа ставит букву столько раз, сколько она встречается в слове.
# Если такой буквы нет, к виселице добавляется круг в петле, изображающий голову.
# Пользователь продолжает отгадывать буквы до тех пор, пока не отгадает всё слово.
# За каждую неудачную попытку добавляется еще одна часть туловища висельника (обычно их 6: голова, туловище, 2 руки и 2 ноги).

#Составляющие проекта:

#Целые числа (тип int);
#Переменные;
#Ввод / вывод данных (функции input() и print());
#Условный оператор (if/elif/else);
#Цикл while;
#Бесконечный цикл;
#Операторы break, continue;
#Создание пользовательских функций;
#Списочные выражения;
#Работа с модулем random для генерации случайных чисел.


#Подключите модуль random;
#Создайте глобальный список word_list, содержащий слова, которые будут использоваться в игре.

#Напишите функцию get_word() которая возвращает случайное слово из списка word_list в верхнем регистре.

#Функция display_hangman() принимает один аргумент tries – количество попыток угадывания слова –
# и возвращает текущее состояние игры в графическом виде:

    #значение tries = 6 соответствует начальному положению, пустая виселица;
    #...
    #значение tries = 0 соответствует конечному положению, то есть проигрышу и полностью нарисованному телу повешенного.
    #Примечание. Для вывода символа бэкслеша \ используется экранирование символа с помощью \, то есть комбинация \\.

#Напишите функцию play(), в которой будет осуществляться основная логика игры. Функция play() принимает в качестве аргумента слово word, сгенерированное функцией  get_word().

#def play(word):
    # тело функции
#Используйте следующие локальные переменные:

#word_completion = '_' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
#guessed = False                    # сигнальная метка
#guessed_letters = []               # список уже названных букв
#guessed_words = []                 # список уже названных слов
#tries = 6                          # количество попыток
#Функция play() в самом начале должна:
#отобразить текст 'Давайте играть в угадайку слов!';
#отобразить текущее состояние игры, распечатав результат вызова функции display_hangman() с начальным количеством допустимых промахов tries = 6;
#отобразить начальное слово word_completion в виде строки с символом _ на каждую букву задуманного слова;
#Необходимо обрабатывать ввод букв или слова целиком. Предусмотрите защиту от дурака, на случай если пользователь ввел символ, не являющийся буквой;
#Если пользователь вводит уже названную букву или слово, то необходимо ему об этом сообщить, и не засчитывать попытку;
#Если пользователь угадал букву, то требуется заменить все символы _ соответствующие этой букве;
#Если пользователь угадал слово целиком, то следует его поздравить и вывести текст 'Поздравляем, вы угадали слово! Вы победили!';
#Если пользователь исчерпал все свои попытки и не угадал слово, следует вывести загаданное слово.

#Примечание. Переводите все символы в верхний регистр.

#Основной цикл программы:
#Организуйте цикл, который будет содержать: генерацию случайного слова с помощью функции get_word(), а затем последующий вызов функции play().
#Организуйте повторный запуск игры, если пользователь пожелает играть еще раз.

#Улучшения проекта
#Можно отображать первую и последнюю букву слова;
#Слова можно выделить в категории и давать подсказку пользователю;

#Существует также вариант игры с 8 частями — добавляются ступни, а также самый длинный вариант, когда сначала за не отгаданную букву рисуются части самой виселицы.

import random

# List of words for the game
WORD_LIST = ['PYTHON', 'PROGRAMMING', 'DEVELOPER', 'COMPUTER', 'KEYBOARD', 'SOFTWARE', 'HARDWARE']


# Function to choose a random word
def get_word():
    return random.choice(WORD_LIST).upper()


# Function to display the hangman based on the number of tries
def display_hangman(tries):
    stages = [  # initial state
        '''
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        ''',
        # head
        '''
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        ''',
        # head and torso
        '''
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        ''',
        # head, torso, and one arm
        '''
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        ''',
        # head, torso, and both arms
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     
           -
        ''',
        # head, torso, both arms, and one leg
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        ''',
        # final state: head, torso, both arms, and both legs
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        '''
    ]
    return stages[6 - tries]


# Function to play the game
def play(word):
    word_completion = '_' * len(word)  # String with underscores for each letter in the word
    guessed = False  # Flag to check if the word has been guessed
    guessed_letters = []  # List of guessed letters
    guessed_words = []  # List of guessed words
    tries = 6  # Number of attempts

    print('Let\'s play the word guessing game!')
    print(display_hangman(tries))
    print(word_completion)
    print("\n")

    while not guessed and tries > 0:
        guess = input("Enter a letter or a word: ").upper()

        if len(guess) == 1 and guess.isalpha():  # If a single letter is entered
            if guess in guessed_letters:  # If the letter has already been guessed
                print(f"You already guessed the letter {guess}. Try another one.")
            elif guess not in word:  # If the letter is not in the word
                print(f"The letter {guess} is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:  # If the letter is in the word
                print(f"The letter {guess} is in the word!")
                guessed_letters.append(guess)
                word_completion = ''.join([guess if word[i] == guess else word_completion[i] for i in range(len(word))])
        elif len(guess) == len(word) and guess.isalpha():  # If a word is entered
            if guess in guessed_words:  # If the word has already been guessed
                print(f"You already guessed the word {guess}. Try again.")
            elif guess != word:  # If the word is incorrect
                print(f"The word {guess} is incorrect.")
                tries -= 1
                guessed_words.append(guess)
            else:  # If the word is correct
                guessed = True
                word_completion = word
                print(f"Congratulations, you guessed the word! You won!")
        else:
            print("Please enter only a letter or a word.")

        print(display_hangman(tries))  # Display the hangman
        print(word_completion)  # Display the current state of the word
        print("\n")

    if not guessed:
        print(f"You lost! The word was: {word}")


# Main function to run the game
def main():
    while True:
        word = get_word()  # Get a random word
        play(word)  # Play the guessing game
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break


# Start the game
main()

