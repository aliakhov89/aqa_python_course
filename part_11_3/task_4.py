#На вход программе подается натуральное число n, а затем n целых чисел.
# Напишите программу, которая создает из указанных чисел список их кубов.


typed_nmb = int(input())
cup_list = []
for cup_item in range(typed_nmb):
    cup_nmb = int(input())
    cup_list.append(cup_nmb ** 3 )
print(cup_list)

