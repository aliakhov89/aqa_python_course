#На вход программе подается натуральное число n, а затем n строк.
# Напишите программу, которая создает из указанных строк список и выводит его.

typed_nmb = int(input())
row_list = []
for word in range(typed_nmb):
    typed_text = input()
    row_list.append(typed_text)
print(row_list)