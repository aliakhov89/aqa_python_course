#Напишите функцию get_next_prime(num), которая принимает в качестве аргумента натуральное число num
# и возвращает первое простое число, большее числа num.


def get_next_prime(nmb):
    nmb += 1
    for i in range(2, nmb):
        if nmb % i == 0:
            return get_next_prime(nmb)
    return  nmb

typed_nmb = int(input())

print(get_next_prime(typed_nmb))