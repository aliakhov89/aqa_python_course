#count(), startswith(), endswith(), find(), rfind(), index(), rindex(), strip(), lstrip(), rstrip(), replace()

s = 'foo goo moo'
print(s.count('oo'))
print(s.count('oo', 0, 8))  # подсчет с 0 по 7 символ

s = 'foobar'
print(s.startswith('foo'))
print(s.startswith('baz'))

s = 'foobar'
print(s.endswith('bar'))
print(s.endswith('baz'))

s = 'foo bar foo baz foo qux'
print(s.find('foo'))
print(s.find('bar'))
print(s.find('qu'))
print(s.find('python'))

s = 'foo bar foo baz foo qux'
print(s.index('foo'))
#print(s.index('g'))

s = '     foo bar foo baz foo qux      '
print(s.strip())

s = '     foo bar foo baz foo qux      '
print(s.lstrip())

s = '      foo bar foo baz foo qux      '
print(s.rstrip())

s = 'foo bar foo baz foo qux'
print(s.replace('foo', 'grault'))

s = 'foo bar foo baz foo qux'
print(s.replace('foo', 'grault', 2))
