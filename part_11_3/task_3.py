#Напишите программу, выводящую следующий список:
#['a', 'bb', 'ccc', 'dddd', 'eeeee', 'ffffff', ...]


counter = 1
alphabet = []
for letter in range(97, 123):
    alphabet.append(chr(letter) * counter)
    counter += 1
print(alphabet)