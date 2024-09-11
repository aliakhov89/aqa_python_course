#sep, end, variables, PEP 8

print('aa', 'bb', 'cc')
print('aa', 'bb', 'cc', sep=' ')  #space between raws
print('aa', 'bb', 'cc', sep='*')  #* between raws

#record sep value to variable
minus = '-'
print('aa', 'bb', 'cc', sep=minus)

print("A great man doesn't seek to lead.")
print("He's called to it. And he answers.")

print("A great man doesn't seek to lead.", end='\n')
print("He's called to it. And he answers.", end='\n')

#record end value to variable
minus = '-'
print('a', 'b', 'c', end=minus)
print('second line')

print('Python')
print()
print('C#')
print('Java')
print()
print('JavaScript')

print('a', '\n', 'b', '\n', 'c', sep='*', end='#')
print()
print('a', 'b', 'c', sep='*', end='finish')

arg1 = 'Hello'
sep1 = '_-_'
end2 = '+++'

print(arg1, 'everyone', sep=sep1, end='! ')
print('How', 'are', 'you', 'in', '2024?', sep=' ', end=end2)

print('a', 'b', 'c', sep='', end='')
print('d', 'e', 'f', sep='', end='')

print('Python', end='\n\n\n')
print('Python', sep='777')

sep1 = '#'
end2 = '?'
print('YES', 'NO', sep=sep1, end='+')
print('MAYBE', 'NEVER', sep='*', end=end2)
print()
#I***like***Python
#tasks for 2.3
#1
print('I', 'like', 'Python', sep='***')

#2

name = input()
print('Hi', name, sep=', ', end='!')

#3
separator = input()
second_raw = input()
third_raw = input()
fourth_raw = input()

print(second_raw, third_raw, fourth_raw, sep=separator)

#Multiple assignment

name, surname = 'Timur', 'Guev'
print('Имя:', name, 'Фамилия:', surname)

name = 'Timur'
surname = 'Guev'
print('Имя:', name, 'Фамилия:', surname)

name = 'Timur'
surname = 'Guev'
print('Имя:', name, 'Фамилия:', surname)

name, surname = input(), input()
print('Имя:', name, 'Фамилия:', surname)

name1 = 'Timur'
name2 = 'Gvido'

name1, name2 = name2, name1
print(name1)
print(name2)

