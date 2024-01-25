numbers = {'0', '1'}
val = input('Ввод: ')

if val.startswith('0') or val.startswith('1'):
    x = set(val)
    if x <= numbers:
        print('Да')
    else:
        print('Нет')

elif val.startswith('b'):
    x = set(val[1:])
    if x <= numbers:
        print('Да')
    else:
        print('Нет')

elif val.startswith('0b'):
    x = set(val[2:1])
    if x <= numbers:
        print('Да')
    else:
        print('Нет')


# Ввод: 0101
# Да

# Ввод: b11
# Да

# Ввод: 0b11001
# Нет