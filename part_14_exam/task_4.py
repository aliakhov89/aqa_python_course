#Напишите функцию number_to_words(num),
# которая принимает в качестве аргумента натуральное число num и возвращает его словесное описание на русском языке.

#Примечание 1. Считайте, что число 1≤num ≤99.


s = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
     'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen',
     'eighteen', 'nineteen', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy',
     'eighty', 'ninety', '']
def number_to_words(num):
    if num <= 20:
        return s[num - 1]
    else:
        return s[num // 10 - 1 + 18] + ' ' + s[num % 10 - 1]

n = int(input())

print(number_to_words(n))