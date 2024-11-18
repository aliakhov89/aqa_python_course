#BEEGEEK наконец-то открыл свой банк, в котором используются специальные банкоматы с необычным паролем.

#Действительный пароль BEEGEEK банка имеет вид a:b:c, где a, b и c – натуральные числа.
# Поскольку основатель BEEGEEK фанатеет от математики, то он решил:
#число a – должно быть палиндромом;
#число b – должно быть простым;
#число c – должно быть четным.

#Напишите функцию is_valid_password(password), которая принимает в качестве аргумента строковое значение пароля password
#и возвращает значение True, если пароль является действительным паролем BEEGEEK банка, или False в противном случае.


def is_valid_password(password):
    splited_pswd = password.split(":")
    if len(splited_pswd) != 3:
        return False
    a, b, c = splited_pswd[0], splited_pswd[1], splited_pswd[2]
    flag_a, flag_b, flag_c = False, False, False
    if a == a[::-1]:
        flag_a = True
    for i in range(2, int(b)):
        if int(b) % i == 0:
            return False
    flag_b = True
    if int(c) % 2 == 0:
        flag_c = True
    return flag_a and flag_b and flag_c

typed_psw = input()

print(is_valid_password(typed_psw))


#Отут я в тупіку - не проходить в Степіку з такими данними
#1991:1:20
# очикується шо буде False а в мене True