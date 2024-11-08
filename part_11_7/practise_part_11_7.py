zeros = []
for i in range(10):
    zeros.append(0)
print(zeros)


zeros = [0] * 10
print(zeros)

numbers = []
for i in range(10):
    numbers.append(i)
print(numbers)

numbers = [i for i in range(10)]
print(numbers)

zeros = [4 for i in range(10)]
print(zeros)

squares = [i ** 2 for i in range(10)]
print(squares)

cubes = [i ** 3 for i in range(10, 21)]
print(cubes)

chars = [j for j in 'abcdefg']
print(chars)


n = int(input())
lines = [input() for _ in range(n)]


liness = [input() for _ in range(int(input()))]


numbers = [int(input()) for _ in range(int(input()))]


evens = [i for i in range(21) if i % 2 == 0]


numbers = [i * j for i in range(1, 5) for j in range(2)]
print(numbers)

