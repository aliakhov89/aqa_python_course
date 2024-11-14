# функция перевода градусов Фаренгейта в градусы Цельсия
def convert_to_celsius(temp):
    result = (5 / 9) * (temp - 32)
    return result

# основная программа
temp = float(input('Bвeдитe количество градусов по Фаренгейту: '))
celsius = convert_to_celsius(temp)
print(celsius)  # градусы Цельсия



def convert_grade(grade):
    if grade >= 90:
        return 5
    elif grade >= 80:
        return 4
    elif grade >= 70:
        return 3
    elif grade >= 60:
        return 2
    else:
        return 1

# основная программа
grade = int(input('Введите вашу отметку по 100-балльной системе: '))
print(convert_grade(grade))