#На вход программе подается последовательность слов, каждое слово на отдельной строке.
# Концом последовательности является слово «КОНЕЦ» или «конец» (большими или маленькими буквами, без кавычек).
# При этом сами слова «КОНЕЦ» и «конец» не входят в последовательность, лишь символизируя её окончание.
# Напишите программу, которая выводит члены данной последовательности.

typed_text = input()
while typed_text != 'end' and typed_text != 'END':
    print(typed_text)
    typed_text = input()