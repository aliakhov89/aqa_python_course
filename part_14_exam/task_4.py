#Напишите функцию number_to_words(num),
# которая принимает в качестве аргумента натуральное число num и возвращает его словесное описание на русском языке.

#Примечание 1. Считайте, что число 1≤num ≤99.


S = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
     'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen',
     'eighteen', 'nineteen', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy',
     'eighty', 'ninety', '']
def number_to_words(num):
    if num <= 20:
        return S[num - 1]
    else:
        return S[num // 10 - 1 + 18] + ' ' + S[num % 10 - 1]

n = int(input())

print(number_to_words(n))




TEXT_NMBS = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
     'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen',
     'eighteen', 'nineteen', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy',
     'eighty', 'ninety', '']

def number_to_words(num, words_list):
    if num <= 20:
        return words_list[num - 1]
    else:
        return words_list[num // 10 - 1 + 18] + ' ' + words_list[num % 10 - 1] if num % 10 != 0 else words_list[num // 10 - 1 + 18]

n = int(input())
print(number_to_words(n, TEXT_NMBS))