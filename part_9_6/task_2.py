#Используя f-строку, дополните приведённый код так, чтобы он вывел текст:
#In 2010, someone paid 10K Bitcoin for two pizzas.
#s = 'In {}, someone paid {} {} for two pizzas.'
#print()

year = 2010
amount = '10K'
currency = 'Bitcoin'
text = f'In {year}, someone paid {amount} {currency} for two pizzas.'
print(text)