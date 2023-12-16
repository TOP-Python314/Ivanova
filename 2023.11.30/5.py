text_input = input('Введите телеграмму: ')
price_calculation = ((len(text_input.replace(' ', ''))) * 30)
price = f'{price_calculation // 100}' + ' руб. ' + f'{price_calculation % 100}' + ' коп.'
print('Цена Вашей телеграммы:', price)

# Введите телеграмму: Съешь этих мягких французских булок да выпей чаю.
# Цена Вашей телеграммы: 12 руб. 60 коп.
