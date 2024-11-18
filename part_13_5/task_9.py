#Напишите функцию convert_to_python_case(text), которая принимает в качестве аргумента строку в «верблюжьем регистре»
# и преобразует его в «змеиный регистр».

def convert_to_python_case(text):
    for i in text:
        if i.isupper():
            text = text.replace(i, '_' + i.lower())
    text = text[1:]
    return text

typed_txt = input()

print(convert_to_python_case(typed_txt))

