#Напишите функцию is_password_good(password), которая принимает в качестве аргумента строковое значение пароля password
#и возвращает значение True, если пароль является надежным и False - в противном случае.

#Пароль является надежным если:
#его длина не менее 8 символов;
#он содержит как минимум одну заглавную букву (верхний регистр);
#он содержит как минимум одну строчную букву (нижний регистр);
#он содержит хотя бы одну цифру.

def is_password_good(password):
    if len(password) < 8:
        return False
    flag_upper = False
    flag_lower = False
    flag_digits = False
    for symbol in password:
        if symbol.isupper():
            flag_upper = True
        elif symbol.islower():
            flag_lower = True
        elif symbol.isdigit():
            flag_digits = True
    return flag_upper and flag_lower and flag_digits

typed_pswd = input()

print(is_password_good(typed_pswd))