#На вход дается число целое n население Вселенной.
#Программа должна вывести одно число – количество выживших.

total_population = int(input())
survivor_population = total_population // 2
survivor_population_rounded = survivor_population + total_population % 2
print(survivor_population_rounded)