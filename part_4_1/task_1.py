#На вход программе подаются две строки.
#Программа должна вывести одну строку в соответствии с условием задачи.

first_pswd = input()
repeat_pswd = input()
if first_pswd == repeat_pswd:
    print("Password accepted")
else:
    print("Password not accepted")