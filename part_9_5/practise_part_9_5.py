#isalnum(), isalpha(), isdigit(), islower(), isupper(), isspace()

s1 = 'abc123'
s2 = 'abc$*123'
s3 = ''

print(s1.isalnum())
print(s2.isalnum())
print(s3.isalnum())

s1 = 'BEEGEEK'
s2 = '2202'

print(s1.isalnum())
print(s2.isalnum())

s1 = 'ABCabc'
s2 = 'abc123'
s3 = ''

print(s1.isalpha())
print(s2.isalpha())
print(s3.isalpha())

s1 = '1234567'
s2 = 'abc123'
s3 = ''

print(s1.isdigit())
print(s2.isdigit())
print(s3.isdigit())


s1 = 'abc'
s2 = 'abc1$d'
s3 = 'Abc1$D'

print(s1.islower())
print(s2.islower())
print(s3.islower())

s1 = 'ABC'
s2 = 'ABC1$D'
s3 = 'Abc1$D'

print(s1.isupper())
print(s2.isupper())
print(s3.isupper())

s1 = '       '
s2 = 'abc1$d'

print(s1.isspace())
print(s2.isspace())