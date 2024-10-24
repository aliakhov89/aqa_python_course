#Используя метод format(), дополните приведённый код так, чтобы он вывел текст:
#In 2010, someone paid 10k Bitcoin for two pizzas.
#s = 'In {0}, someone paid {1} {2} for two pizzas.'
#print()
year = 2010
amount = '10k'
currency = 'Bitcoin'
text = 'In {0}, someone paid {1} {2} for two pizzas.' .format(year, amount, currency)
print(text)