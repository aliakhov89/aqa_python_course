#ord()
num1 = ord('A')
num2 = ord('B')
num3 = ord('a')
print(num1, num2, num3)

#chr()

chr1 = chr(65)
chr2 = chr(75)
chr3 = chr(110)

print(chr1, chr2, chr3)

for i in range(26):
    print(chr(ord('A') + i))