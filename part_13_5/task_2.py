#Напишите функцию is_prime(num), которая принимает в качестве аргумента натуральное число
# и возвращает значение True, если число является простым, или False в противном случае.


def is_prime(nmb):
    if nmb == 1:
        return False
    for i in range(2, nmb):
        if nmb % i == 0:
            return False
    return True

typed_nmb = int(input())

print(is_prime(typed_nmb))