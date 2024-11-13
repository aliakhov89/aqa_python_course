#Напишите функцию print_fio(name, surname, patronymic), которая принимает три параметра:


#name – имя человека;
#surname – фамилия человека;
#patronymic – отчество человека;

#а затем выводит на печать ФИО человека.


name = input()
surname = input()
patronymic = input()


def print_fio(name, surname, patronymic):
    print(surname[0].upper() + name[0].upper() + patronymic[0].upper())


print_fio(name, surname, patronymic)
