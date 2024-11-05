#На вход программе подается натуральное число n, где n≥2.
# Затем поступают n целых чисел.
# Напишите программу, которая создает из указанных чисел список, состоящий из сумм соседних чисел (0 и 1, 1 и2, 2 и 3 и т.д.).

typed_nmb = int(input())
typed_nmbs = []
adjacent_numbers = []
for nmb in range(typed_nmb):
    typed_nmbs.append(int(input()))
for nmb in range(len(typed_nmbs) - 1):
    adjacent_numbers.append(typed_nmbs[nmb] + typed_nmbs[1 + nmb])
print(adjacent_numbers)


#з урахуванням комента АЛЕ не працює
typed_nmbs = list(map(int, input().split()))
adjacent_numbers = [typed_nmbs[i] + typed_nmbs[i + 1] for i in range(len(typed_nmbs) - 1)]
print(adjacent_numbers)






