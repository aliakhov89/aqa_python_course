#Как вы помните из прошлой задачи, модератору Сэму за каждый символ его сообщений в комментариях Тимур платит в 🐝 (пчелках-coin) по следующему тарифу:
#<код символа в таблице Unicode>×3🐝
#А стоимость всего сообщения складывается из суммы стоимостей всех символов.
# На этот раз Сэму захотелось схитрить и попробовать увеличить стоимость своего сообщения, заменив в нем некоторые английские буквы на русские.
# Как вы помните, русские буквы в таблице Unicode находятся после английских.


#Сэм хочет заменить следующие английские буквы:
#eyopaxcETOPAHXCBM
#на соответствующие им русские буквы:
#еуорахсЕТОРАНХСВМ

#На вход программе подается строка текста.
# Требуется написать программу, которая находит стоимость старого и нового сообщений Сэма в 🐝 и выводит текст в следующем формате:
#Старая стоимость: <стоимость старого сообщения>🐝
#Новая стоимость: <стоимость нового сообщения>🐝

typed_msg_en = input()
msg_price_old = 0
msg_price_new = 0
ru_letters = 'еуорахсЕТОРАНХСВМ'
en_letters = 'eyopaxcETOPAHXCBM'
for symbol in typed_msg_en:
    msg_price_old += ord(symbol)
sam_earn_en = msg_price_old * 3
print(f'Old price: {sam_earn_en}🐝')
#check eng letters
for symbol in typed_msg_en:
    if symbol in en_letters:
        en_index = en_letters.index(symbol)
        ru_index = en_index
        ru_letter = ru_letters[ru_index]
        msg_price_new += ord(ru_letter) * 3
    else:
        msg_price_new += ord(symbol) * 3
print(f'New price: {msg_price_new}🐝')












