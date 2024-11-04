#На вход программе подается натуральное число n, а затем n целых чисел.
# Напишите программу, которая создает из указанных чисел список, затем удаляет все элементы стоящие по нечетным индексам,
# а затем выводит полученный список.

typed_nmb = int(input())
numbers = []
for nmb in range(typed_nmb):
    numbers.append(int(input()))
print(numbers[0::2])


# з map
numbers = list(map(int, (input() for i in range(int(input())))))
print(numbers[0::2])