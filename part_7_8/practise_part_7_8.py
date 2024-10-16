for i in range(3):
    for j in range(3):
        print(i, j)

for i in range(3):
    for j in range(3):
        if i == j:
            break
        print(i, j)

for i in range(3):
    for j in range(3):
        if i == j:
            continue
        print(i, j)
