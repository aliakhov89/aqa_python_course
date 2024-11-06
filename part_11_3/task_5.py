#На вход программе подается натуральное число n.
# Напишите программу, которая создает список, состоящий из делителей введенного числа.

typed_nmb = int(input())
divider_list = []
for nmb in range(1, typed_nmb + 1):
    if typed_nmb % nmb == 0:
        divider_list.append(nmb)
print(divider_list)