#На вход программе подаются два числа a и b.
# Напишите программу, которая для каждого кодового значения в диапазоне от a до b (включительно), выводит соответствующий ему символ из таблицы символов Unicode.

typed_code_a, typed_code_b = int(input()), int(input())
for code in range(typed_code_a, typed_code_b + 1):
    print(chr(code), end = ' ')