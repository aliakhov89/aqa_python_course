#Дополните приведенный код, используя списочное выражение,
# так чтобы получить список всех чисел-палиндромов от 100 до 1000 (включительно).

#Примечание. Результирующий список должен состоять из целых чисел.

palindrom_digits = [i for i in range(100, 1001) if str(i) == str(i)[::-1]]
print(palindrom_digits)