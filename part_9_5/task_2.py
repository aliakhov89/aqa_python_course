#В службе по дорожному движению решили оптимизировать процесс создания автомобильных номеров: вместо человека генерацию автомобильных номеров поручили некоторой GPT (модели машинного обучения).
# Как мы знаем, искусственный интеллект ещё сыроват и делает много ошибок, поэтому его результаты следует тщательно проверять.
# Корректный автомобильный номер (в России) имеет следующий формат:

#Напишите программу, которая принимает на вход строку и проверяет, является ли эта строка корректным автомобильным номером.
# Программа должна вывести «YES» (без кавычек), если искусственный интеллект справился со своей задачей, или «NO» (без кавычек) в противном случае.
# В нашей задаче корректным автомобильным номером будем считать следующие форматы:

#<БУКВА><ЦИФРА><ЦИФРА><ЦИФРА><БУКВА><БУКВА>_<ЦИФРА><ЦИФРА>
#<БУКВА><ЦИФРА><ЦИФРА><ЦИФРА><БУКВА><БУКВА>_<ЦИФРА><ЦИФРА><ЦИФРА>
#где <ЦИФРА> – это любая цифра, а <БУКВА> – это одна из букв кириллицы АВЕКМНОРСТУХ.

#На вход программе подаётся одна строка – сгенерированный ИИ автомобильный номер.
#Программа должна вывести текст в соответствии с условием задачи.

typed_plate_nmb = input()
flag = 'NO'
allowed_letters = 'АВЕКМНОРСТУХ'
if 9 <= len(typed_plate_nmb) <= 10:
    letters_in_plate = typed_plate_nmb[0] + typed_plate_nmb[4:6]
    digits_in_plate = typed_plate_nmb[1:4] + typed_plate_nmb[7:]
    underscore = typed_plate_nmb[6]
    if digits_in_plate.isdigit() and underscore == '_':
        flag = 'YES'
    for letter in letters_in_plate:
        if letter not in allowed_letters:
            flag = 'NO'
            break
print(flag)
